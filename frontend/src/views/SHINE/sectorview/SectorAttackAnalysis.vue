<template>
  <div class="content midover">
    <sidebox/>
    <div class="md-layout">
      <div class="md-layout-item  md-size-90">
        <alert>
          <h4 >Sector Incident Attack Analsis</h4>
        </alert>
        <el-select v-model="sector" @change="changeFillData($event)" filterable placeholder="Business Sector">
                <el-option v-for="item in SectorOptions" :key="item.sectorid" :label="item.sector_name" :value="item.sectorid">
                  {{item.sector_name}}
                </el-option>
              </el-select>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item  midcardsize viewb">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Incident Category</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="incidentcategoryData" :options="incidentcategoryOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item cardsize viewb">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Top IP Watchlist</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="ipwatchlistData" :options="ipwatchlistOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item  cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Top Domain Watchlist</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="domainwatchlistData" :options="domainwatchlistOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item  cardsize viewb">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Top URL Watchlist</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="urlwatchlistData" :options="urlwatchlistOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item  cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Top Malicious E-mail</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="maliciousemailData" :options="maliciousemailOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item  cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Top File Hash Watchlist</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="filehashData" :options="filehashOption"/>
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
        <md-button md-menu-trigger class=' md-raised toggle' to="/Sectorview">Back to Sectorview</md-button>
        </md-menu>
      </div>
    </div>
  </div>
</template>

