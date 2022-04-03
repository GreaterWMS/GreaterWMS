<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="goodslist" :label="$t('goods.goods_list')" icon="img:statics/goods/goodslist.png" :to="{ name: 'mp_goodslist' }" exact/>
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
