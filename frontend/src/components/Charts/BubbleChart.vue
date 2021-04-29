<script>
import { Bubble } from 'vue-chartjs'

export default {
  extends: Bubble,
  name: 'BubbleChart',
  props: [ 'url' ],
  mounted: async function () {
    try {
      let response = await fetch(this.url)
      let parsedResponse = await response.json()
      // title: title of the chart, labels: label of data like[jan, feb,...], datasetlabel:name of dataset, data: value of dataset
      let title
      let labels
      let datasetlabel1
      let data1
      let datasetlabel2
      let data2
      try {
        title = parsedResponse.bubbleChart.map(item => item.title)
        labels = parsedResponse.bubbleChart.map(item => item.labels)
        datasetlabel1 = parsedResponse.bubbleChart.map(item => item.datasetlabel1)
        data1 = parsedResponse.bubbleChart.map(item => item.data1)
        datasetlabel2 = parsedResponse.bubbleChart.map(item => item.datasetlabel2)
        data2 = parsedResponse.bubbleChart.map(item => item.data2)
      } catch (e) {
        // todo catch
        console.log(e)
        title = parsedResponse.bubbleChart.map(item => item.title)
        labels = parsedResponse.bubbleChart.map(item => item.labels)
        datasetlabel1 = parsedResponse.bubbleChart.map(item => item.datasetlabel1)
        data1 = parsedResponse.bubbleChart.map(item => item.data1)
        datasetlabel2 = parsedResponse.bubbleChart.map(item => item.datasetlabel2)
        data2 = parsedResponse.bubbleChart.map(item => item.data2)
      }
      setTimeout(() => {
        this.renderChart(
          {
            labels: labels,
            datasets: [
              {
                label: datasetlabel1,
                backgroundColor: '#f87979',
                data: data1
                // data: [{x: 1,y: 30,r: 15}, {x: 4, y: 20,r: 10}]
              },
              {
                label: datasetlabel2,
                backgroundColor: '#7C8CF8',
                data: data2
              }
            ]
          },
          {
            responsive: true,
            maintainAspectRatio: false,
            title: {
              display: true,
              text: title
            }
          }
        )
      }, 300)
    } catch (e) {
      console.log(e)
      this.$emit('unavailable')
    }
  }
}
</script>
