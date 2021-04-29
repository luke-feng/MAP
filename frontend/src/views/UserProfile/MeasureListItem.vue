<template lang="html">
  <div class='mlitem md-layout'>
    <div class='md-layout-item md-size-15'>
      <label>Measure: </label>
    </div>
    <div class='md-layout-item md-size-35'>
        <el-select v-model="IncidentCategory" filterable placeholder="Attack Type">
              <el-option v-for="item in IncidentCategoryOptions" :key="item.incident_category_id" :label="item.incident_category" :value="item.incident_category_id">
                {{item.incident_category}}
              </el-option>
        </el-select>
    </div>
    <div class='md-layout-item md-size-35'>
      <el-select v-model="MeasureTypeID" clearable placeholder="Measure Type" filterable>
              <el-option v-for="item in MeasureTypeOptions" :label="item.measure_name" :key="item.measure_type_id" :value="item.measure_type_id">
                {{item.measure_name}}
              </el-option>
            </el-select>
      </div>
    <div class='md-layout-item md-size-15'>
      <el-button icon="el-icon-d-arrow-right" @click="showMoreMeasure = true"></el-button>
    </div>
    <md-dialog :md-active.sync="showMoreMeasure">
      <md-dialog-title>Measure Details</md-dialog-title>
      <measure-detail-from :measure="measure" @done="closeMoreMeasureForm" v-on:stateChanged="updateMoreMeasure">
      </measure-detail-from>
      <md-dialog-actions>
        <md-button class="md-primary" @click="showMoreMeasure = false">
          <md-icon>close</md-icon>
        </md-button>
      </md-dialog-actions>
    </md-dialog>
  </div>
</template>

<script>
import { shinebaseurl } from '@/config/variables.js'
import MeasureDetailForm from '@/views/UserProfile/MeasureDetailForm'
export default {
  components: {
    'measure-detail-from': MeasureDetailForm
  },
  props: ['measure'],
  methods: {
    updateMoreMeasure: function () {
      this.closeMoreMeasureForm()
      return this.showMoreMeasure
    },
    closeMoreMeasureForm: function () {
      this.showMoreMeasure = false
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
  },
  data: function () {
    return {
      MeasureTypeID: this.measure.measure_type_id,
      InitialCost: this.measure.initial_cost,
      IncidentCategory: this.measure.incident_category,
      MeasureTypeOptions: null,
      IncidentCategoryOptions: null,
      showMoreMeasure: false,
      showSuccess: false
    }
  },
  mounted () {
    this.MeasureTypeID = this.measure.measure_type_id
    this.InitialCost = this.measure.initial_cost
    this.IncidentCategory = this.measure.incident_category
    this.showMoreMeasure = false
    this.showSuccess = false
    this.getMeasureTypeOptions()
    this.getIncidentCategoryOptions()
  }
}
</script>

<style lang="css" scoped>
#mlitem {
  padding-bottom: 5px;
  max-width: 100%;
}
</style>
