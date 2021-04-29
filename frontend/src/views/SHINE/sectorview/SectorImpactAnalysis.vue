<template>
  <div class="content midover">
    <sidebox/>
    <div class="md-layout">
      <div class="md-layout-item  md-size-90">
        <alert>
          <h4 >Sector Incident Impact Analsis</h4>
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
              <div class="md-subheading">Impact Rating</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="impactratingData" :options="impactratingOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item  cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Loss Duration</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="lossdurationData" :options="lossdurationOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item  midcardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Security Compromise</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="securitycompromiseData" :options="securitycompromiseOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item  cardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Loss Property</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="losspropertyData" :options="losspropertyOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item midcardsize viewb">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Incident Effect</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="incidenteffectData" :options="incidenteffectOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item cardsize viewb">
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
// import PolarAreaChart from '../../../components/Charts/PolarAreaChart'
import Sidebox from '../../../components/Sidebox'
import { shinebaseurl } from '@/config/variables.js'
export default {

  components: {
    BarChart,
    // PolarAreaChart,
    Sidebox
  },
  data () {
    return {
      sector: null,
      SectorOptions: null,
      loaded: false,
      impactratingData: null,
      impactratingOption: null,
      incidenteffectData: null,
      incidenteffectOption: null,
      securitycompromiseData: null,
      securitycompromiseOption: null,
      losspropertyData: null,
      losspropertyOption: null,
      lossdurationData: null,
      lossdurationOption: null,
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
    this.fillimpactratingData(this.defaultsector)
    this.fillincidenteffectData(this.defaultsector)
    this.fillsecuritycompromiseData(this.defaultsector)
    this.filllosspropertyData(this.defaultsector)
    this.filllossdurationData(this.defaultsector)
  },
  methods: {
    changeFillData (event) {
      this.fillimpactratingData(event)
      this.fillincidenteffectData(event)
      this.fillsecuritycompromiseData(event)
      this.filllosspropertyData(event)
      this.filllossdurationData(event)
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
    fillimpactratingData (event) {
      let url = `${shinebaseurl}/attackinfo/api/MonthlyImpactRating/sector/` + event
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          let results = res.data
          // console.log(results)
          let resno = []
          let resmi = []
          let resma = []
          let resmo = []
          let resun = []
          var noi = 0
          var mii = 0
          var mai = 0
          var moi = 0
          var uni = 0
          for (var i = 0; i < results.length; i++) {
            switch (results[i].impact_rating__impact_rating) {
              case 'None':
                resno[noi] = results[i]
                noi++
                break
              case 'Minor':
                resmi[mii] = results[i]
                mii++
                break
              case 'Major':
                resma[mai] = results[i]
                mai++
                break
              case 'Moderate':
                resmo[moi] = results[i]
                moi++
                break
              case 'Unknown':
                resun[uni] = results[i]
                uni++
                break
            }
          }
          // console.log('resno')
          // console.log(resno)
          // console.log('resmi')
          // console.log(resmi)
          // console.log('resma')
          // console.log(resma)
          let labels = Array.from(new Set(results.map(a => a.attack_id__start_time_stamp__month)))
          let labelsno = Array.from(new Set(resno.map(a => a.attack_id__start_time_stamp__month)))
          let labelsmi = Array.from(new Set(resmi.map(a => a.attack_id__start_time_stamp__month)))
          let labelsma = Array.from(new Set(resma.map(a => a.attack_id__start_time_stamp__month)))
          let labelsmo = Array.from(new Set(resmo.map(a => a.attack_id__start_time_stamp__month)))
          let labelsun = Array.from(new Set(resun.map(a => a.attack_id__start_time_stamp__month)))
          let datano = resno.map(a => a.total)
          let datami = resmi.map(a => a.total)
          let datama = resma.map(a => a.total)
          let datamo = resmo.map(a => a.total)
          let dataun = resun.map(a => a.total)
          // console.log('labels')
          // console.log(labels)
          // console.log('labelsno')
          // console.log(labelsno)
          // console.log('labelsmi')
          // console.log(labelsmi)
          // console.log('labelsma')
          // console.log(labelsma)
          for (var j = 0; j < labels.length; j++) {
            if (labelsno[j] !== labels[j]) {
              datano.splice(j, 0, 0)
              labelsno.splice(j, 0, 0)
            }
            if (labelsmi[j] !== labels[j]) {
              datami.splice(j, 0, 0)
              labelsmi.splice(j, 0, 0)
            }
            if (labelsma[j] !== labels[j]) {
              datama.splice(j, 0, 0)
              labelsma.splice(j, 0, 0)
            }
            if (labelsmo[j] !== labels[j]) {
              datamo.splice(j, 0, 0)
              labelsmo.splice(j, 0, 0)
            }
            if (labelsun[j] !== labels[j]) {
              dataun.splice(j, 0, 0)
              labelsun.splice(j, 0, 0)
            }
          }
          // console.log(labels)
          // console.log(datano)
          this.impactratingOption = {
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: true
                },
                stacked: true,
                gridLines: {
                  display: false
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Numbers'
                }
              }],
              xAxes: [ {
                ticks: {
                  beginAtZero: true
                },
                stacked: true,
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
          this.impactratingData = {
            labels: labels,
            datasets: [
              {
                label: 'Unknown',
                backgroundColor: '#d8e3e7',
                data: datami
              },
              {
                label: 'None',
                backgroundColor: '#51c4d3',
                data: datano
              },
              {
                label: 'Minor',
                backgroundColor: '#d5ecc2',
                data: datami
              },
              {
                label: 'Moderate',
                backgroundColor: '#ffc2b4',
                data: datami
              },
              {
                label: 'Major',
                backgroundColor: '#ff8882',
                data: datama
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    fillincidenteffectData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/YearlyIncidentEffectTimes/sector/` + event)
        .then((res) => {
          let results = res.data
          // console.log(results)
          let labels = results.map(a => a.incident_effect__incident_effect)
          let data = results.map(a => a.total)
          this.incidenteffectOption = {
            legend: {
              display: false
            },
            responsive: true,
            maintainAspectRatio: false
          }
          labels = this.shortenLabel(labels)
          this.incidenteffectData = {
            labels: labels,
            datasets: [
              {
                backgroundColor: '#F7AA97',
                data: data
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    fillsecuritycompromiseData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/MonthlySecurityCompromise/sector/` + event)
        .then((res) => {
          let results = res.data
          // console.log(results)
          let resno = []
          let resmi = []
          let resma = []
          var noi = 0
          var mii = 0
          var mai = 0
          let resun = []
          var uni = 0
          for (var i = 0; i < results.length; i++) {
            switch (results[i].security_compromise__security_compromise) {
              case 'Suspected':
                resno[noi] = results[i]
                noi++
                break
              case 'Yes':
                resmi[mii] = results[i]
                mii++
                break
              case 'No':
                resma[mai] = results[i]
                mai++
                break
              case 'Unknown':
                resun[uni] = results[i]
                uni++
                break
            }
          }
          // console.log('resno')
          // console.log(resno)
          // console.log('resmi')
          // console.log(resmi)
          // console.log('resma')
          // console.log(resma)
          let labels = Array.from(new Set(results.map(a => a.attack_id__start_time_stamp__month)))
          let labelsno = Array.from(new Set(resno.map(a => a.attack_id__start_time_stamp__month)))
          let labelsmi = Array.from(new Set(resmi.map(a => a.attack_id__start_time_stamp__month)))
          let labelsma = Array.from(new Set(resma.map(a => a.attack_id__start_time_stamp__month)))
          let labelsun = Array.from(new Set(resun.map(a => a.attack_id__start_time_stamp__month)))
          let datano = resno.map(a => a.total)
          let datami = resmi.map(a => a.total)
          let datama = resma.map(a => a.total)
          let dataun = resun.map(a => a.total)
          // console.log('labels')
          // console.log(labels)
          // console.log('labelsno')
          // console.log(labelsno)
          // console.log('labelsmi')
          // console.log(labelsmi)
          // console.log('labelsma')
          // console.log(labelsma)
          for (var j = 0; j < labels.length; j++) {
            if (labelsno[j] !== labels[j]) {
              datano.splice(j, 0, 0)
              labelsno.splice(j, 0, 0)
            }
            if (labelsmi[j] !== labels[j]) {
              datami.splice(j, 0, 0)
              labelsmi.splice(j, 0, 0)
            }
            if (labelsma[j] !== labels[j]) {
              datama.splice(j, 0, 0)
              labelsma.splice(j, 0, 0)
            }
            if (labelsun[j] !== labels[j]) {
              dataun.splice(j, 0, 0)
              labelsun.splice(j, 0, 0)
            }
          }
          // console.log(datano)
          // console.log(datami)
          this.securitycompromiseOption = {
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
            legend: {
              display: true
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.securitycompromiseData = {
            labels: labels,
            datasets: [
              {
                label: 'Unknown',
                backgroundColor: '#d8e3e7',
                data: dataun
              },
              {
                label: 'No',
                backgroundColor: '#51c4d3',
                data: datama
              },
              {
                label: 'Suspected',
                backgroundColor: '#ffd3b4',
                data: datano
              },
              {
                label: 'Yes',
                backgroundColor: '#ffaaa7',
                data: datami
              }
            ]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    filllosspropertyData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/YearlyTopLossProperty/sector/` + event)
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
          let labels = Array.from(new Set(results.map(a => a.loss_property__loss_property)))
          let labels1 = Array.from(new Set(res1.map(a => a.loss_property__loss_property)))
          let labels2 = Array.from(new Set(res2.map(a => a.loss_property__loss_property)))
          let labels3 = Array.from(new Set(res3.map(a => a.loss_property__loss_property)))
          let labels4 = Array.from(new Set(res4.map(a => a.loss_property__loss_property)))
          let labels5 = Array.from(new Set(res5.map(a => a.loss_property__loss_property)))
          let labels6 = Array.from(new Set(res6.map(a => a.loss_property__loss_property)))
          let labels7 = Array.from(new Set(res7.map(a => a.loss_property__loss_property)))
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
          this.losspropertyOption = {
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
                  labelString: 'Loss Property'
                },
                stacked: true
              }]
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.losspropertyData = {
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
    filllossdurationData (event) {
      this.$axios.get(`${shinebaseurl}/attackinfo/api/YearlyLossDuration/sector/` + event)
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
          let labels = Array.from(new Set(results.map(a => a.loss_duration__loss_duration)))
          let labels1 = Array.from(new Set(res1.map(a => a.loss_duration__loss_duration)))
          let labels2 = Array.from(new Set(res2.map(a => a.loss_duration__loss_duration)))
          let labels3 = Array.from(new Set(res3.map(a => a.loss_duration__loss_duration)))
          let labels4 = Array.from(new Set(res4.map(a => a.loss_duration__loss_duration)))
          let labels5 = Array.from(new Set(res5.map(a => a.loss_duration__loss_duration)))
          let labels6 = Array.from(new Set(res6.map(a => a.loss_duration__loss_duration)))
          let labels7 = Array.from(new Set(res7.map(a => a.loss_duration__loss_duration)))
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
          this.lossdurationOption = {
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
                  labelString: 'Loss Duration'
                },
                stacked: true
              }]
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.lossdurationData = {
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
