<template>
  <q-page class="q-pa-md bg-grey-2 ">
    <q-card class="bg-white q-ml-sm shadow-11">
  <q-card-section>
    <div class="text-h6 text-grey-8 text-weight-bolder">
      Bar Chart
      <q-select outlined v-model="selected_product"
                class="bg-white float-right q-mb-sm " style="width:300px;"
                :options="product_options" label="Select Product"/>
    </div>
  </q-card-section>
  <q-card-section class="q-pa-none map_height">
    <IEcharts :option="getBarChartOptions" :resizable="true" style="width: 100%; height: 600px"/>
  </q-card-section>
</q-card>
  </q-page>
</template>

<script>
import IEcharts from 'vue-echarts-v3/src/full.js'

export default {
  name: 'charts',
  data () {
    return {
      selected_product: 'Matcha Latte',
      data: [
        { product: 'Matcha Latte', 2015: 43.3, 2016: 85.8, 2017: 93.7 },
        { product: 'Milk Tea', 2015: 83.1, 2016: 73.4, 2017: 55.1 },
        { product: 'Cheese Cocoa', 2015: 86.4, 2016: 65.2, 2017: 82.5 },
        { product: 'Walnut Brownie', 2015: 72.4, 2016: 53.9, 2017: 39.1 }
      ],
      product_options: ['Matcha Latte', 'Milk Tea', 'Cheese Cocoa', 'Walnut Brownie']
    }
  },
  computed: {
    getBarChartOptions () {
      var _this = this

      // eslint-disable-next-line camelcase
      var filtered_data = _this.data.filter(function (item) {
        return item.product === _this.selected_product
      })

      let buisness
      return {

        grid: {
          bottom: '25%'
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
            show: false
          }
        },
        series: [
          { type: 'bar' },
          { type: 'bar' },
          { type: 'bar' }
        ]
      }
    }
  },
  components: {
    IEcharts
  }
}
</script>
