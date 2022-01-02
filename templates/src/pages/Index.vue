<template>
  <q-page class="flex flex-center">
    <div style="margin-top: -7%;">
      <div class="q-mb-xl" style="color: #4C5875;text-align: center;">
        <div style="font-weight: bold;font-size: 100px;letter-spacing: 10px;">WELCOME</div>
        <div style="font-size: 22px;letter-spacing: 2px;">
          GreaterWMS
          <span v-if="isEnglish">&nbsp</span>
          {{ $t('index.index_title') }}
        </div>
      </div>
      <div class="flex flex-center">
        <lottie-web-cimo ref="lottie_web" style="width: 50%; max-width: 80%" />
      </div>
    </div>
    <div style="position: absolute;right: 2%;bottom: 8%;font-family:SourceHanSansCN; font-size: 16px;color: #4C5875;">—— &nbsp;&nbsp; Easy Come &nbsp; Easy Go &nbsp; &nbsp;——</div>
  </q-page>
</template>
<script>
import LottieWebCimo from 'components/lottie-web-cimo'
import { database } from '../db/database'
import { Platform, LocalStorage, Screen } from 'quasar'

export default {
  name: 'PageIndex',
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
  },
  mounted: function () {
    var _this = this
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
    if (Platform.is.electron) {
      _this.height = String(Screen.height) + 'px'
    } else {
      _this.height = Screen.height + '' + 'px'
    }
  }
}
</script>
