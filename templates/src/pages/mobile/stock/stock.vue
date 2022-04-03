<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="stocklist" :label="$t('stock.stocklist')" icon="img:statics/stock/stocklist.png" :to="{ name: 'mp_stocklist' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="stockbinlist" :label="$t('stock.stockbinlist')" icon="img:statics/warehouse/binset.png" :to="{ name: 'mp_stockbinlist' }" exact/>
        </transition>
      </q-tabs>
    </div>
  </div>
</template>
    <div class="main-table">
      <router-view />
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Pagestock',
  data () {
    return {
      detaillink: 'stocklist'
    }
  },
  methods: {
  }
}
</script>
