<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
  <q-route-tab name="company" label="Company info" icon="img:statics/baseinfo/company.png" to="/baseinfo/company" exact/>
  <q-route-tab name="supplier" label="Supplier" icon="img:statics/baseinfo/supplier.png" to="/baseinfo/supplier" exact/>
  <q-route-tab name="customer" label="Customer" icon="img:statics/baseinfo/customer.png" to="/baseinfo/customer" exact/>
      </q-tabs>
    </div>
  </div>
</template>
    <router-view />
  </q-page>
</template>

<script>
export default {
  name: 'Pagebaseinfo',
  data () {
    return {
      detaillink: 'company'
    }
  },
  methods: {
  }
}
</script>
