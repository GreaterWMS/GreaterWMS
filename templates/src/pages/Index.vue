<template>
  <q-page class="flex flex-center">
    <lottie-web-cimo v-show="device === 0" ref="lottie_web" style="width: 40%; max-width: 80%"/>
    <lottie-web-cimo v-show="device === 1" ref="lottie_web" style="width: 60%; max-width: 80%"/>
    <lottie-web-cimo v-show="device === 2 && !fab" ref="lottie_web" style="width: 90%; max-width: 90%"/>
    <!--    <div v-show="device === 2" :style="{height: height,width: width}">-->
    <!--      <div class="q-gutter-x-md q-gutter-y-xl">-->
    <!--        <q-card flat>-->
    <!--          <q-card-section horizontal>-->
    <!--            <q-card-actions class="col-6" align="center">-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Zebra Technologies'" icon="img:statics/inbound/preloadstock.png" :label="$t('scan.scan_sorting')" stack flat color="black" size="xl" to="zebra_sorting"/>-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Urovo'" icon="img:statics/inbound/preloadstock.png" :label="$t('scan.scan_sorting')" stack flat color="black" size="xl" to="urovo_sorting"/>-->
    <!--            </q-card-actions>-->
    <!--            <q-separator vertical></q-separator>-->
    <!--            <q-card-actions class="col-6" align="center">-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Zebra Technologies'" icon="img:statics/inbound/presortstock.png" :label="$t('scan.scan_uptobin')" stack flat color="black" size="xl" to="zebra_uptobin"/>-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Urovo'" icon="img:statics/inbound/presortstock.png" :label="$t('scan.scan_uptobin')" stack flat color="black" size="xl" to="urovo_uptobin"/>-->
    <!--            </q-card-actions>-->
    <!--          </q-card-section>-->
    <!--          <q-separator></q-separator>-->
    <!--          <q-card-section horizontal>-->
    <!--            <q-card-actions class="col-6" align="center">-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Zebra Technologies'" icon="img:statics/outbound/picked.png" :label="$t('scan.scan_picking')" stack flat color="black" size="xl" to="zebra_picking"/>-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Urovo'" icon="img:statics/outbound/picked.png" :label="$t('scan.scan_picking')" stack flat color="black" size="xl" to="urovo_picking"/>-->
    <!--            </q-card-actions>-->
    <!--            <q-separator vertical></q-separator>-->
    <!--            <q-card-actions class="col-6" align="center">-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Zebra Technologies'" icon="img:statics/icons/car.png" :label="$t('scan.scan_shipping')" stack flat color="black" size="xl" to="zebra_shipping"/>-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Urovo'" icon="img:statics/icons/car.png" :label="$t('scan.scan_shipping')" stack flat color="black" size="xl" to="urovo_shipping"/>-->
    <!--            </q-card-actions>-->
    <!--          </q-card-section>-->
    <!--          <q-separator></q-separator>-->
    <!--          <q-card-section horizontal>-->
    <!--            <q-card-actions class="col-6" align="center">-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Zebra Technologies'" icon="img:statics/icons/movetobin.png" :label="$t('scan.scan_movetobin')" stack flat color="black" size="xl" to="zebra_movetobin"/>-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Urovo'" icon="img:statics/icons/movetobin.png" :label="$t('scan.scan_movetobin')" stack flat color="black" size="xl" to="urovo_movetobin"/>-->
    <!--            </q-card-actions>-->
    <!--            <q-separator vertical></q-separator>-->
    <!--            <q-card-actions class="col-6" align="center">-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Zebra Technologies'" icon="img:statics/stock/cyclecount.png" :label="$t('scan.scan_inventory')" stack flat color="black" size="xl" to="zebra_cyclecount"/>-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Urovo'" icon="img:statics/stock/cyclecount.png" :label="$t('scan.scan_inventory')" stack flat color="black" size="xl" to="urovo_cyclecount"/>-->
    <!--            </q-card-actions>-->
    <!--          </q-card-section>-->
    <!--          <q-separator></q-separator>-->
    <!--          <q-card-section horizontal>-->
    <!--            <q-card-actions class="col-6" align="center">-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Zebra Technologies'" icon="img:statics/goods/goodslist.png" :label="$t('scan.scan_goodsquery')" stack flat color="black" size="xl" to="zebra_goodslist"/>-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Urovo'" icon="img:statics/goods/goodslist.png" :label="$t('scan.scan_goodsquery')" stack flat color="black" size="xl" to="urovo_goodslist"/>-->
    <!--            </q-card-actions>-->
    <!--            <q-separator vertical></q-separator>-->
    <!--            <q-card-actions class="col-6" align="center">-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Zebra Technologies'" icon="img:statics/stock/stocklist.png" :label="$t('scan.scan_locationquery')" stack flat color="black" size="xl" to="zebra_locationquery"/>-->
    <!--              <q-btn v-show="device_name !== '' && device_name === 'Urovo'" icon="img:statics/stock/stocklist.png" :label="$t('scan.scan_locationquery')" stack flat color="black" size="xl" to="urovo_locationquery"/>-->
    <!--            </q-card-actions>-->
    <!--          </q-card-section>-->
    <!--        </q-card>-->
    <!--      </div>-->
    <!--    </div>-->
    <q-page-sticky v-show="device === 2" position="bottom-right" :offset="[18, 18]">
      <q-fab
        v-model="fab"
        icon="add"
        direction="up"
        color="accent"
        vertical-actions-align="left"
      >
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="bg-white text-black"
          :label="$t('scan.scan_locationquery')"
          v-show="device_name === 'Urovo'"
          to="urovo_locationquery"
          :style="{
                         'margin-top': fab8.top,
                         'margin-bottom': fab8.bottom,
                         'margin-left': fab8.left,
                         'margin-right': fab8.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/stock/stocklist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="bg-white text-black"
          :label="$t('scan.scan_locationquery')"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_locationquery"
          :style="{
                         'margin-top': fab8.top,
                         'margin-bottom': fab8.bottom,
                         'margin-left': fab8.left,
                         'margin-right': fab8.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/stock/stocklist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="bg-white text-black"
          :label="$t('scan.scan_goodsquery')"
          :style="{
                         'margin-top': fab7.top,
                         'margin-bottom': fab7.bottom,
                         'margin-left': fab7.left,
                         'margin-right': fab7.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/goods/goodslist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="bg-white text-black"
          icon="img:statics/stock/cyclecount.png"
          :label="$t('scan.scan_inventory')"
          :style="{
                         'margin-top': fab6.top,
                         'margin-bottom': fab6.bottom,
                         'margin-left': fab6.left,
                         'margin-right': fab6.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/stock/cyclecount.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="bg-white text-black"
          :label="$t('scan.scan_movetobin')"
          :style="{
                         'margin-top': fab5.top,
                         'margin-bottom': fab5.bottom,
                         'margin-left': fab5.left,
                         'margin-right': fab5.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/icons/movetobin.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="bg-white text-black"
          :label="$t('scan.scan_shipping')"
          :style="{
                         'margin-top': fab4.top,
                         'margin-bottom': fab4.bottom,
                         'margin-left': fab4.left,
                         'margin-right': fab4.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/icons/car.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="bg-white text-black"
          :label="$t('scan.scan_picking')"
          :style="{
                         'margin-top': fab3.top,
                         'margin-bottom': fab3.bottom,
                         'margin-left': fab3.left,
                         'margin-right': fab3.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/outbound/picked.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="bg-white text-black"
          :label="$t('scan.scan_uptobin')"
          :style="{
                         'margin-top': fab2.top,
                         'margin-bottom': fab2.bottom,
                         'margin-left': fab2.left,
                         'margin-right': fab2.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/inbound/presortstock.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="bg-white text-black"
          :label="$t('scan.scan_sorting')"
          :style="{
                         'margin-top': fab1.top,
                         'margin-bottom': fab1.bottom,
                         'margin-left': fab1.left,
                         'margin-right': fab1.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/inbound/preloadstock.png" />
        </q-fab-action>
      </q-fab>
    </q-page-sticky>
  </q-page>
