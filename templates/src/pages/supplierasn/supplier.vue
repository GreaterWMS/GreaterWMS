<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="supplierasnlist" :label="$t('inbound.asn')" icon="img:statics/inbound/asn.png" :to="{ name: 'supplierasnlist' }"to="/supplierasn/supplierasnlist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="supplierasnfinish" :label="$t('inbound.asnfinish')" icon="img:statics/inbound/asnfinish.png" :to="{ name: 'supplierasnfinish' }" exact/>
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
  name: 'Pagesupplierasn',
  data () {
    return {
      detaillink: 'supplierasnlist'
    }
  },
  methods: {
  }
}
</script>
