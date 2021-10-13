<template>
  <q-card class="shadow-11" :style={height:height}>
    <q-card-section>
      <div class="text-h6 text-grey-8 text-weight-bolder">
        {{selected_product + $t('index.chart')}}
        <q-select outlined v-model="selected_product"
                  class="bg-white float-right q-mb-sm " style="width:300px;"
                  :options="product_options" label="Select Product"/>
      </div>
    </q-card-section>
    <q-card-section class="q-pa-none">
      <IEcharts :option="getBarChartOptions" :resizable="true" style="height: 600px; width: 100%"/>
    </q-card-section>
  </q-card>
</template>

<script>
import IEcharts from 'vue-echarts-v3/src/full.js'

export default {
  name: 'charts',
  data () {
    return {
      height: '',
      selected_product: this.$t('dashboards.total_receipts'),
      data: [
        { product: this.$t('dashboards.total_receipts'), 2015: 43.3, 2016: 85.8, 2017: 93.7, 2018: 100, 2019: 100, 2020: 100, 2021: 100, 2022: 100, 2023: 100, 2024: 100, 2025: 100 },
        { product: this.$t('dashboards.category_receipt_ranking'), 2015: 83.1, 2016: 73.4, 2017: 55.1, 2018: 100, 2019: 100, 2020: 100, 2021: 100, 2022: 100, 2023: 100, 2024: 100, 2025: 100 },
        { product: this.$t('dashboards.receiving_quantity_ranking'), 2015: 86.4, 2016: 65.2, 2017: 82.5, 2018: 100, 2019: 100, 2020: 100, 2021: 100, 2022: 100, 2023: 100, 2024: 100, 2025: 100 },
        { product: this.$t('dashboards.Receiving_amount_ranking'), 2015: 72.4, 2016: 53.9, 2017: 39.1, 2018: 100, 2019: 100, 2020: 100, 2021: 100, 2022: 100, 2023: 100, 2024: 100, 2025: 100 }
      ],
      product_options: [this.$t('dashboards.total_receipts'), this.$t('dashboards.receiving_quantity_ranking'), this.$t('dashboards.Receiving_amount_ranking')]
    }
  },
  methods: {
  },
  computed: {
    getBarChartOptions () {
      console.log(1)
      const _this = this
      let buisness
      const filtered_data = _this.data.filter(function (item) {
        return item.product === _this.selected_product
      })
      console.log(filtered_data)
      return {
        grid: {
          bottom: '1%'
        },
        xAxis: {
          type: 'category',
          axisLabel: {},
          nameLocation: 'middle',
          nameGap: 78
        },
        tooltip: {},
        dataset: {
          dimensions: ['product', '2015', '2016', '2017'],
          source: filtered_data
        },
        buisness,
        yAxis: {
          type: 'value',
          splitLine: {
            show: true,
            lineStyle: {
              type: [30, 20]
            }
          }
        },
        series: [
          {
            type: 'bar',
            barWidth: 80,
            barGap: '70%',
            barCategoryGap: '10%',
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'

                }
              }
            }
          },
          {
            type: 'bar',
            barWidth: 80,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'

                }
              }
            }
          },
          {
            type: 'bar',
            barWidth: 80,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'

                }
              }
            }
          },
          {
            type: 'bar',
            barWidth: 80,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'

                }
              }
            }
          },
          {
            type: 'bar',
            barWidth: 80,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'

                }
              }
            }
          },
          {
            type: 'bar',
            barWidth: 80,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'

                }
              }
            }
          },
          {
            type: 'bar',
            barWidth: 80,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'

                }
              }
            }
          },
          {
            type: 'bar',
            barWidth: 80,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'

                }
              }
            }
          },
          {
            type: 'bar',
            barWidth: 80,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'

                }
              }
            }
          },
          {
            type: 'bar',
            barWidth: 80,
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  position: 'top'

                }
              }
            }
          }
        ]
      }
    }

  },
  mounted () {
    var _this = this
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height - 200) + 'px'
    } else {
      _this.height = _this.$q.screen.height - 200 + '' + 'px'
    }
  },
  components: {
    IEcharts
  }
}
</script>
