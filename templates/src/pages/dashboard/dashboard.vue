<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
  <q-route-tab name="sales" label="销售报表" icon="img:statics/dashboard/sales.png" to="/dashboard/sales" exact/>
      </q-tabs>
    </div>
  </div>
</template>
    <router-view />
  </q-page>
</template>

<script>
export default {
  name: 'Pagedashboard',
  data () {
    return {
      detaillink: 'dashboard'
    }
  },
  methods: {
  }
}
</script>
