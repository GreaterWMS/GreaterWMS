<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
  <q-route-tab name="warehouseset" label="warehouse" icon="img:statics/warehouse/warehouseset.png" to="/warehouse/warehouseset" exact/>
  <q-route-tab name="binset" label="bin_set" icon="img:statics/warehouse/binset.png" to="/warehouse/binset" exact/>
  <q-route-tab name="binsize" label="bin_size" icon="img:statics/warehouse/binsize.png" to="/warehouse/binsize" exact/>
  <q-route-tab name="property" label="bin_property" icon="img:statics/warehouse/property.png" to="/warehouse/property" exact/>
      </q-tabs>
    </div>
  </div>
</template>
    <router-view />
  </q-page>
</template>

<script>
export default {
  name: 'Pagewarehouse',
  data () {
    return {
      detaillink: 'warehouse'
    }
  },
  methods: {
  }
}
</script>
