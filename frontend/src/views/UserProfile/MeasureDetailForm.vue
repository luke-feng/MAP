<template lang="html">
  <div id="msform">
  <el-form ref="form" :model="form" >
    <div class="list">
      <md-list :md-expand-single=true>
        <md-list-item>
          <div class='md-layout-item md-small-size-100 md-size-50'>
            <label>Attack Type: </label>
            <el-select v-model="IncidentCategory" filterable placeholder="Attack Type">
              <el-option v-for="item in IncidentCategoryOptions" :key="item.incident_category_id" :label="item.incident_category" :value="item.incident_category_id">
                {{item.incident_category}}
              </el-option>
            </el-select>
          </div>
          <div class='md-layout-item md-small-size-100 md-size-50'>
            <label>Measure Type: </label>
            <el-select v-model="MeasureTypeID" clearable placeholder="Measure Type" filterable>
              <el-option v-for="item in MeasureTypeOptions" :label="item.measure_name" :key="item.measure_type_id" :value="item.measure_type_id">
                {{item.measure_name}}
              </el-option>
            </el-select>
          </div>
         </md-list-item>
        <md-list-item>
            <md-field>
              <label>Measure Description</label>
                <md-textarea v-model="MeasureDescription" md-autogrow></md-textarea>
            </md-field>
        </md-list-item>
        <md-list-item>
            <md-field>
              <label>Measure Active Years</label>
                <md-textarea v-model="TimePeriod" md-autogrow></md-textarea>
            </md-field>
            <md-field>
              <label>Vulnerability Without Measure</label>
              <md-input v-model='VulnerabilityWithoutMeasure' type='text'></md-input>
            </md-field>
            <md-field>
              <label>Discount Rate</label>
              <md-input v-model='DiscountRate' type='text'></md-input>
            </md-field>
        </md-list-item>
        <md-list-item>
            <md-field>
              <label>Initial Cost</label>
                <md-textarea v-model="InitialCost" md-autogrow></md-textarea>
            </md-field>
            <md-field>
              <label>Annual Upgrade Cost</label>
              <md-input v-model='AnnualUpgrade' type='text'></md-input>
            </md-field>
            <md-field>
              <label>Annual Maintenance Cost</label>
              <md-input v-model='AnnualMaintenance' type='text'></md-input>
            </md-field>
        </md-list-item>
        <md-list-item>
            <md-field>
              <label>Reduced Vulnerability</label>
                <md-textarea v-model="ReducedVulnerability" md-autogrow></md-textarea>
            </md-field>
            <md-field>
              <label>Reduced L1 Rate</label>
              <md-input v-model='ReducedL1Rate' type='text'></md-input>
            </md-field>
            <md-field>
              <label>Reduced L2 Rate</label>
              <md-input v-model='ReducedL2Rate' type='text'></md-input>
            </md-field>
        </md-list-item>
        <div class="share-btn-wrapper" style='text-align:center;'>
        <md-button class="md-primary" @click="close">
          Close
        </md-button>
      </div>
    </md-list>
  </div>
  </el-form>
</div>
</template>

<script>
import { shinebaseurl } from '@/config/variables.js'

export default {
  name: 'Measure Detail',
  props: ['measure'],
  data () {
    return {
      OrganizationID: null,
      UserID: null,
      MeasureTypeID: null,
      MeasureDescription: null,
      TimePeriod: null,
      InitialCost: null,
      AnnualUpgrade: null,
      AnnualMaintenance: null,
      ReducedVulnerability: null,
      ReducedL1Rate: null,
      ReducedL2Rate: null,
      IncidentCategory: null,
      MeasureTypeOptions: null,
      IncidentCategoryOptions: null,
      VulnerabilityWithoutMeasure: 0.1,
      DiscountRate: 0.05,
      showSuccess: false
    }
  },
  computed: {
    isDefined: function () {
      return this.MeasureTypeID && this.TimePeriod
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
    this.OrganizationID = info1.organizationid
    this.getMeasureTypeOptions()
    this.getIncidentCategoryOptions()
    this.OrganizationID = this.measure.organization_id
    this.UserID = this.measure.user_id
    this.MeasureTypeID = this.measure.measure_type_id
    this.MeasureDescription = this.measure.measure_description
    this.TimePeriod = this.measure.time_period
    this.InitialCost = this.measure.initial_cost
    this.AnnualUpgrade = this.measure.annual_upgrade
    this.AnnualMaintenance = this.measure.annual_maintenance
    this.ReducedVulnerability = this.measure.reduced_vulnerability
    this.ReducedL1Rate = this.measure.reduced_l1_rate
    this.ReducedL2Rate = this.measure.reduced_l2_rate
    this.IncidentCategory = this.measure.incident_category
    this.VulnerabilityWithoutMeasure = this.measure.vulnerability_without_measure
    this.DiscountRate = this.measure.discount_rate
  },
  methods: {
    close () {
      this.$emit('stateChanged')
    },
    async getMeasureTypeOptions () {
      await this.$axios.get(`${shinebaseurl}/measuretype/api/MeasuretypeList/`)
        .then((res) => {
          this.MeasureTypeOptions = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    async getIncidentCategoryOptions () {
      await this.$axios.get(`${shinebaseurl}/info_share/api/IncidentcategoryList/`)
        .then((res) => {
          this.IncidentCategoryOptions = res.data
        }).catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>

<style lang="css">
#msform {
    width: 100%;
    margin: auto;
    padding-left: 1%;
    padding-right: 1%;
  }
</style>
