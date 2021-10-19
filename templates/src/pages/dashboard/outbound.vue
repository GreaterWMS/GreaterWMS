<template>
  <q-card class="shadow-11" :style={height:height}>
    <q-card-section>
      <div class="text-h6 text-grey-8 text-weight-bolder">
        {{selected_product + $t('index.chart')}}
        <q-select outlined v-model="selected_product"
                  class="bg-white float-right q-mb-sm " style="width:300px;"
                  :options="product_options" label="Select Product" @select="getList()"/>
      </div>
    </q-card-section>
    <q-card-section>
      <IEcharts :option="barChartOption" :resizable="true" :style="{height:height2, width: width}"/>
    </q-card-section>
  </q-card>
</template>

<script>
import IEcharts from 'vue-echarts-v3/src/full.js'
import { getauth } from 'boot/axios_request'

export default {
  name: 'charts',
  data () {
    return {
      height: '',
      height2: '',
      width: '100%',
      barChartOption: {
        grid: {
          bottom: '25%'
        },
        legend: {},
        tooltip: {},
        dataset: {
          dimensions: ['product', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
          source: [
            { product: '2015', 2015: 43.3, 2016: 85.8, 2017: 93.7, 2018: 85.8, 2019: 85.8, 2020: 85.8, 2021: 85.8, 2022: 85.8, 2023: 85.8, 2024: 85.8 }
          ]
        },
        xAxis: {
          type: 'category',
          axisLabel: {
            rotate: 45
          }
        },
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
            barWidth: '6%',
            barGap: '60%',
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
            barWidth: '6%',
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
            barWidth: '6%',
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
            barWidth: '6%',
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
            barWidth: '6%',
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
            barWidth: '6%',
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
            barWidth: '6%',
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
            barWidth: '6%',
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
            barWidth: '6%',
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
            barWidth: '6%',
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
      },
      selected_product: this.$t('dashboards.total_sales'),
      data: [
        { product: this.$t('dashboards.total_sales'), 2015: 43.3, 2016: 85.8, 2017: 93.7, 2018: 100, 2019: 100, 2020: 100, 2021: 100, 2022: 100, 2023: 100, 2024: 100, 2025: 100 }
      ],
      product_options: [this.$t('dashboards.total_sales')]
    }
  },
  methods: {
    getList () {
      var _this = this
      getauth(_this.pathname, {
      }).then(res => {
        console.log(res)
      }).catch(err => {
        console.log(err)
      })
    }
  },
  computed: {
    getBarChartOptions () {
      var _this = this
      let buisness
      const filtered_data = _this.data.filter(function (item) {
        console.log(item.product)
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
          source: { product: '总销量', 2015: 43.3, 2016: 85.8, 2017: 93.7, 2018: 100, 2019: 100, 2020: 100, 2021: 100, 2022: 100, 2023: 100, 2024: 100, 2025: 100 }
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
    if (_this.$q.platform.is.electron) {
      _this.height2 = String(_this.$q.screen.height * 0.85) + 'px'
    } else {
      _this.height2 = _this.$q.screen.height * 0.85 + '' + 'px'
    }
  },
  components: {
    IEcharts
  }
}
</script>
