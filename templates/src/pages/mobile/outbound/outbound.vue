<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="dn" :label="$t('outbound.dn')" icon="img:statics/outbound/dnlist.png" :to="{ name: 'mp_dn' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="shippedstock" :label="$t('outbound.shippedstock')" icon="img:statics/outbound/outbound.png" :to="{ name: 'mp_shippedstock' }" exact/>
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
  name: 'Pageoutbound',
  data () {
    return {
      detaillink: 'dn'
    }
  },
  methods: {
  }
}
</script>
