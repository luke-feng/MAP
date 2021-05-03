<template>
  <div class="content midover">
    <sidebox/>
    <div class="md-layout">
      <div class="md-layout-item  md-size-90">
        <alert>
          <h4 >User Incident Discovery Method Analsis</h4>
        </alert>
      </div>
    </div>
    <div class="md-layout">
      <div class="md-layout-item  longcardsize viewb">
         <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-subheading">Discovery Method</div>
            </md-card-header>
            <md-card-content>
              <BarChart :chartData="discoverymethodData" :options="discoverymethodOption"/>
            </md-card-content>
          </md-ripple>
        </md-card>
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
// import LineChart from '../../../components/Charts/LineChart'
import BarChart from '../../../components/Charts/BarChart'
// import PolarAreaChart from '../../../components/Charts/PolarAreaChart'
import Sidebox from '../../../components/Sidebox'
import { shinebaseurl } from '@/config/variables.js'
export default {
  components: {
    // LineChart,
    BarChart,
    // PolarAreaChart,
    Sidebox
  },
  data () {
    return {
      sector: null,
      SectorOptions: null,
      loaded: false,
      discoverymethodData: null,
      discoverymethodOption: null,
      organizationid: null,
      UserID: null
    }
  },
  mounted: async function () {
    let userurl = `${shinebaseurl}:8080/auth/info`
    var res = await fetch(userurl, { credentials: 'include' })
    var info = await res.json()
    this.UserID = info.id
    let sectorurl = `${shinebaseurl}/userinfo/api/UserDetail/` + this.UserID
    var res1 = await fetch(sectorurl)
    var info1 = await res1.json()
    this.organizationid = info1.organizationid
    this.filldiscoverymethodData(this.organizationid)
  },
  methods: {
    onItemClick (e, i) {
      console.log('onItemClick')
    },
    onCollapse (c) {
      console.log('onCollapse')
      this.collapsed = c
    },
    filldiscoverymethodData (event) {
      let url = `${shinebaseurl}/attackinfo/api/YearlyDiscoveryMethod/org/` + event
      this.$axios.get(url)
        .then((res) => {
          let results = res.data
          let labels = results.map(a => a.discovery_method__discovery_method)
          let data = results.map(a => a.total)
          this.discoverymethodOption = {
            legend: {
              display: false
            },
            responsive: true,
            maintainAspectRatio: false
          }
          this.discoverymethodData = {
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
    }
  }
}
</script>
<style>
</style>
