<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="stocklist" :label="$t('stock.stocklist')" icon="img:statics/stock/stocklist.png" :to="{ name: 'stocklist' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="stockbinlist" :label="$t('stock.stockbinlist')" icon="img:statics/warehouse/binset.png" :to="{ name: 'stockbinlist' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="emptybin" :label="$t('stock.emptybin')" icon="all_out" :to="{ name: 'emptybin' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="occupiedbin" :label="$t('stock.occupiedbin')" icon="all_inbox" :to="{ name: 'occupiedbin' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="cyclecount" :label="$t('cyclecount')" icon="img:statics/stock/cyclecount.png" :to="{ name: 'cyclecount' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="cyclecountrecorder" :label="$t('cyclecountrecorder')" icon="img:statics/stock/cyclecountrecorder.png" :to="{ name: 'cyclecountrecorder' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="handcount" :label="$t('handcount.handcount')" icon="img:statics/stock/cyclecount.png" :to="{ name: 'handcount' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="handcountrecorder" :label="$t('handcount.handcountrecorder')" icon="img:statics/stock/cyclecountrecorder.png" :to="{ name: 'handcountrecorder' }" exact/>
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
