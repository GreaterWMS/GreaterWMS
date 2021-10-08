<template>
<q-card class="bg-white q-ml-sm shadow-11">
  <q-card-section>
    <div class="text-h6 text-grey-8 text-weight-bolder">
      Bar Chart
      <q-select outlined v-model="selected_product"
                class="bg-white float-right q-mb-sm " style="width:300px;"
                :options="product_options" label="Select Product"/>
    </div>
  </q-card-section>
  <q-card-section class="q-pa-none">
    <IEcharts :option="barChartOption" :resizable="true" style="height: 600px; width: 100%"/>
  </q-card-section>
</q-card>
</template>


<script>
import IEcharts from 'vue-echarts-v3/src/full.js'

export default {
  name: 'charts',
  data () {
    return {
      barChartOption: {
        grid: {
          bottom: '25%'
        },
        legend: {},
        tooltip: {},
        dataset: {
          dimensions: ['product', '2015', '2016', '2017'],
          source: [
            { product: 'Matcha Latte', 2015: 43.3, 2016: 85.8, 2017: 93.7 },
            { product: 'Milk Tea', 2015: 83.1, 2016: 73.4, 2017: 55.1 },
            { product: 'Cheese Cocoa', 2015: 86.4, 2016: 65.2, 2017: 82.5 },
            { product: 'Walnut Brownie', 2015: 72.4, 2016: 53.9, 2017: 39.1 }
          ]
        },
        xAxis: {
          type: 'category',
          axisLabel: {
            rotate: 45
          }
        },
        yAxis: {},
        // Declare several bar series, each will be mapped
        // to a column of dataset.source by default.
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
