<template>
  <div>
    <q-card>
      <q-card-section class="text-h6">
        Dotted Bar Chart
      </q-card-section>
      <q-card-section>
        <div ref="dottedbarchart" id="dottedbarChart" style="height: 100%"></div>
      </q-card-section>
      <q-resize-observer @resize="onResize"/>
    </q-card>
  </div>
</template>

<script>

// Generate data
var category = []
var dottedBase = +new Date()
var lineData = []
var barData = []

for (var i = 0; i < 20; i++) {
  var date = new Date(dottedBase += 3600 * 24 * 1000)
  category.push([
    date.getFullYear(),
    date.getMonth() + 1,
    date.getDate()
  ].join('-'))
  var b = Math.random() * 200
  var d = Math.random() * 200
  barData.push(b)
  lineData.push(d + b)
}

export default {
  name: 'DottedBarChart',
  data () {
    return {
      model: false,
      options: {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['line', 'bar'],
          textStyle: {
            color: '#ccc'
          },
          bottom: 10,
          top: '2%'
        },
        xAxis: {
          data: category,
          axisLine: {
            lineStyle: {
              color: '#ccc'
            }
          }
        },
        yAxis: {
          splitLine: { show: false },
          axisLine: {
            lineStyle: {
              color: '#ccc'
            }
          }
        },
        series: [{
          name: 'line',
          type: 'line',
          smooth: true,
          showAllSymbol: true,
          symbol: 'emptyCircle',
          symbolSize: 15,
          data: lineData
        }, {
          name: 'bar',
          type: 'bar',
          barWidth: 10,
          itemStyle: {
            barBorderRadius: 5,
            color: new echarts.graphic.LinearGradient(
              0, 0, 0, 1,
              [
                { offset: 0, color: '#14c8d4' },
                { offset: 1, color: '#43eec6' }
              ]
            )
          },
          data: barData
        }, {
          name: 'line',
          type: 'bar',
          barGap: '-100%',
          barWidth: 10,
          itemStyle: {
            color: new echarts.graphic.LinearGradient(
              0, 0, 0, 1,
              [
                { offset: 0, color: 'rgba(20,200,212,0.5)' },
                { offset: 0.2, color: 'rgba(20,200,212,0.2)' },
                { offset: 1, color: 'rgba(20,200,212,0)' }
              ]
            )
          },
          z: -12,
          data: lineData
        }, {
          name: 'dotted',
          type: 'pictorialBar',
          symbol: 'rect',
          itemStyle: {
            color: '#0f375f'
          },
          symbolRepeat: true,
          symbolSize: [12, 4],
          symbolMargin: 1,
          z: -10,
          data: lineData
        }]
      },
      dottedbar_chart: null
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
      const dottedbarChart = document.getElementById('dottedbarChart')
      echarts.dispose(dottedbarChart)
      const theme = this.model ? 'dark' : 'light'
      this.dottedbar_chart = echarts.init(dottedbarChart, theme)
      this.dottedbar_chart.setOption(this.options)
    },
    onResize () {
      if (this.dottedbar_chart) {
        this.dottedbar_chart.resize()
      }
    }
  }
}
</script>

<style scoped>

</style>
