<template>
  <div class="content midover">
    <sidebox/>
    <div class="md-layout">
      <div class="md-layout-item  md-size-90">
        <alert>
          <h4 >Sector Economic Impact Analsis</h4>
        </alert>
        <el-select v-model="sector" @change="changeFillData($event)" filterable placeholder="Business Sector">
                <el-option v-for="item in SectorOptions" :key="item.sectorid" :label="item.sector_name" :value="item.sectorid">
                  {{item.sector_name}}
                </el-option>
              </el-select>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Total Losses in Each Sector</div>
            </md-card-header>
            <md-card-content>
              <PolarAreaChart :chartData="totallossData" :options="totallossOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Monthly Losses Cuased by Cyberattack</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="monthlylossData" :options="montylylossOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item  cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Share of Losses Caused by Different Types of Cyberattacks</div>
            </md-card-header>
            <md-card-content>
              <PieChart :chartData="shareoflossData" :options="shareoflossOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Share of Different Types of Loss</div>
            </md-card-header>
            <md-card-content>
              <PieChart :chartData="sharetypelossData" :options="sharetypelossOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item cardsize viewb">
      </div>
      <div class="md-layout-item  cardsize viewb">
      </div>
      <div class="md-layout-item morebottonsize viewm" >
        <md-menu>
        <md-button md-menu-trigger class=' md-raised toggle' to="/Sectorview">Back to Sectorview</md-button>
        </md-menu>
      </div>
    </div>
  </div>
</template>

<script>
import BarChart from '../../../components/Charts/BarChart'
import PieChart from '../../../components/Charts/PieChart'
import Sidebox from '../../../components/Sidebox'
import PolarAreaChart from '../../../components/Charts/PolarAreaChart'
import { shinebaseurl } from '@/config/variables.js'
export default {

  components: {
    BarChart,
    PieChart,
    PolarAreaChart,
    Sidebox
  },
  data () {
    return {
      sector: null,
      SectorOptions: null,
      loaded: false,
      totallossData: null,
      totallossOption: null,
      monthlylossData: null,
      montylylossOption: null,
      shareoflossOption: null,
      shareoflossData: null,
      defaultsector: null,
      UserID: null,
      sharetypelossOption: null,
      sharetypelossData: null
    }
  },
  mounted: async function () {
    this.getSector()
    let userurl = `${shinebaseurl}:8080/auth/info`
    var res = await fetch(userurl, { credentials: 'include' })
    var info = await res.json()
    this.UserID = info.id
    let sectorurl = `${shinebaseurl}/userinfo/api/UserDetail/` + this.UserID
    var res1 = await fetch(sectorurl)
    var info1 = await res1.json()
    this.defaultsector = info1.sectorid
    this.fillaveragelossData(this.defaultsector)
    this.fillmonthlylossData(this.defaultsector)
    this.fillshareoflossOption(this.defaultsector)
    this.fillsharetypelossOption(this.defaultsector)
  },
  methods: {
    changeFillData (event) {
      this.fillaveragelossData(event)
      this.fillmonthlylossData(event)
      this.fillshareoflossOption(event)
      this.fillsharetypelossOption(event)
    },
    getSector () {
      let url = `${shinebaseurl}/sector/api/sector_list/?is_valid=true`
      this.$axios.get(url)
        .then((res) => {
          this.SectorOptions = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    onItemClick (e, i) {
      console.log('onItemClick')
    },
    onCollapse (c) {
      console.log('onCollapse')
      this.collapsed = c
    },
    async fillsharetypelossOption (event) {
      await this.$axios.get(`${shinebaseurl}/attackinfo/api/YearlyLossSumByLossCate/sector/` + event)
        .then((res) => {
          let results = res.data
          let labels = ['Cost of Equipment Replacement', 'Cost of Repair', 'Corporate Income Loss', 'Organization Productive Loss', 'SLA Loss', 'Indirect Loss']
          let data = [results[0].total_coer, results[0].total_cor, results[0].total_col, results[0].total_opl, results[0].total_sla, results[0].total_il]
          this.sharetypelossOption = {
            responsive: true,
            maintainAspectRatio: false
          }
          this.sharetypelossData = {
            labels: labels,
            datasets: [
              {
                backgroundColor: ['#d8e3e7', '#98ddca', '#bfcba8', '#864000', '#f3f4ed', '#f8f4e1', '#f39189', '#f0e4d7', '#4a3933'],
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    fillaveragelossData (event) {
      let url = `${shinebaseurl}/attackinfo/api/YearlyLossSumBySector/`
      this.$axios.get(url)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.sector_id__sector_name)
          let data = results.map(a => a.total_loss)
          this.totallossOption = {
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.totallossData = {
            labels: labels,
            datasets: [
              {
                label: 'Total Loss',
                backgroundColor: ['#F7AA97', '#D4DFE6', '#E0E3DA'],
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    fillmonthlylossData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/MonthlyLossSum/sector/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.attack_id__start_time_stamp__month)
          let data = results.map(a => a.total_loss)
          this.montylylossOption = {
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: true
                },
                gridLines: {
                  display: true
                },
                scaleLabel: {
                  display: true,
                  labelString: 'EUROs'
                }
              }],
              xAxes: [ {
                ticks: {
                  beginAtZero: true
                },
                gridLines: {
                  display: false
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Month'
                }
              }]
            },
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.monthlylossData = {
            labels: labels,
            datasets: [
              {
                label: 'Losses',
                borderColor: 'white',
                pointBackgroundColor: 'white',
                backgroundColor: '#a3daff',
                borderWidth: 1,
                pointBorderColor: 'white',
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    fillshareoflossOption (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/AttackTypeLossSum/sector/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.incident_category__incident_category)
          let data = results.map(a => a.total_loss)
          this.shareoflossOption = {
            responsive: true,
            maintainAspectRatio: false
          }
          this.shareoflossData = {
            labels: labels,
            datasets: [
              {
                backgroundColor: ['#d8e3e7', '#98ddca', '#bfcba8', '#864000', '#f3f4ed', '#f8f4e1', '#f39189', '#f0e4d7', '#4a3933'],
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
<style>
</style>
