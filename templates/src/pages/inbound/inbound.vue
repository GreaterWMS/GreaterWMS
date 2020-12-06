<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="asn" label="ASN" icon="img:statics/inbound/asn.png" to="/inbound/asn" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="predeliverystock" label="Pre Delivery" icon="img:statics/inbound/polist.png" to="/inbound/predeliverystock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="preloadstock" label="Pre Load" icon="img:statics/inbound/preloadstock.png" to="/inbound/preloadstock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="presortstock" label="Sorting" icon="img:statics/inbound/presortstock.png" to="/inbound/presortstock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="sortstock" label="Sorted" icon="img:statics/inbound/sortstock.png" to="/inbound/sortstock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="shortage" label="Shortage Qty" icon="img:statics/inbound/shortage.png" to="/inbound/shortage" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="more" label="More Qty" icon="img:statics/inbound/more.png" to="/inbound/more" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="asnfinish" label="Receiving List" icon="img:statics/inbound/asnfinish.png" to="/inbound/asnfinish" exact/>
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
      detaillink: 'asn'
    }
  },
  methods: {
  }
}
</script>
