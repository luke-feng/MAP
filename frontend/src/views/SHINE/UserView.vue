<template>
  <div class="content midover">
    <sidebox/>
    <div class="md-layout">
      <div class="md-layout-item  md-size-90">
        <alert>
          <h4 >User View</h4>
        </alert>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item  viewbottonsize viewb" >
        <popover  content="Economic impact view" trigger="hover" placement="bottomLeft ">
          <md-button class="md-raised md-primary">Economic View</md-button>
        </popover>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Monthly Losses Caused by Cyberattack</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="monthlylossesData" :options="monthlylossesOption"/>
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
              <DoughnutChart :chartData="shareoflossData" :options="shareoflossOption"/>
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
              <PolarAreaChart :chartData="averageoflossData" :options="averageoflossOpinion"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item morebottonsize viewm" >
        <md-menu>
        <md-button md-menu-trigger class=' md-raised toggle'>More Economic Views</md-button>
        <md-menu-content>
          <md-menu-item to="/userview/economic">Economic Impact Analysis</md-menu-item>
          <md-menu-item to="/userview/measure">Security Measure Analysis</md-menu-item>
          <md-menu-item to="/Overview">Back to Overview</md-menu-item>
        </md-menu-content>
        </md-menu>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item" >
        <popover  content="Technical information view" trigger="hover" placement="bottomLeft ">
           <md-button class="md-raised md-primary">Incident statistics</md-button>
        </popover>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item midcardsize viewb">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Monthly Number of Attacks</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="mothlynumberData" :options="mothlynumberOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item  cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Number of Attacks in Each Incident Category</div>
            </md-card-header>
            <md-card-content>
              <PieChart :chartData="shareoftypeData" :options="shareoftypeOption"/>
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
              <div class="md-subheading">Top 5 Attacked System</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="shareofsystemData" :options="shareofsystemOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item  cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Top 5 Attacked Asset</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="shareofassetData" :options="shareofassetOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item cardsize viewb">
      </div>
      <div class="md-layout-item morebottonsize viewm" >
        <md-menu>
        <md-button md-menu-trigger class=' md-raised toggle'>More Inights Views</md-button>
        <md-menu-content>
          <md-menu-item to="/userview/impact">Impact Analysis</md-menu-item>
          <md-menu-item to="/userview/adversary">Adversary Analysis</md-menu-item>
          <md-menu-item to="/userview/attack">Attack Analysis</md-menu-item>
          <md-menu-item to="/userview/asset">Asset Analysis</md-menu-item>
          <md-menu-item to="/userview/discovery">Discovery Method Analysis</md-menu-item>
          <md-menu-item to="/Overview">Back to Overview</md-menu-item>
        </md-menu-content>
        </md-menu>
      </div>
    </div>
  </div>
</template>

<script>
import PieChart from '../../components/Charts/PieChart'
import BarChart from '../../components/Charts/BarChart'
import DoughnutChart from '../../components/Charts/DoughnutChart'
import PolarAreaChart from '../../components/Charts/PolarAreaChart'
// import RadarChart from '../../components/Charts/RadarChart'
import Sidebox from '../../components/Sidebox'
import { shinebaseurl } from '@/config/variables.js'
export default {

  components: {
    PieChart,
    BarChart,
    DoughnutChart,
    PolarAreaChart,
    // RadarChart,
    Sidebox
  },
  data () {
    return {
      sector: null,
      SectorOptions: null,
      loaded: false,
      monthlylossesData: null,
      monthlylossesOption: null,
      shareoflossData: null,
      shareoflossOption: null,
      mothlynumberData: null,
      mothlynumberOption: null,
      shareoftypeData: null,
      shareoftypeOption: null,
      shareofassetData: null,
      shareofassetOption: null,
      shareofsystemData: null,
      shareofsystemOption: null,
      defaultsector: null,
      organizationid: null,
      UserID: null,
      averageoflossData: null,
      averageoflossOpinion: null
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
    // console.log(this.organizationid)
    this.fillmonthlylossesData(this.organizationid)
    await this.fillshareoflossData(this.organizationid)
    this.fillmothlynumberData(this.organizationid)
    await this.fillshareoftypeData(this.organizationid)
    this.fillshareofassetData(this.organizationid)
    this.fillshareofsystemData(this.organizationid)
    this.fillaverageoflossData(this.organizationid)
  },
  methods: {
    onItemClick (e, i) {
      // console.log('onItemClick')
    },
    onCollapse (c) {
      // console.log('onCollapse')
      this.collapsed = c
    },
    fillaverageoflossData (event) {
      let lossdata = this.shareoflossData.datasets[0].data
      let attackdata = this.shareoftypeData.datasets[0].data
      let data = []
      let labels = this.shareoflossData.labels
      for (var i = 0; i < lossdata.length; i++) {
        if (attackdata[i] === 0) {
          data[i] = 0
        } else {
          data[i] = lossdata[i] / attackdata[i]
        }
      }
      this.averageoflossOpinion = {
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
    },
    fillmonthlylossesData (event) {
      let url = `${shinebaseurl}/attackinfo/api/MonthlyLossSum/org/` + event
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          let results = res.data
          // console.log(results)
          let labels = results.map(a => a.attack_id__start_time_stamp__month)
          let data = results.map(a => a.total_loss)
          this.monthlylossesOption = {
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
          this.monthlylossesData = {
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
    async fillshareoflossData (event) {
      await this.$axios.get(`${shinebaseurl}/attackinfo/api/AttackTypeLossSum/org/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.incident_category__incident_category)
          let data = results.map(a => a.total_loss)
          this.shareoflossOption = {
            legend: {
              display: true
            },
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
    fillmothlynumberData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/MonthlyIncidentCateList/org/` + event)
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
          this.mothlynumberOption = {
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
          this.mothlynumberData = {
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
    },
    async fillshareoftypeData (event) {
      await this.$axios.get(`${shinebaseurl}/attackinfo/api/overviewIncidentCate/org/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.incident_category__incident_category)
          let data = results.map(a => a.total)
          this.shareoftypeOption = {
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.shareoftypeData = {
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
    fillshareofassetData (event) {
      let url = `${shinebaseurl}/attackinfo/api/YearlyTopAssetType/org/` + event
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          let results = res.data
          // console.log(results)
          let labels = results.map(a => a.asset_type__asset_type).slice(0, 5)
          let data = results.map(a => a.total).slice(0, 5)
          this.shareofassetOption = {
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
                  labelString: 'Top Asset Type'
                }
              }]
            },
            legend: {
              display: false
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.shareofassetData = {
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
    fillshareofsystemData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/YearlyTopSystemType/org/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.system_type__system_type).slice(0, 5)
          labels = this.shortenLabel(labels)
          let data = results.map(a => a.total).slice(0, 5)
          this.shareofsystemOption = {
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
                  labelString: 'Top System Type'
                }
              }]
            },
            legend: {
              display: false
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.shareofsystemData = {
            labels: labels,
            datasets: [
              {
                backgroundColor: ['#bfcba8', '#864000', '#f3f4ed', '#f8f4e1', '#f39189', '#f0e4d7', '#4a3933'],
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    shortenLabel (labelList) {
      var newlabellist = []
      for (var j = 0; j < labelList.length; j++) {
        let short = labelList[j].substring(0, 30)
        newlabellist[j] = short
      }
      return newlabellist
    }
  }
}
</script>

<style>
</style>
