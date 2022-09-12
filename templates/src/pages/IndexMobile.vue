<template>
  <q-page v-show="!fab" class="flex flex-center">
    <div style="margin-top: -7%;">
      <div className="q-mb-xl" style="color: #4C5875;text-align: center;">
        <div style="font-weight: bold;font-size: 50px;letter-spacing: 10px;">WELCOME</div>
        <div style="font-size: 18px;letter-spacing: 2px;">
          GreaterWMS
          <span v-if="isEnglish">&nbsp</span>
          {{ $t('index.index_title') }}
        </div>
      </div>
      <div class="flex flex-center">
        <lottie-web-cimo ref="lottie_web" style="width: 60%; max-width: 80%"/>
      </div>
    </div>
    <div style="position: absolute;right: 2%;bottom: 8%;font-family:SourceHanSansCN; font-size: 16px;color: #4C5875;">——
      &nbsp;&nbsp; Easy Come &nbsp; Easy Go &nbsp; &nbsp;——
    </div>
  </q-page>
</template>
<script>
import LottieWebCimo from 'components/lottie-web-cimo'
import { database } from '../db/database'
import { Platform, LocalStorage } from 'quasar'

export default {
  name: 'PageIndexMobile',
  components: { LottieWebCimo },
  data () {
    return {
      isEnglish: false,
      cleardata: [],
      height: '',
      width: '100%'
    }
  },
  methods: {},
  beforeCreate: function () {
    if (Platform.is.cordova) {
      navigator.splashscreen.show()
    }
  },
  computed: {
    fab: {
      get () {
        return this.$store.state.fabchange.fab
      }
    }
  },
  created: function () {
    LocalStorage.set('menulink', '')
    if (this.$q.localStorage.getItem('lang') === 'en-us') {
      this.isEnglish = true
    } else {
      this.isEnglish = false
    }
  },
  beforeMount: function () {
    if (Platform.is.cordova) {
      window.setTimeout(function () {
        navigator.splashscreen.hide()
      }, -1000)
    }
  },
  mounted: function () {
    var _this = this
    var page = database.getInstance().get().test
    page.toArray().then(res => {
      if (res.length > 0) {
        _this.cleardata = []
        page.each(result => {
          _this.cleardata.push(result.id)
        })
        page.bulkDelete(this.cleardata)
        _this.cleardata = []
      } else {
        page.add({
          id: 1,
          test: 'next'
        })
      }
    })
  }
}
</script>