<script>
// import PieChart from '../../../components/Charts/PieChart'
import BarChart from '../../../components/Charts/BarChart'
// import PolarAreaChart from '../../../components/Charts/PolarAreaChart'
import Sidebox from '../../../components/Sidebox'
import { shinebaseurl } from '@/config/variables.js'
export default {
  components: {
    // PieChart,
    BarChart,
    // PolarAreaChart,
    Sidebox
  },
  data () {
    return {
      sector: null,
      SectorOptions: null,
      loaded: false,
      maliciousemailData: null,
      maliciousemailOption: null,
      ipwatchlistData: null,
      ipwatchlistOption: null,
      filehashData: null,
      filehashOption: null,
      domainwatchlistData: null,
      domainwatchlistOption: null,
      urlwatchlistData: null,
      urlwatchlistOption: null,
      incidentcategoryData: null,
      incidentcategoryOption: null,
      defaultsector: null,
      UserID: null
    }
  },
  mounted: async function () {
    this.getSector()
    let userurl = `${shinebaseurl}:8080/auth/info`
    var res = await fetch(userurl, { credentials: 'include' })
    var info = await res.json()
    this.UserID = info.id
    // console.log(this.UserID)
    let sectorurl = `${shinebaseurl}/userinfo/api/UserDetail/` + this.UserID
    var res1 = await fetch(sectorurl)
    var info1 = await res1.json()
    this.defaultsector = info1.sectorid
    // console.log(this.defaultsector)
    this.fillmaliciousemailData(this.defaultsector)
    this.fillipwatchlistData(this.defaultsector)
    this.fillfilehashData(this.defaultsector)
    this.filldomainwatchlistData(this.defaultsector)
    this.fillurlwatchlistData(this.defaultsector)
    this.fillincidentcategoryData(this.defaultsector)
  },
  methods: {
    changeFillData (event) {
      this.fillmaliciousemailData(event)
      this.fillipwatchlistData(event)
      this.fillfilehashData(event)
      this.filldomainwatchlistData(event)
      this.fillurlwatchlistData(event)
      this.fillincidentcategoryData(event)
    },
    getSector () {
      // let data={};
      let url = `${shinebaseurl}/sector/api/sector_list/?is_valid=true`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
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
    fillmaliciousemailData (event) {
      let url = `${shinebaseurl}/attackinfo/api/YearlyTopMaliciousEmailWatchlist/sector/` + event
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          let results = res.data
          // console.log(results)
          let labels = results.map(a => a.watchlist)
          let data = results.map(a => a.times)
          this.maliciousemailOption = {
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.maliciousemailData = {
            labels: labels,
            datasets: [
              {
                backgroundColor: ['#a1cae2', '#faf3e0', '#99bbad', '#e7e6e1', '#413c69'],
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    fillipwatchlistData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/YearlyTopIpWatchlist/sector/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.watchlist
          let data = results.times
          this.ipwatchlistOption = {
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: true
                },
                gridLines: {
                  display: false
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Numbers'
                },
                stacked: true
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
                  labelString: 'Top Ip Watchlist'
                }
              }]
            },
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.ipwatchlistData = {
            labels: labels,
            datasets: [
              {
                backgroundColor: ['#a1cae2', '#faf3e0', '#99bbad', '#e7e6e1', '#413c69'],
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    fillfilehashData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/YearlyTopFileHashWatchlist/sector/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.watchlist)
          let data = results.map(a => a.times)
          this.filehashOption = {
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: true
                },
                gridLines: {
                  display: false
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Numbers'
                },
                stacked: true
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
                  labelString: 'Top File Hash Watchlist'
                }
              }]
            },
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.filehashData = {
            labels: labels,
            datasets: [
              {
                backgroundColor: ['#a1cae2', '#faf3e0', '#99bbad', '#e7e6e1', '#413c69'],
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    filldomainwatchlistData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/YearlyTopDomainWatchlis/sector/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.watchlist)
          let data = results.map(a => a.times)
          this.domainwatchlistOption = {
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: true
                },
                gridLines: {
                  display: false
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Numbers'
                },
                stacked: true
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
                  labelString: 'Top Domain Watchlist'
                }
              }]
            },
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.domainwatchlistData = {
            labels: labels,
            datasets: [
              {
                backgroundColor: ['#a1cae2', '#faf3e0', '#99bbad', '#e7e6e1', '#413c69'],
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    fillurlwatchlistData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/YearlyTopURLWatchlist/sector/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.watchlist)
          let data = results.map(a => a.times)
          this.urlwatchlistOption = {
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: true
                },
                gridLines: {
                  display: false
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Numbers'
                },
                stacked: true
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
                  labelString: 'Top URL Watchlist'
                }
              }]
            },
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.fillurlwatchlistData = {
            labels: labels,
            datasets: [
              {
                backgroundColor: ['#a1cae2', '#faf3e0', '#99bbad', '#e7e6e1', '#413c69'],
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    fillincidentcategoryData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/MonthlyIncidentCateList/sector/` + event)
        .then((res) => {
          let results = res.data
          let res1 = []
          let res2 = []
          let res3 = []
          let res4 = []
          let res5 = []
          let res6 = []
          let res7 = []
          var i1 = 0
          var i2 = 0
          var i3 = 0
          var i4 = 0
          var i5 = 0
          var i6 = 0
          var i7 = 0
          for (var i = 0; i < results.length; i++) {
            switch (results[i].incident_category__incident_category) {
              case 'Exercise/Network Defense Testing':
                res1[i1] = results[i]
                i1++
                break
              case 'Scans/Probes/Attempted Access':
                res2[i2] = results[i]
                i2++
                break
              case 'Denial of Service':
                res3[i3] = results[i]
                i3++
                break
              case 'Investigation':
                res4[i4] = results[i]
                i4++
                break
              case 'Malicious Code':
                res5[i5] = results[i]
                i5++
                break
              case 'Improper Usage':
                res6[i6] = results[i]
                i6++
                break
              case 'Unauthorized Access':
                res7[i7] = results[i]
                i7++
                break
            }
          }
          let labels = Array.from(new Set(results.map(a => a.attack_id__start_time_stamp__month)))
          let labels1 = Array.from(new Set(res1.map(a => a.attack_id__start_time_stamp__month)))
          let labels2 = Array.from(new Set(res2.map(a => a.attack_id__start_time_stamp__month)))
          let labels3 = Array.from(new Set(res3.map(a => a.attack_id__start_time_stamp__month)))
          let labels4 = Array.from(new Set(res4.map(a => a.attack_id__start_time_stamp__month)))
          let labels5 = Array.from(new Set(res5.map(a => a.attack_id__start_time_stamp__month)))
          let labels6 = Array.from(new Set(res6.map(a => a.attack_id__start_time_stamp__month)))
          let labels7 = Array.from(new Set(res7.map(a => a.attack_id__start_time_stamp__month)))
          let data1 = res1.map(a => a.total)
          let data2 = res2.map(a => a.total)
          let data3 = res3.map(a => a.total)
          let data4 = res4.map(a => a.total)
          let data5 = res5.map(a => a.total)
          let data6 = res6.map(a => a.total)
          let data7 = res7.map(a => a.total)
          for (var j = 0; j < labels.length; j++) {
            if (labels1[j] !== labels[j]) {
              data1.splice(j, 0, 0)
              labels1.splice(j, 0, 0)
            }
            if (labels2[j] !== labels[j]) {
              data2.splice(j, 0, 0)
              labels2.splice(j, 0, 0)
            }
            if (labels3[j] !== labels[j]) {
              data3.splice(j, 0, 0)
              labels3.splice(j, 0, 0)
            }
            if (labels4[j] !== labels[j]) {
              data4.splice(j, 0, 0)
              labels4.splice(j, 0, 0)
            }
            if (labels5[j] !== labels[j]) {
              data5.splice(j, 0, 0)
              labels5.splice(j, 0, 0)
            }
            if (labels6[j] !== labels[j]) {
              data6.splice(j, 0, 0)
              labels6.splice(j, 0, 0)
            }
            if (labels7[j] !== labels[j]) {
              data7.splice(j, 0, 0)
              labels7.splice(j, 0, 0)
            }
          }
          this.incidentcategoryOption = {
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: true
                },
                gridLines: {
                  display: false
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Numbers'
                },
                stacked: true
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
                },
                stacked: true
              }]
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.incidentcategoryData = {
            labels: labels,
            datasets: [
              {
                label: 'Exercise/Network Defense Testing',
                backgroundColor: '#d8e3e7',
                data: data1
              },
              {
                label: 'Scans/Probes/Attempted Access',
                backgroundColor: '#98ddca',
                data: data2
              },
              {
                label: 'Denial of Service',
                backgroundColor: '#bfcba8',
                data: data3
              },
              {
                label: 'Investigation',
                backgroundColor: '#864000',
                data: data4
              },
              {
                label: 'Malicious Code',
                backgroundColor: '#f3f4ed',
                data: data5
              },
              {
                label: 'Improper Usage',
                backgroundColor: '#f8f4e1',
                data: data6
              },
              {
                label: 'Unauthorized Access',
                backgroundColor: '#f39189',
                data: data7
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
