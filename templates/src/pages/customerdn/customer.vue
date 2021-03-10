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
                               $q.localStorage.getItem('staff_type') !== 'Supervisor' &&
                               $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                               $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                               $q.localStorage.getItem('staff_type') !== 'StockControl'
                              "
                       name="customerdnlist" :label="$t('menuItem.customerdn')" icon="img:statics/outbound/dnlist.png" to="/customerdn/customerdnlist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                               $q.localStorage.getItem('staff_type') !== 'Supervisor' &&
                               $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                               $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                               $q.localStorage.getItem('staff_type') !== 'StockControl'
                              "
                       name="customerpod" :label="$t('outbound.pod')" icon="img:statics/outbound/receiving.png" to="/customerdn/customerpod" exact/>
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
  name: 'Pagecustomer',
  data () {
    return {
      detaillink: 'customerdn'
    }
  },
  methods: {
  }
}
</script>
