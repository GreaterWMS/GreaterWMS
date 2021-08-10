<template>
  <q-page class="flex flex-center">
      <lottie-web-cimo ref="lottie_web" style="width: 40%; max-width: 70%"/>
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
      cleardata: []
    }
  },
  mounted: function () {
    var page = database.getInstance().get().a
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
          a: 'next',
          b: '',
          c: 'previous',
          d: '',
          e: '',
          f: '',
          g: ''
        })
      }
    })
  }
}
</script>
