<template>
  <div>
    <q-card class="shadow-24">
      <q-card-section class="text-h6">
      </q-card-section>
      <q-card-section>
        <div ref="piechart" id="pieChart" :style="{height:height}"></div>
      </q-card-section>
      <q-resize-observer @resize="onResize"/>
    </q-card>
  </div>
</template>

<script>
import { database } from 'src/db/database'

export default {
  name: 'PieChart',
  data () {
    return {
      height: '',
      model: false,
      options: {
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
          top: 'bottom',
          bottom: '5%',
          left: 'center'
        },
        series: [
          {
            name: 'Access source',
            type: 'pie',
            radius: ['40%', '70%'],
            center: ['50%', '35%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: true,
              position: 'left'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: true
            },
            data: [
              { value: 1048, name: 'Search Engine' },
              { value: 735, name: 'Direct access' },
              { value: 580, name: 'Email marketing' },
              { value: 484, name: 'Affiliate Advertising' },
              { value: 300, name: 'Video ad' }
            ]
          }
        ]
      },
      pie_chart: null
    }
  },
  mounted () {
    var _this = this
    console.log(1)
    _this.piechartdata()
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
    piechartdata () {
      var _this = this
      var chart = database.getInstance().get().piechart
      chart.toArray().then(res => {
        for (var i = 0; i < 5; i++) {
          _this.options.series[0].data[i].name = res[0].name[i]
        }
        _this.init()
      })
    },
    init () {
      const pieChart = document.getElementById('pieChart')
      echarts.dispose(pieChart)
      const theme = this.model ? 'dark' : 'light'
      this.pie_chart = echarts.init(pieChart, theme)
      this.pie_chart.setOption(this.options)
    },
    onResize () {
      if (this.pie_chart) {
        this.pie_chart.resize()
      }
    }
  }
}
</script>

<style scoped>

</style>
