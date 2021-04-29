<template>
  <div class="content midover">
    <sidebox/>
    <div class="md-layout">
      <div class="md-layout-item  md-size-90">
        <alert>
          <h4 >Sector Incident Discovery Method Analsis</h4>
        </alert>
      <el-select v-model="sector" @change="changeFillData($event)" filterable placeholder="Business Sector">
                <el-option v-for="item in SectorOptions" :key="item.sectorid" :label="item.sector_name" :value="item.sectorid">
                  {{item.sector_name}}
                </el-option>
              </el-select>
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
            <md-button md-menu-trigger class=' md-raised toggle' to="/Sectorview">Back to Sectorview</md-button>
          </md-menu>
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
    this.filldiscoverymethodData(this.defaultsector)
  },
  methods: {
    changeFillData (event) {
      this.filldiscoverymethodData(event)
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
    filldiscoverymethodData (event) {
      let url = `${shinebaseurl}/attackinfo/api/YearlyDiscoveryMethod/sector/` + event
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          let results = res.data
          // console.log(results)
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
