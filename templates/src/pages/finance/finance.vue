<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="capitallist" :label="$t('finance.capital')" icon="img:statics/capital/capital.png" :to="{ name: 'capitallist' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="freight" :label="$t('finance.freight')" icon="img:statics/capital/freight.png" :to="{ name: 'freight' }" exact/>
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
  name: 'Pagecapital',
  data () {
    return {
      detaillink: 'capitallist'
    }
  },
  methods: {
  }
}
</script>
