<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="solist" label="出库列表" icon="img:statics/outbound/solist.png" to="/outbound/solist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="neworder" label="新订单" icon="img:statics/outbound/solist.png" to="/outbound/neworder" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="orderrelease" label="订单释放" icon="img:statics/outbound/solist.png" to="/outbound/orderrelease" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="pickstock" label="待拣货" icon="img:statics/outbound/solist.png" to="/outbound/pickstock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="pickedstock" label="待发货" icon="img:statics/outbound/solist.png" to="/outbound/pickedstock" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="backorder" label="欠货订单" icon="img:statics/outbound/solist.png" to="/outbound/backorder" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="sodetail" label="发货明细" icon="img:statics/outbound/solist.png" to="/outbound/sodetail" exact/>
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