</template>
<script>
import LottieWebCimo from 'components/lottie-web-cimo'
import { database } from '../db/database'
import Vconsole from 'vconsole'
if (process.env.NODE_ENV !== 'production') {
  const vConsole = new Vconsole()
}

export default {
  name: 'PageIndex',
  components: { LottieWebCimo },
  data () {
    return {
      cleardata: [],
      device: 0,
      device_name: '',
      height: '',
      width: '100%',
      fab: false,
      touchheight: ((this.$q.screen.width - 50) / 5) + '' + 'px',
      touchwidth: ((this.$q.screen.width - 50) / 5) + '' + 'px',
      fab1: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab2: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab3: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab4: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab5: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab6: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab7: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab8: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      }
    }
  },
  methods: {
  },
  mounted: function () {
    var _this = this
    if (window.device) {
      if (window.device.manufacturer === 'Urovo' || window.device.manufacturer === 'Zebra Technologies') {
        _this.device_name = window.device.manufacturer
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
    } else if (_this.$q.platform.is.cordova) {
      if (window.device) {
        if (window.device.manufacturer === 'Urovo' || window.device.manufacturer === 'Zebra Technologies') {
          console.log(window.screen.height, window.screen.width)
          _this.fab1.top = '0px'
          _this.fab1.bottom = (0 - ((_this.$q.screen.width - 50) / 5)) + '' + 'px'
          _this.fab1.left = (((_this.$q.screen.width - 50) / 5) - (_this.$q.screen.width / 12 * 10)) + '' + 'px'
          _this.fab1.right = '0px'
          _this.fab2.top = '0px'
          _this.fab2.bottom = (0 - ((_this.$q.screen.width - 50) / 5)) + '' + 'px'
          _this.fab2.left = ((((_this.$q.screen.width - 50) / 5) - (_this.$q.screen.width / 12 * 10)) / 2) + '' + 'px'
          _this.fab2.right = '0px'
          _this.fab3.top = '0px'
          _this.fab3.bottom = '0px'
          _this.fab3.left = '-0px'
          _this.fab3.right = '0px'
          _this.fab4.top = ((_this.$q.screen.width - 50) / 5) + '' + 'px'
          _this.fab4.bottom = (0 - ((_this.$q.screen.width - 50) / 5)) + '' + 'px'
          _this.fab4.left = (((_this.$q.screen.width - 50) / 5) - (_this.$q.screen.width / 12 * 10)) + '' + 'px'
          _this.fab4.right = '0px'
          _this.fab5.top = '0px'
          _this.fab5.bottom = (0 - ((_this.$q.screen.width - 50) / 5)) + '' + 'px'
          _this.fab5.left = ((((_this.$q.screen.width - 50) / 5) - (_this.$q.screen.width / 12 * 10)) / 2) + '' + 'px'
          _this.fab5.right = '0px'
          _this.fab6.top = '0px'
          _this.fab6.bottom = '0px'
          _this.fab6.left = '0px'
          _this.fab6.right = '0px'
          _this.fab7.top = ((_this.$q.screen.width - 50) / 5) + '' + 'px'
          _this.fab7.bottom = (0 - ((_this.$q.screen.width - 50) / 5)) + '' + 'px'
          _this.fab7.left = (((_this.$q.screen.width - 50) / 5) - (_this.$q.screen.width / 12 * 10)) + '' + 'px'
          _this.fab7.right = '0px'
          _this.fab8.top = '0px'
          _this.fab8.bottom = ((_this.$q.screen.width - 50) / 5) + '' + 'px'
          _this.fab8.left = ((((_this.$q.screen.width - 50) / 5) - (_this.$q.screen.width / 12 * 10)) / 2) + '' + 'px'
          _this.fab8.right = '0px'
        }
      }
    } else {
      _this.height = _this.$q.screen.height + '' + 'px'
    }
  }
}
</script>
