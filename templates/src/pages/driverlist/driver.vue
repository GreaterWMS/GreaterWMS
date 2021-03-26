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
                         " name="driverlist" :label="$t('driver.driver')" icon="img:statics/staff/driver.png" to="/driver/driverlist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="dispatchlist" :label="$t('driver.dispatchlist')" icon="img:statics/outbound/dispatchlist.png" to="/driver/dispatchlist" exact/>
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
  name: 'Pagedriver',
  data () {
    return {
      detaillink: 'driverlist'
    }
  },
  methods: {
  }
}
</script>
