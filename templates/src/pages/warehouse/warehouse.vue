<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="warehouseset" :label="$t('warehouse.warehouse')" icon="img:statics/warehouse/warehouseset.png" to="/warehouse/warehouseset" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="binset" :label="$t('warehouse.binset')" icon="img:statics/warehouse/binset.png" to="/warehouse/binset" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="binsize" :label="$t('warehouse.binsize')" icon="img:statics/warehouse/binsize.png" to="/warehouse/binsize" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="property" :label="$t('warehouse.property')" icon="img:statics/warehouse/property.png" to="/warehouse/property" exact/>
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
  name: 'Pagewarehouse',
  data () {
    return {
      detaillink: 'warehouse'
    }
  },
  methods: {
  }
}
</script>
