<script>
import { Radar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins
export default {
  extends: Radar,
  name: 'RadarChart',
  mixins: [reactiveProp],
  props: {
    chartData: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },
  mounted: async function () {
    this.renderChart(this.chartData, this.options)
  }
}
</script>
