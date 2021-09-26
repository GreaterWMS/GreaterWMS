<template>
  <div>
    <q-card>
      <q-card-section class="text-h6">
        Boxplot Chart
      </q-card-section>
      <q-card-section>
        <div ref="boxplotchart" id="boxplotchart" style="height: 100%"></div>
      </q-card-section>
      <q-resize-observer @resize="onResize"/>
    </q-card>
  </div>
</template>

<script>
export default {
  name: 'BoxplotChart',
  data () {
    return {
      model: false,
      options: {
        title: [
          {
            text: 'Upper: Q3 + 1.5 * IQR \nlower: Q1 - 1.5 * IQR',
            borderColor: '#999',
            // borderWidth: 1,
            textStyle: {
              fontWeight: 'normal',
              fontSize: 14,
              lineHeight: 20
            },
            left: '10%',
            top: '90%'
          }
        ],
        dataset: [{
          source: [
            [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
            [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
            [880, 880, 880, 860, 720, 720, 620, 860, 970, 950, 880, 910, 850, 870, 840, 840, 850, 840, 840, 840],
            [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
            [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
          ]
        }, {
          transform: {
            type: 'boxplot',
            config: { itemNameFormatter: 'expr {value}' }
          }
        }, {
          fromDatasetIndex: 1,
          fromTransformResult: 1
        }],
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '10%',
          right: '10%',
          bottom: '20%',
          top: '5%'
        },
        xAxis: {
          type: 'category',
          boundaryGap: true,
          nameGap: 30,
          splitArea: {
            show: false
          },
          splitLine: {
            show: false
          }
        },
        yAxis: {
          type: 'value',
          name: 'km/s minus 299,000',
          splitArea: {
            show: true
          }
        },
        series: [
          {
            name: 'boxplot',
            type: 'boxplot',
            datasetIndex: 1
          },
          {
            name: 'outlier',
            type: 'scatter',
            datasetIndex: 2
          }
        ]
      },
      boxplot_chart: null
    }
  },
  mounted () {
    this.init()
  },
  watch: {
    '$q.dark.isActive': function () {
      this.init()
    }
  },
  methods: {
    init () {
      const boxplotChart = document.getElementById('boxplotChart')
      echarts.dispose(boxplotChart)
      const theme = this.model ? 'dark' : 'light'
      this.boxplot_chart = echarts.init(boxplotChart, theme)
      this.boxplot_chart.setOption(this.options)
    },
    onResize () {
      if (this.boxplot_chart) {
        this.boxplot_chart.resize()
      }
    }
  }
}
</script>

<style scoped>

</style>
