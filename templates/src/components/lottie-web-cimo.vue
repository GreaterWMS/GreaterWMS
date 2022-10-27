<template>
  <div ref="lottieBox"></div>
</template>

<script>
import lottie from 'lottie-web'
var welcome = require('./welcome.json')

export default {
  name: 'lottie-web-cimo',
  data () {
    return {
      lottie: {},
      animationData: welcome,
      loop: true
    }
  },
  methods: {
    initLottie: function () {
      var _this = this
      _this.lottie = lottie.loadAnimation({
        container: _this.$refs.lottieBox,
        renderer: 'svg',
        loop: _this.loop || true,
        animationData: _this.animationData
      })
      _this.lottie.setSpeed(2.5)
    }

  },
  mounted () {
    this.initLottie()
  },
  beforeDestroy () {
    this.lottie.destroy()
    this.lottie = null
  }
}
</script>
