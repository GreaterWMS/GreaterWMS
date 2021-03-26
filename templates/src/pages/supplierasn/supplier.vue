<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Admin' &&
                               $q.localStorage.getItem('staff_type') !== 'Manager' &&
                               $q.localStorage.getItem('staff_type') !== 'Supervisor' &&
                               $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                               $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                               $q.localStorage.getItem('staff_type') !== 'StockControl' &&
                               $q.localStorage.getItem('staff_type') !== 'Customer'
                              "
                       name="supplierasnlist" :label="$t('inbound.asn')" icon="img:statics/inbound/asn.png" to="/supplierasn/supplierasnlist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Admin' &&
                               $q.localStorage.getItem('staff_type') !== 'Manager' &&
                               $q.localStorage.getItem('staff_type') !== 'Supervisor' &&
                               $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                               $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                               $q.localStorage.getItem('staff_type') !== 'StockControl' &&
                               $q.localStorage.getItem('staff_type') !== 'Customer'
                              "
                       name="supplierasnfinish" :label="$t('inbound.asnfinish')" icon="img:statics/inbound/asnfinish.png" to="/supplierasn/supplierasnfinish" exact/>
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
