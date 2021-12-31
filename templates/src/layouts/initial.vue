<template>
  <router-view />
</template>

<script>
import { LocalStorage, Platform } from 'quasar'
import Vconsole from 'vconsole'
if (process.env.NODE_ENV !== 'production') {
  const vConsole = new Vconsole()
}

export default {
  name: 'initial',
  data () {
    return {
      webto: '',
      platform: ''
    }
  },
  methods: {
  },
  beforeCreate () {
    var _this = this
    if (Platform.is.cordova) {
      if (window.device) {
        if (window.device.manufacturer === 'Zebra Technologies') {
          LocalStorage.set('device', 2)
          _this.webto = '/scanner/zebra'
        } else if (window.device.manufacturer === 'Urovo') {
          LocalStorage.set('device', 2)
          _this.webto = '/scanner/urovo'
        } else {
          LocalStorage.set('device', 1)
          _this.webto = '/mobile'
        }
      }
    } else if (Platform.is.mobile) {
      LocalStorage.set('device', 1)
      _this.webto = '/mobile'
    } else {
      LocalStorage.set('device', 0)
      _this.webto = '/web'
    }
    _this.$router.push(_this.webto)
  }
}
</script>

<style scoped>

</style>
