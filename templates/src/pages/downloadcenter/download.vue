<template>
  <q-page class="flex flex-top">
    <template>
      <div class="q-pa-md">
        <div class="q-gutter-y-md" style="max-width: 100%">
          <q-tabs>
            <transition appear enter-active-class="animated zoomIn">
              <q-route-tab
                v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' && $q.localStorage.getItem('staff_type') !== 'Customer'"
                name="downloadinbound"
                :label="$t('inbound.asn')"
                icon="img:statics/inbound/asn.png"
                to="/downloadcenter/downloadinbound"
                exact
              />
            </transition>
            <transition appear enter-active-class="animated zoomIn">
              <q-route-tab
                v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' && $q.localStorage.getItem('staff_type') !== 'Customer'"
                name="downloadoutbound"
                :label="$t('outbound.dn')"
                icon="img:statics/outbound/dnlist.png"
                to="/downloadcenter/downloadoutbound"
                exact
              />
            </transition>
            <transition appear enter-active-class="animated zoomIn">
              <q-route-tab
                v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' && $q.localStorage.getItem('staff_type') !== 'Customer'"
                name="downloadstocklist"
                :label="$t('stock.stocklist')"
                icon="img:statics/stock/stocklist.png"
                to="/downloadcenter/downloadstocklist"
                exact
              />
            </transition>
            <transition appear enter-active-class="animated zoomIn">
              <q-route-tab
                v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' && $q.localStorage.getItem('staff_type') !== 'Customer'"
                name="downloadbinlist"
                :label="$t('stock.stockbinlist')"
                icon="img:statics/warehouse/binset.png"
                to="/downloadcenter/downloadbinlist"
                exact
              />
            </transition>
            <transition appear enter-active-class="animated zoomIn">
              <q-route-tab
                v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' && $q.localStorage.getItem('staff_type') !== 'Customer'"
                name="downloadgoodslist"
                :label="$t('goods.goods_list')"
                icon="img:statics/goods/goodslist.png"
                to="/downloadcenter/downloadgoodslist"
                exact
              />
            </transition>
          </q-tabs>
        </div>
      </div>
    </template>
    <div class="main-table"><router-view /></div>
  </q-page>
</template>

<script>
export default {
  name: 'download'
};
</script>

<style scoped></style>
