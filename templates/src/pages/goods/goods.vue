<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="goodslist" :label="$t('goods.goods_list')" icon="img:statics/goods/goodslist.png" :to="{ name: 'goodslist' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="goodsunit" :label="$t('goods.unit')" icon="img:statics/goods/goodsunit.png" :to="{ name: 'goodsunit' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="goodsclass" :label="$t('goods.class')" icon="img:statics/goods/goodsclass.png" :to="{ name: 'goodsclass' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="goodscolor" :label="$t('goods.color')" icon="img:statics/goods/goodscolor.png" :to="{ name: 'goodscolor' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="goodsbrand" :label="$t('goods.brand')" icon="img:statics/goods/goodsbrand.png" :to="{ name: 'goodsbrand' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="goodsshape" :label="$t('goods.shape')" icon="img:statics/goods/goodsshape.png" :to="{ name: 'goodsshape' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="goodsspecs" :label="$t('goods.specs')" icon="img:statics/goods/goodsspecs.png" :to="{ name: 'goodsspecs' }" exact/>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="goodsorigin" :label="$t('goods.origin')" icon="img:statics/goods/goodsorigin.png" :to="{ name: 'goodsorigin' }" exact/>
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
