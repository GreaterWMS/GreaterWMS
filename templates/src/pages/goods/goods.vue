<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
  <q-route-tab name="goodslist" label="goods list" icon="img:statics/goods/goodslist.png" to="/goods/goodslist" exact/>
  <q-route-tab name="goodsunit" label="unit" icon="img:statics/goods/goodsunit.png" to="/goods/goodsunit" exact/>
  <q-route-tab name="goodsclass" label="class" icon="img:statics/goods/goodsclass.png" to="/goods/goodsclass" exact/>
  <q-route-tab name="goodscolor" label="color" icon="img:statics/goods/goodscolor.png" to="/goods/goodscolor" exact/>
  <q-route-tab name="goodsbrand" label="brand" icon="img:statics/goods/goodsbrand.png" to="/goods/goodsbrand" exact/>
  <q-route-tab name="goodsshape" label="shape" icon="img:statics/goods/goodsshape.png" to="/goods/goodsshape" exact/>
  <q-route-tab name="goodsspecs" label="specs" icon="img:statics/goods/goodsspecs.png" to="/goods/goodsspecs" exact/>
  <q-route-tab name="goodsorigin" label="origin" icon="img:statics/goods/goodsorigin.png" to="/goods/goodsorigin" exact/>
      </q-tabs>
    </div>
  </div>
</template>
    <router-view></router-view>
  </q-page>
</template>

<script>
export default {
  name: 'Pagegoods',
  data () {
    return {
      detaillink: 'goodslist'
    }
  },
  methods: {
  }
}
</script>
