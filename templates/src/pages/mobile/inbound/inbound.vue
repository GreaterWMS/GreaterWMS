<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="asn" :label="$t('inbound.asn')" icon="img:statics/inbound/asn.png" :to="{ name: 'mp_asn' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="asnfinish" :label="$t('inbound.asnfinish')" icon="img:statics/inbound/asnfinish.png" :to="{ name: 'mp_asnfinish' }" exact/>
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
  name: 'Pageinbound',
  data () {
    return {
      detaillink: 'asn'
    }
  },
  methods: {
  }
}
</script>
