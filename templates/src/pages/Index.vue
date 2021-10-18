<template>
  <q-page class="flex flex-center">
    <lottie-web-cimo v-show="device !== 2" ref="lottie_web" style="width: 40%; max-width: 70%"/>
    <div class="q-pa-md" v-show="device === 2" style="height: 100%; max-width: 100%">
      <div class="q-gutter-x-md q-gutter-y-xl">
        <q-btn icon="phone" v-for="n in 8" :key="n" label="Stacked" stack flat color="black" />
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
      device: 0
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
  },
}
</script>
