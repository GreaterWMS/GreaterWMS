<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="stafflist" :label="$t('staff.staff')" icon="img:statics/staff/stafflist.png" to="/staff/stafflist" exact/>
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
