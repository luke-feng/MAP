<template>
  <div class="content midover">
    <sidebox/>
    <div class="md-layout ">
      <div class="md-layout-item  tilesize">
        <alert>
          <h4 >Overview</h4>
        </alert>
      </div>
    </div>
    <div  class="md-layout">
      <div class="md-layout-item  viewbottonsize viewb" >
        <popover  content="Economic impact overview" trigger="hover" placement="bottomLeft ">
            <md-button class="md-raised md-primary">Economic View</md-button>
        </popover>
      </div>
      <div class="md-layout-item md-size-30 viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Monthly Losses Cuased by Cyberattack</div>
            </md-card-header>
            <md-card-content>
              <AreaChart :chartData="monthlylossdata" :options="monthlylossoptions"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item  md-size-30 viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Share of Losses Caused by Different Types of Cyberattacks</div>
            </md-card-header>
            <md-card-content>
              <DoughnutChart :chartData="shareoflossdata" :options="shareoflossoptions"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item morebottonsize viewm" >
        <md-menu>
        <md-button md-menu-trigger class='md-raised toggle'>More Economic Views</md-button>
        <md-menu-content>
          <md-menu-item to="/sectorview">Sector-specific Views</md-menu-item>
          <md-menu-item to="/userview">User-specific Views</md-menu-item>
        </md-menu-content>
        </md-menu>
      </div>
    </div>
    <div  class="md-layout">
      <div class="md-layout-item  viewbottonsize viewb" >
        <popover  content="Technical information overview" trigger="hover" placement="bottomLeft ">
          <md-button class="md-raised md-primary">Incident statistics</md-button>
        </popover>
      </div>
      <div class="md-layout-item md-size-30 viewb">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Monthly Numbers by Cyberattack</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="monthlyattackdata" :options="monthlyattackoptions"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item  md-size-30 viewb">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Number of Attacks in Each Incident Category</div>
            </md-card-header>
            <md-card-content>
              <PolarAreaChart :chartData="shareofattackdata" :options="shareofattackoptions"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item morebottonsize viewm" >
        <md-menu>
        <md-button md-menu-trigger class=' md-raised toggle'>More Inights Views</md-button>
        <md-menu-content>
          <md-menu-item to="/sectorview">Sector-specific Views</md-menu-item>
          <md-menu-item to="/userview">User-specific Views</md-menu-item>
        </md-menu-content>
        </md-menu>
      </div>
    </div>
  </div>
</template>

<script>

import AreaChart from '../../components/Charts/AreaChart'
import DoughnutChart from '../../components/Charts/DoughnutChart'
import BarChart from '../../components/Charts/BarChart'
import PolarAreaChart from '../../components/Charts/PolarAreaChart'
import Sidebox from '../../components/Sidebox'
import { shinebaseurl } from '@/config/variables.js'
export default {
  components: {
    AreaChart,
    DoughnutChart,
    BarChart,
    PolarAreaChart,
    Sidebox
  },
  data () {
    return {
      loaded: false,
      monthlylossdata: null,
      shareofattackdata: null,
      monthlyattackdata: null,
      shareoflossdata: null,
      shareoflossoptions: null,
      monthlyattackoptions: null,
      monthlylossoptions: null,
      shareofattackoptions: null,
      userId: null,
      allUsers: [],
      firstname: null,
      lastname: null,
      organization: null,
      sector: null,
      email: null
    }
  },
  mounted: async function () {
    this.$store.dispatch('determineAuthState')
    setInterval(() => { this.$store.dispatch('pollAnalyses') }, 10000)
    let userurl = `${shinebaseurl}:8080/auth/info`
    var res = await fetch(userurl, { credentials: 'include' })
    var info = await res.json()
    this.userId = info.id
    this.firstname = info.firstname
    this.lastname = info.lastname
    this.email = info.email
    let sectorurl = `${shinebaseurl}/userinfo/api/UserDetail/` + this.userId
    var resSect = await fetch(sectorurl)
    var infoSect = await resSect.json()
    this.organization = infoSect.organizationid
    this.sector = infoSect.sectorid
    this.findThisUser()
    this.fillshareoflossdata(this.organization)
    this.fillshareofattackdata(this.organization)
    this.fillmonthlyattackdata(this.organization)
    this.fillmonthlylossdata(this.organization)
  },
  methods: {
    async findThisUser () {
      let allUsersUrl = `${shinebaseurl}/userinfo/api/UserList/`
      await this.$axios.get(allUsersUrl)
        .then((res) => {
          this.allUsers = res.data
        })
        .catch(error => {
          console.log(error)
        })
      var found = this.allUsers.find(element => element === this.userId)
      let data = {
        userid: this.userId,
        userfirstname: this.firstname,
        userlastname: this.lastname,
        useremail: this.email
      }
      if (found !== this.userId) {
        this.$axios({
          method: 'post',
          url: `${shinebaseurl}/userinfo/api/UserCreate/`,
          data: this.$qs.stringify(data) }
        )
          .then((res) => {
            // console.log(res)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    onItemClick (e, i) {
      console.log('onItemClick')
    },
    onCollapse (c) {
      console.log('onCollapse')
      this.collapsed = c
    },
    fillshareoflossdata (event) {
      let url = `${shinebaseurl}/attackinfo/api/AttackTypeLossSum/org/` + event
      this.$axios.get(url)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.incident_category__incident_category)
          let data = results.map(a => a.total_loss)
          this.shareoflossoptions = {
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.shareoflossdata = {
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
    fillshareofattackdata (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/overviewIncidentCate/org/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.incident_category__incident_category)
          let data = results.map(a => a.total)
          this.shareofattackoptions = {
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.shareofattackdata = {
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
    fillmonthlyattackdata (event) {
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
          this.monthlyattackoptions = {
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
          this.monthlyattackdata = {
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
    fillmonthlylossdata (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/MonthlyLossSum/org/` + event)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.attack_id__start_time_stamp__month)
          let data = results.map(a => a.total_loss)
          this.monthlylossoptions = {
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
          this.monthlylossdata = {
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
    }
  }
}
</script>
<style>
.midover {
  margin-top: 20px;
  max-width: 80%;
  margin-left: 15%;
  display: flex;
  flex-direction: column;
}
.viewb {
  margin-top: 20px;
  display: flex;
  margin-right: 1%;
  flex-direction: column;
}
.viewmid {
  margin-top: 8em;
  margin-bottom: 10em;
  display: flex;
  flex-direction: column;
}
.viewm {
  margin-top:30em;
  display: flex;
  flex-direction: column;
}
.empty{
  max-width: 2%;
}
.tilesize{
  max-width: 100%;
}
.viewbottonsize{
  max-width: 12%;
  margin-right: 1%;
}
.cardsize{
  max-width: 25%;
  margin-right: 1%;
}
.midcardsize{
  max-width: 51%;
  margin-right: 1%;
}
.longcardsize{
  max-width: 77%;
  margin-right: 1%;
}
.morebottonsize{
  max-width: 15%;
}
</style>
