<template>
  <div>
    <q-card class="shadow-24">
      <q-card-section class="text-h6">
        <q-btn icon="download" class="float-right" @click="SaveImage" flat dense>
          <q-tooltip>Download PNG</q-tooltip>
        </q-btn>
      </q-card-section>
      <q-card-section>
        <div ref="barchart" id="barChart" :style="{height: height}"></div>
      </q-card-section>
      <q-resize-observer @resize="onResize"/>
    </q-card>
  </div>
</template>

<script>
import { database } from '../db/database'

export default {
  name: 'BarChart',
  data () {
    return {
      height: '',
      model: false,
      options: {
        legend: {
          bottom: 10
        },
        tooltip: {},
        dataset: {
          source: [
            ['product', '2015', '2016', '2017', '2018'],
            ['Matcha Latte', 43.3, 85.8, 93.7, 77.6],
            ['Milk Tea', 83.1, 73.4, 55.1, 36.1],
            ['Cheese Cocoa', 86.4, 65.2, 82.5, 46.2],
            ['Walnut Brownie', 72.4, 53.9, 39.1, 53.3],
            ['Walnut Brownie', 72.4, 53.9, 39.1, 53.3],
            ['Walnut Brownie', 72.4, 53.9, 39.1, 53.3],
            ['Walnut Brownie', 72.4, 53.9, 39.1, 53.3],
            ['Walnut Brownie', 72.4, 53.9, 39.1, 53.3],
            ['Walnut Brownie', 72.4, 53.9, 39.1, 53.3]
          ]
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '20%',
          top: '5%',
          containLabel: true
        },
        xAxis: { type: 'category' },
        yAxis: {},
        // Declare several bar series, each will be mapped
        // to a column of dataset.source by default.
        series: [
          { type: 'bar' },
          { type: 'bar' },
          { type: 'bar' },
          { type: 'bar' }
        ]
      },
      bar_chart: null
    }
  },
  mounted () {
    var _this = this
    _this.barchartdata()
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height - 260) + 'px'
    } else {
      _this.height = _this.$q.screen.height - 260 + '' + 'px'
    }
  },
  watch: {
    '$q.dark.isActive': function () {
      this.init()
    }
  },
  methods: {
    barchartdata () {
      var _this = this
      var chart = database.getInstance().get().barchart
      chart.toArray().then(res => {
        console.log('0000', res, _this.options.dataset.source)
        for (var i = 0; i < res[0].xAxis.length; i++) {
          console.log(res[0].xAxis[i], i - 1)
          _this.options.dataset.source[0][i + 1] = res[0].xAxis[i]
        }
        for (var j = 0; j < 9; j++) {
          _this.options.dataset.source[j + 1][0] = res[0].dataset[j]
        }
        _this.init()
      })
    },
    SaveImage () {
      const linkSource = this.bar_chart.getDataURL()
      const downloadLink = document.createElement('a')
      document.body.appendChild(downloadLink)
      downloadLink.href = linkSource
      downloadLink.target = '_self'
      downloadLink.download = 'BarChart.png'
      downloadLink.click()
    },
    init () {
      const barChart = document.getElementById('barChart')
      echarts.dispose(barChart)
      const theme = this.model ? 'dark' : 'light'
      this.bar_chart = echarts.init(barChart, theme)
      this.bar_chart.setOption(this.options)
    },
    onResize () {
      if (this.bar_chart) {
        this.bar_chart.resize()
      }
    }
  }
}
</script>

<style scoped>

</style>
