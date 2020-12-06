<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
  <q-route-tab name="stocklist" label="Stock List" icon="img:statics/stock/stocklist.png" to="/stock/stocklist" exact/>
  <q-route-tab name="stockbinlist" label="Bin Stock" icon="img:statics/warehouse/binset.png" to="/stock/stockbinlist" exact/>
  <q-route-tab name="emptybin" label="Empty Bin" icon="img:statics/stock/cyclecount.png" to="/stock/emptybin" exact/>
  <q-route-tab name="occupiedbin" label="Occupied Bin" icon="img:statics/stock/cyclecount.png" to="/stock/occupiedbin" exact/>
      </q-tabs>
    </div>
  </div>
</template>
    <router-view />
  </q-page>
</template>

<script>
export default {
  name: 'Pagestock',
  data () {
    return {
      detaillink: 'stock'
    }
  },
  methods: {
  }
}
</script>
