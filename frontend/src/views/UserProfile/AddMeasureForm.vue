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
            <el-select v-model="MeasureTypeID" @change="getDefaultreduce($event)" clearable placeholder="Measure Type" filterable>
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
        <md-button class="md-raised md-primary" @click="saveMeasure" :disabled="!isDefined">
          Save
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
  name: 'AddMeasure',
  // props: ['dataset', 'showFileShare'],
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
    await this.getMeasureTypeOptions()
    await this.getIncidentCategoryOptions()
  },
  methods: {
    async getDefaultreduce (event) {
      await this.$axios.get(`${shinebaseurl}/measuretype/api/MeasuretypeList/`)
        .then((res) => {
          this.MeasureTypeOptions = res.data
          for (var i = 0; i < this.MeasureTypeOptions.length; i++) {
            if (this.MeasureTypeOptions[i].measure_type_id === event) {
              this.ReducedVulnerability = this.MeasureTypeOptions[i].reduced_vulnerability_defult
              this.ReducedL1Rate = this.MeasureTypeOptions[i].reduced_l1_rate_default
              this.ReducedL2Rate = this.MeasureTypeOptions[i].reduced_l2_rate_default
            }
          }
        }).catch(function (error) {
          console.log(error)
        })
    },
    saveMeasure () {
      let data = {
        organization_id: this.OrganizationID,
        user_id: this.UserID,
        incident_category: this.IncidentCategory,
        measure_type_id: this.MeasureTypeID,
        measure_description: this.MeasureDescription,
        time_period: this.TimePeriod,
        initial_cost: this.InitialCost,
        annual_upgrade: this.AnnualUpgrade,
        annual_maintenance: this.AnnualMaintenance,
        reduced_vulnerability: this.ReducedVulnerability,
        reduced_l1_rate: this.ReducedL1Rate,
        reduced_l2_rate: this.ReducedL2Rate,
        vulnerability_without_measure: this.VulnerabilityWithoutMeasure,
        discount_rate: this.DiscountRate
      }
      this.$axios({
        method: 'post',
        url: `${shinebaseurl}/measures/api/MeasureRecordCreate/`,
        data: this.$qs.stringify(data) }
      )
        .then((res) => {
        })
        .catch(function (error) {
          console.log(error)
        })
      this.$message({
        message: 'Save Measure Success.',
        type: 'success'
      })
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
