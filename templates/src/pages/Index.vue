<template>
  <q-page :class="{'flex': device === 2, 'flex flex-center': device !== 2,}">
    <lottie-web-cimo v-show="device !== 2" ref="lottie_web" style="width: 40%; max-width: 70%"/>
    <div v-show="device === 2" :style="{height: height,width: width}">
      <div class="q-gutter-x-md q-gutter-y-xl">
        <q-card flat>
        <q-card-section horizontal>
          <q-card-actions class="col-6" align="center">
            <q-btn icon="img:statics/inbound/preloadstock.png" :label="$t('scan.scan_sorting')" stack flat color="black" size="xl" to="scan_sorting"/>
          </q-card-actions>
          <q-separator vertical></q-separator>
          <q-card-actions class="col-6" align="center">
            <q-btn icon="img:statics/inbound/presortstock.png" :label="$t('scan.scan_uptobin')" stack flat color="black" size="xl"/>
          </q-card-actions>
        </q-card-section>
          <q-separator></q-separator>
          <q-card-section horizontal>
            <q-card-actions class="col-6" align="center">
              <q-btn icon="img:statics/outbound/picked.png" :label="$t('scan.scan_picking')" stack flat color="black" size="xl" />
            </q-card-actions>
            <q-separator vertical></q-separator>
            <q-card-actions class="col-6" align="center">
              <q-btn icon="img:statics/icons/car.png" :label="$t('scan.scan_shipping')" stack flat color="black" size="xl"/>
            </q-card-actions>
          </q-card-section>
          <q-separator></q-separator>
          <q-card-section horizontal>
            <q-card-actions class="col-6" align="center">
              <q-btn icon="img:statics/icons/movetobin.png" :label="$t('scan.scan_movetobin')" stack flat color="black" size="xl" />
            </q-card-actions>
            <q-separator vertical></q-separator>
            <q-card-actions class="col-6" align="center">
              <q-btn icon="img:statics/stock/cyclecount.png" :label="$t('scan.scan_inventory')" stack flat color="black" size="xl" to="scan_cyclecount"/>
            </q-card-actions>
          </q-card-section>
          <q-separator></q-separator>
          <q-card-section horizontal>
            <q-card-actions class="col-6" align="center">
              <q-btn icon="img:statics/goods/goodslist.png" :label="$t('scan.scan_goodsquery')" stack flat color="black" size="xl" to="scan_goodslist"/>
            </q-card-actions>
            <q-separator vertical></q-separator>
            <q-card-actions class="col-6" align="center">
              <q-btn icon="img:statics/stock/stocklist.png" :label="$t('scan.scan_locationquery')" stack flat color="black" size="xl" to="scan_stockbinlist"/>
            </q-card-actions>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>
<script>
import LottieWebCimo from 'components/lottie-web-cimo'
import { database } from '../db/database'

export default {
  name: 'PageIndex',
  components: { LottieWebCimo },
  data () {
    return {
      cleardata: [],
      device: 0,
      height: '',
      width: '100%'
    }
  },
  mounted: function () {
    var _this = this
    if (window.device) {
      if (window.device.manufacturer === 'Urovo' || window.device.manufacturer === 'Zebra Technologies') {
        _this.device = 2
      } else {
        _this.device = 1
      }
    } else {
      if (_this.$q.platform.is.mobile) {
        _this.device = 1
      }
    }
    var page = database.getInstance().get().test
    page.toArray().then(res => {
      if (res.length > 0) {
        this.cleardata = []
        page.each(result => {
          this.cleardata.push(result.id)
        })
        page.bulkDelete(this.cleardata)
        this.cleardata = []
      } else {
        page.add({
          id: 1,
          test: 'next'
        })
      }
    })
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height) + 'px'
    } else {
      _this.height = _this.$q.screen.height + '' + 'px'
    }
  }
}
</script>
