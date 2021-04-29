<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  name: 'LineChart',
  props: [ 'url' ],
  mounted: async function () {
    try {
      let response = await fetch(this.url)
      let parsedResponse = await response.json()
      // title: title of the chart, x/ylabelstring x/y title, labels: label of data like[jan, feb,...], datasetlabel:name of dataset, data: value of dataset
      let title
      let xlabelString
      let ylabelString
      let labels
      let datasetlabel1
      let data1
      let datasetlabel2
      let data2
      try {
        title = parsedResponse.lineChart.map(item => item.title)
        xlabelString = parsedResponse.lineChart.map(item => item.xlabelString)
        ylabelString = parsedResponse.lineChart.map(item => item.ylabelString)
        labels = parsedResponse.lineChart.map(item => item.labels)
        datasetlabel1 = parsedResponse.lineChart.map(item => item.datasetlabel1)
        data1 = parsedResponse.lineChart.map(item => item.data1)
        datasetlabel2 = parsedResponse.lineChart.map(item => item.datasetlabel2)
        data2 = parsedResponse.lineChart.map(item => item.data2)
      } catch (e) {
        // todo catch
        title = parsedResponse.lineChart.map(item => item.title)
        xlabelString = parsedResponse.lineChart.map(item => item.xlabelString)
        ylabelString = parsedResponse.lineChart.map(item => item.ylabelString)
        labels = parsedResponse.lineChart.map(item => item.labels)
        datasetlabel1 = parsedResponse.lineChart.map(item => item.datasetlabel1)
        data1 = parsedResponse.lineChart.map(item => item.data1)
        datasetlabel2 = parsedResponse.lineChart.map(item => item.datasetlabel2)
        data2 = parsedResponse.lineChart.map(item => item.data2)
      }
      setTimeout(() => {
        this.renderChart(
          {
            labels: labels,
            datasets: [
              {
                backgroundColor: 'transparent',
                borderColor: 'rgba(1, 116, 188, 0.50)',
                pointBackgroundColor: 'rgba(1, 71, 188, 1)',
                label: datasetlabel1,
                data: data1
              },
              {
                backgroundColor: 'transparent',
                borderColor: 'rgba(116, 6, 188, 0.50)',
                pointBackgroundColor: 'rgba(171, 71, 188, 1)',
                label: datasetlabel2,
                data: data2
              }
            ]
          },
          {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              xAxes: [{
                scaleLabel: {
                  display: true,
                  labelString: xlabelString
                }
              }],
              yAxes: [{
                scaleLabel: {
                  display: true,
                  labelString: ylabelString
                },
                ticks: {
                  beginAtZero: true
                }
              }]
            },
            title: {
              display: true,
              text: title
            }
          }
        )
      }, 300)
    } catch (e) {
      this.$emit('unavailable')
    }
  }
}
</script>
