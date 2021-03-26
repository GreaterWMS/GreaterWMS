<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="goodslist" :label="$t('goods.goods_list')" icon="img:statics/goods/goodslist.png" to="/goods/goodslist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') === 'Supplier'
                              " name="goodslist" :label="$t('goods.goods_list')" icon="img:statics/goods/goodslist.png" to="/goods/goodslist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') === 'Customer'
                              " name="goodslist" :label="$t('goods.goods_list')" icon="img:statics/goods/goodslist.png" to="/goods/goodslist" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="goodsunit" :label="$t('goods.unit')" icon="img:statics/goods/goodsunit.png" to="/goods/goodsunit" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="goodsclass" :label="$t('goods.class')" icon="img:statics/goods/goodsclass.png" to="/goods/goodsclass" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="goodscolor" :label="$t('goods.color')" icon="img:statics/goods/goodscolor.png" to="/goods/goodscolor" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="goodsbrand" :label="$t('goods.brand')" icon="img:statics/goods/goodsbrand.png" to="/goods/goodsbrand" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="goodsshape" :label="$t('goods.shape')" icon="img:statics/goods/goodsshape.png" to="/goods/goodsshape" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="goodsspecs" :label="$t('goods.specs')" icon="img:statics/goods/goodsspecs.png" to="/goods/goodsspecs" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="goodsorigin" :label="$t('goods.origin')" icon="img:statics/goods/goodsorigin.png" to="/goods/goodsorigin" exact/>
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
