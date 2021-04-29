
<script>
import { PolarArea, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: PolarArea,
  name: 'PolarAreaChart',
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
  mounted () {
    this.renderChart(this.chartData, this.options)
    // console.log(this.chartData)
  }
  // mounted () {
  //   this.renderChart({
  //     labels: ['None', 'Insignificant', 'Minor', 'Max'],
  //     datasets: [
  //       {
  //         label: 'Sector 1',
  //         backgroundColor: 'rgba(179,181,198,0.2)',
  //         pointBackgroundColor: 'rgba(179,181,198,1)',
  //         pointBorderColor: '#fff',
  //         pointHoverBackgroundColor: '#fff',
  //         pointHoverBorderColor: 'rgba(179,181,198,1)',
  //         data: [65, 59, 90, 81]
  //       },
  //       {
  //         label: 'Sector 2',
  //         backgroundColor: 'rgba(255,99,132,0.2)',
  //         pointBackgroundColor: 'rgba(255,99,132,1)',
  //         pointBorderColor: '#fff',
  //         pointHoverBackgroundColor: '#fff',
  //         pointHoverBorderColor: 'rgba(255,99,132,1)',
  //         data: [28, 48, 40, 19]
  //       }
  //     ]
  //   },
  //   {
  //     responsive: true,
  //     maintainAspectRatio: false
  //   }
  //   )
  // }
}
</script>
