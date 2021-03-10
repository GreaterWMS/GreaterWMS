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
                         " name="stafflist" :label="$t('staff.staff')" icon="img:statics/staff/stafflist.png" to="/staff/stafflist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                               $q.localStorage.getItem('staff_type') !== 'Customer' &&
                               $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                               $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                               $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                         name="stafftype" :label="$t('staff.view_staff.staff_type')" icon="img:statics/staff/stafftype.png" to="/staff/stafftype" exact/>
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
  name: 'Pagestaff',
  data () {
    return {
      detaillink: 'staff'
    }
  },
  methods: {
  }
}
</script>
