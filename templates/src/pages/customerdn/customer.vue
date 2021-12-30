<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="customerdnlist" :label="$t('menuItem.customerdn')" icon="img:statics/outbound/dnlist.png" :to="{ name: 'customerdnlist' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="customerpod" :label="$t('outbound.pod')" icon="img:statics/outbound/receiving.png" :to="{ name: 'customerpod' }" exact/>
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
  name: 'Pagecustomerdn',
  data () {
    return {
      detaillink: 'customerdnlist'
    }
  },
  methods: {
  }
}
</script>
