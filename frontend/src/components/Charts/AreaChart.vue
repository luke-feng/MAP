
<script>
import { Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Line,
  name: 'AreaChart',
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
  data () {
  },
  mounted: async function () {
    this.renderChart(this.chartData, this.options)
  }
}
</script>
