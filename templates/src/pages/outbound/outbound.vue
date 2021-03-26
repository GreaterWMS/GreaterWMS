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
                         " name="dn" :label="$t('outbound.dn')" icon="img:statics/outbound/dnlist.png" to="/outbound/dn" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="neworder" :label="$t('outbound.neworder')" icon="img:statics/outbound/order.png" to="/outbound/neworder" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="backorder" :label="$t('outbound.backorder')" icon="img:statics/outbound/backorder.png" to="/outbound/backorder" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="pickstock" :label="$t('outbound.pickstock')" icon="img:statics/outbound/pickstock.png" to="/outbound/pickstock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="pickedstock" :label="$t('outbound.pickedstock')" icon="img:statics/outbound/picked.png" to="/outbound/pickedstock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="pickinglist" :label="$t('outbound.pickinglist')" icon="img:statics/outbound/pickinglist.png" to="/outbound/pickinglist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="shippedstock" :label="$t('outbound.shippedstock')" icon="img:statics/outbound/outbound.png" to="/outbound/shippedstock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="pod" :label="$t('outbound.pod')" icon="img:statics/outbound/receiving.png" to="/outbound/pod" exact/>
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
      detaillink: 'dn'
    }
  },
  methods: {
  }
}
</script>
