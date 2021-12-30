<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="company" :label="$t('baseinfo.company_info')" icon="img:statics/baseinfo/company.png" :to="{ name: 'company' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="supplier" :label="$t('baseinfo.supplier')" icon="img:statics/baseinfo/supplier.png" :to="{ name: 'supplier' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="customer" :label="$t('baseinfo.customer')" icon="img:statics/baseinfo/customer.png" :to="{ name: 'customer' }" exact/>
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
