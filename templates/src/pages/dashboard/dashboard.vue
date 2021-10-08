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
                         " name="inbounddashboard" :label="$t('dashboards.outbound_statements')" icon="img:statics/dashboard/in_statement.png" to="/dashboard/inbounddashboard" exact/>
            </transition>
            <transition appear enter-active-class="animated zoomIn">
              <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="barchart" :label="$t('dashboards.inbound_statements')" icon="img:statics/dashboard/out_statement.png" to="/dashboard/barchart" exact/>
            </transition>
            <transition appear enter-active-class="animated zoomIn">
              <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="piechart" :label="$t('dashboards.stock_statements')" icon="img:statics/dashboard/in_statement.png" to="/dashboard/piechart" exact/>
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
      detaillink: 'capital'
    }
  },
  methods: {
  }
}
</script>
