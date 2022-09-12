<template>
  <div>
    <div
      left-arrow
      title="二维码扫描"
      safe-area-inset-top
      @click-left="onClickLeft"
    >
    </div>
    <div class="scroll-container scan-container">
      <div class="scan-none-1"></div>
      <div class="scan-box-container">
        <div class="scan-none-2"></div>
        <div class="scan-box">
          <div class="scan-box-area">
            <div class="top-left"></div>
            <div class="top-right"></div>
            <div class="bottom-left"></div>
            <div class="bottom-right"></div>
            <div class="light" @click="onLightTrigger">
              <i
                :class="[
                  'iconfont',
                  light
                    ? 'icon-shoudiantong-dakai'
                    : 'icon-shoudiantong-guanbi',
                ]"
              ></i>
              <span>轻触 {{ light ? "关闭" : "打开" }}</span>
            </div>
          </div>
        </div>
        <div class="scan-none-2"></div>
      </div>
      <div class="scan-none-1 scan-bottom">
        <p>请将二维码对准至框内，即可自动扫描</p>
      </div>
    </div>
  </div>
</template>

<script>
import { LocalStorage } from 'quasar'

export default {
  name: 'Scan',
  data () {
    return {
      light: false
    }
  },
  beforeCreate () {
  },
  beforeDestroy () {
    // 恢复之前的背景
    try {
      QRScanner.hide((status) => {
        console.log('[Scan.vue] 关闭扫描' + JSON.stringify(status))
      })
      QRScanner.destroy(function (status) {
        console.log('[Scan.vue] 销毁扫码' + JSON.stringify(status))
      })
    } catch (e) {
      console.log('[Scan.vue]' + JSON.stringify(e))
    }
  },
  mounted () {
    this.onScan()
    console.log(this.$route.path)
  },
  methods: {
    onClickLeft () {
      this.$router.go(-1)// 返回上一层
    },
    /**
     * 扫码
     */
    onScan () {
      var _this = this
      try {
        QRScanner.show((status) => {
          // alert('[Scan.vue onScan] 显示扫描' + JSON.stringify(status))
          console.log(Date())
        })
        QRScanner.scan((err, contents) => {
          if (err) {
            alert(JSON.stringify(e))
          } else {
            navigator.vibrate(1)
            navigator.notification.beep(1)
            alert('扫描结果: ' + contents)
            console.log(LocalStorage.getItem('linkchange'))
            _this.$router.push({ name: LocalStorage.getItem('linkchange') })
            console.log(Date())
          }
        })
      } catch (e) {
        console.log('[Scan.vue：onScan] ' + JSON.stringify(e))
      }
    },

    /**
     * 手电筒开关
     */
    onLightTrigger () {
      try {
        if (!this.light) {
          QRScanner.enableLight((err, status) => {
            err &&
              console.log(
                '[Scan.vue] 打开手电筒状态错误：' + JSON.stringify(err)
              )
            console.log('[Scan.vue] 打开手电筒状态：' + JSON.stringify(status))
          })
        } else {
          QRScanner.disableLight((err, status) => {
            err &&
              console.log(
                '[Scan.vue] 关闭手电筒状态错误：' + JSON.stringify(err)
              )
            console.log('[Scan.vue] 关闭手电筒状态：' + JSON.stringify(status))
          })
        }
      } catch (e) {
        console.log('[Scan.vue] ' + JSON.stringify(e))
        return
      }
      this.light = !this.light
    }
  }
}
</script>
<style scoped>
/* //可滚动内容区域 */
.scroll-container {
  width: 100%;
  height: 96vh;
  overflow: auto;
  -webkit-overflow-scrolling: touch;
}
::-webkit-scrollbar {
  display: none;
}
.scan-container {
  background: rgba(0, 0, 0, 0);
  display: flex;
  flex-direction: column;
}
.scan-container .scan-none-1 {
  flex: 1;
  width: 100%;
  background: rgba(0, 0, 0, 0.4);
  text-align: center;
  color: rgba(255, 255, 255, 0.8);
}
.scan-container .scan-none-1:first-child {
  flex: 0.6;
}
.scan-container .scan-box-container {
  height: 18rem;
  display: flex;
}
.scan-container .scan-box-container .scan-none-2 {
  flex: 1;
  height: 18rem;
  background: rgba(0, 0, 0, 0.4);
}

.scan-container .scan-box-container .scan-box {
  width: 18rem;
  height: 18rem;
  background: rgba(0, 0, 0, 0);
}
.scan-box .scan-box-area {
  width: 18rem;
  height: 18rem;
  position: relative;
}
.light {
  width: 18rem;
  position: absolute;
  color: rgba(255, 255, 255, 0.8);
}
.center {
  flex-direction: column;
  bottom: 0.32rem;
}

.top-left {
  position: absolute;
  top: -3px;
  left: -3px;
  width: 1rem;
  height: 1rem;
  border-top: 0.3rem solid #5f69b2;
  border-left: 0.3rem solid #5f69b2;
}

.top-right {
  position: absolute;
  top: -3px;
  right: -3px;
  width: 1rem;
  height: 1rem;
  border-top: 0.3rem solid #5f69b2;
  border-right: 0.3rem solid #5f69b2;
}

.bottom-left {
  position: absolute;
  bottom: -3px;
  left: -3px;
  width: 1rem;
  height: 1rem;
  border-bottom: 0.3rem solid #5f69b2;
  border-left: 0.3rem solid #5f69b2;
}

.bottom-right {
  position: absolute;
  bottom: -3px;
  right: -3px;
  width: 1rem;
  height: 1rem;
  border-bottom: 0.3rem solid #5f69b2;
  border-right: 0.3rem solid #5f69b2;
}
.scan-bottom {
  position: relative;
}
.bottome-icon {
  position: absolute;
  bottom: 2rem;
  left: 0;
  width: 100%;
  display: flex;
}
.bottome-icon i {
  flex: 1;
}
.bottome-icon i:first-child {
  border-right: 3px solid #ddd;
}
</style>
