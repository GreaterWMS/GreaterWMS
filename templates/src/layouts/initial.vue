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
      webto: ''
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
          _this.webto = 'zebrascan'
        } else if (window.device.manufacturer === 'Urovo' || window.device.manufacturer === 'ubx') {
          LocalStorage.set('device', 2)
          _this.webto = 'urovoscan'
        } else if (window.device.manufacturer === 'SEUIC') {
          LocalStorage.set('device', 2)
          _this.webto = 'seuicscan'
        } else {
          LocalStorage.set('device', 1)
          _this.webto = 'mobilescan'
        }
      }
    } else if (Platform.is.mobile) {
      LocalStorage.set('device', 1)
      _this.webto = 'mobilescan'
    } else {
      LocalStorage.set('device', 0)
      _this.webto = 'web_index'
      if (LocalStorage.has('menulink')) {
        if (LocalStorage.getItem('menulink') !== '') {
          _this.webto = LocalStorage.getItem('menulink')
        }
      }
    }
    _this.$router.push({ name: _this.webto })
  }
}
</script>

<style scoped>

</style>
