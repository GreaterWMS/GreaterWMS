<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="stafflist" :label="$t('staff.staff')" icon="perm_contact_calendar" :to="{ name: 'stafflist' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="stafflist_check_code" :label="$t('staff.check_code')" icon="published_with_changes" :to="{ name: 'stafflist_check_code' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="stafftype" :label="$t('staff.view_staff.staff_type')" icon="img:statics/staff/stafftype.png" :to="{ name: 'stafftype' }" exact/>
        </transition>
      </q-tabs>
    </div>
  </div>
</template>
    <div :style="{width: '100%', margin: '-10px 10px 0 10px'}">
      <router-view />
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Pagestaff',
  data () {
    return {
      detaillink: 'stafflist'
    }
  },
  methods: {
  }
}
</script>
