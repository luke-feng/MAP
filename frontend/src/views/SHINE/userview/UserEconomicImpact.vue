<template>
  <div class="content midover">
    <sidebox/>
    <div class="md-layout">
      <div class="md-layout-item  md-size-90">
        <alert>
          <h4 >User Economic Impact Analsis</h4>
        </alert>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item longcardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Rank of Measures</div>
              <el-select v-model="incidentcategory" @change="filltableData($event)" filterable placeholder="Incident Category">
                    <el-option v-for="item in IncidentCategoryOptions" :key="item.incident_category_id" :label="item.incident_category" :value="item.incident_category_id">
                      {{item.incident_category}}
                    </el-option>
              </el-select>
            </md-card-header>
            <md-card-content>
              <el-table
                :data="tableData"
                height="250"
                style="width: 100%">
                <el-table-column
                  prop="incident_category_name"
                  label="Attack Tpye">
                </el-table-column>
                <el-table-column
                  prop="measure_type_name"
                  label="Measure Tpye">
                </el-table-column>
                <el-table-column
                  prop="measure_description"
                  label="Measure Description">
                </el-table-column>
                <el-table-column
                  prop="rosi"
                  label="ROSI">
                </el-table-column>
                <el-table-column
                  prop="npv"
                  label="NPV">
                </el-table-column>
              </el-table>
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
    <div class="md-layout-item  cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Average Loss in Different Types of Cyberattacks</div>
            </md-card-header>
            <md-card-content>
              <PolarAreaChart :chartData="averageoflossData" :options="averageoflossOption"/>
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
      <div class="md-layout-item  cardsize viewb">
      </div>
    <div class="md-layout-item  cardsize viewb">
      </div>
      <div class="md-layout-item morebottonsize viewm" >
        <md-menu>
        <md-button md-menu-trigger class=' md-raised toggle' to="/userview">Back to Userrview</md-button>
        </md-menu>
      </div>
    </div>
  </div>
</template>

<script>
import BarChart from '../../../components/Charts/BarChart'
import PieChart from '../../../components/Charts/PieChart'
import PolarAreaChart from '../../../components/Charts/PolarAreaChart'
import Sidebox from '../../../components/Sidebox'
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
      monthlylossData: null,
      montylylossOption: null,
      shareoflossOption: null,
      shareoflossData: null,
      organizationid: null,
      UserID: null,
      tableData: [],
      IncidentCategoryOptions: [],
      incidentcategory: null,
      averageoflossData: null,
      averageoflossOption: null,
      sharetypelossOption: null,
      sharetypelossData: null
    }
  },
  mounted: async function () {
    let userurl = `${shinebaseurl}:8080/auth/info`
    var res = await fetch(userurl, { credentials: 'include' })
    var info = await res.json()
    this.UserID = info.id
    // console.log(this.UserID)
    let sectorurl = `${shinebaseurl}/userinfo/api/UserDetail/` + this.UserID
    var res1 = await fetch(sectorurl)
    var info1 = await res1.json()
    this.organizationid = info1.organizationid
    this.fillmonthlylossData(this.organizationid)
    await this.fillshareoflossOption(this.organizationid)
    await this.getdefaultIncidentCategory()
    this.getIncidentCategoryOptions()
    this.filltableData(this.incidentcategory)
    this.fillaverageoflossData(this.organizationid)
    this.fillsharetypelossOption(this.organizationid)
  },
  methods: {
    async getIncidentCategoryOptions () {
      await this.$axios.get(`${shinebaseurl}/info_share/api/IncidentcategoryList/`)
        .then((res) => {
          this.IncidentCategoryOptions = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    async getdefaultIncidentCategory () {
      await this.$axios.get(`${shinebaseurl}/measures/api/MeasureRecordListByUser/` + this.UserID)
        .then((res) => {
          let results = res.data
          if (results.length === 0) {
            this.incidentcategory = 1
          } else {
            this.incidentcategory = results[0].incident_category
          }
        }).catch(function (error) {
          console.log(error)
        })
    },
    filltableData (event) {
      let url = `${shinebaseurl}/measures/api/MeasureRecordList/` + this.UserID + '/' + event
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          let results = res.data
          // console.log(results)
          this.tableData = results
        })
        .catch(error => {
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
    fillmonthlylossData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/MonthlyLossSum/org/` + event)
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
    async fillshareoflossOption (event) {
      await this.$axios.get(`${shinebaseurl}/attackinfo/api/AttackTypeLossSum/org/` + event)
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
    },
    async fillsharetypelossOption (event) {
      await this.$axios.get(`${shinebaseurl}/attackinfo/api/YearlyLossSumByLossCate/org/` + event)
        .then((res) => {
          let results = res.data
          let labels = ['Cost of Equipment Replacement', 'Cost of Repair', 'Corporate Income Loss', 'Organization Productive Loss', 'SLA Loss', 'Indirect Loss']
          let data = [results[0].total_coer, results[0].total_cor, results[0].total_col, results[0].total_opl, results[0].total_sla, results[0].total_il]
          // console.log(data)
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
    async fillaverageoflossData (event) {
      await this.$axios.get(`${shinebaseurl}/attackinfo/api/overviewIncidentCate/org/` + event)
        .then((res) => {
          let results = res.data
          // console.log(results)
          let labels = results.map(a => a.incident_category__incident_category)
          let attackdata = results.map(a => a.total)
          // console.log(attackdata)
          let lossdata = this.shareoflossData.datasets[0].data
          // console.log(lossdata)
          let data = []
          for (var i = 0; i < lossdata.length; i++) {
            if (attackdata[i] === 0) {
              data[i] = 0
            } else {
              data[i] = lossdata[i] / attackdata[i]
            }
          }
          this.averageoflossOption = {
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.averageoflossData = {
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
