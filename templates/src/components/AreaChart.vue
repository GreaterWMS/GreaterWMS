<template>
  <div>
    <q-card>
      <q-card-section class="text-h6">
        Stacked Area Chart
      </q-card-section>
      <q-card-section>
        <div ref="areachart" id="areaChart" style="height: 100%"></div>
      </q-card-section>
      <q-resize-observer @resize="onResize"/>
    </q-card>
  </div>
</template>

<script>
export default {
  name: 'AreaChart',
  data () {
    return {
      model: false,
      options: {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        legend: {
          data: ['Email marketing', 'Affiliate advertising', 'Video advertising', 'Direct access', 'Search engine'],
          bottom: 10
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '15%',
          top: '5%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Email marketing',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: [120, 132, 101, 134, 90, 230, 210]
          },
          {
            name: 'Affiliate Advertising',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: [220, 182, 191, 234, 290, 330, 310]
          },
          {
            name: 'Video ads',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: [150, 232, 201, 154, 190, 330, 410]
          },
          {
            name: 'Direct access',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: [320, 332, 301, 334, 390, 330, 320]
          },
          {
            name: 'Search Engine',
            type: 'line',
            stack: 'Total',
            label: {
              show: true,
              position: 'top'
            },
            areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            data: [820, 932, 901, 934, 1290, 1330, 1320]
          }
        ]
      },
      area_chart: null
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
      const areaChart = document.getElementById('areaChart')
      echarts.dispose(areaChart)
      const theme = this.model ? 'dark' : 'light'
      this.area_chart = echarts.init(areaChart, theme)
      this.area_chart.setOption(this.options)
    },
    onResize () {
      if (this.area_chart) {
        this.area_chart.resize()
      }
    }
  }
}
</script>

<style scoped>

</style>
