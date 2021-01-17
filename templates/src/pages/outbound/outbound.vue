<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="dn" label="DN" icon="img:statics/outbound/dnlist.png" to="/outbound/dn" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="neworder" label="New Order" icon="img:statics/outbound/order.png" to="/outbound/neworder" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="backorder" label="Back Order" icon="img:statics/outbound/backorder.png" to="/outbound/backorder" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="pickstock" label="Pre Pick" icon="img:statics/outbound/pickstock.png" to="/outbound/pickstock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="pickedstock" label="Picked" icon="img:statics/outbound/picked.png" to="/outbound/pickedstock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="shippedstock" label="Shipping Detail" icon="img:statics/outbound/outbound.png" to="/outbound/shippedstock" exact/>
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
  name: 'Pageinbound',
  data () {
    return {
      detaillink: 'outbound'
    }
  },
  methods: {
  }
}
</script>
