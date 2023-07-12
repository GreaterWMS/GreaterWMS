<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="warehouselist" :label="$t('menuItem.cloudwarehouse')" icon="warehouse" :to="{ name: 'warehouselist' }" exact/>
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
  name: 'Pagecloudwarehouse',
  data () {
    return {
      detaillink: 'warehouselist'
    }
  },
  methods: {
  }
}
</script>
