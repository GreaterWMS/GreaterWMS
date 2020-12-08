<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="stocklist" label="Stock List" icon="img:statics/stock/stocklist.png" to="/stock/stocklist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="stockbinlist" label="Bin Stock" icon="img:statics/warehouse/binset.png" to="/stock/stockbinlist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="emptybin" label="Empty Bin" icon="img:statics/stock/cyclecount.png" to="/stock/emptybin" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="occupiedbin" label="Occupied Bin" icon="img:statics/stock/cyclecount.png" to="/stock/occupiedbin" exact/>
        </transition>
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
