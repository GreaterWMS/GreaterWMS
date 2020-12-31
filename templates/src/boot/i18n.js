import Vue from 'vue'
import VueI18n from 'vue-i18n'
import messages from 'src/i18n'
import axios from 'axios'
import { LocalStorage } from 'quasar'

Vue.use(VueI18n)

if (LocalStorage.has('country')) {
} else {
  axios.post('https://www.56yhz.com/area/').then(res => {
    LocalStorage.set('country', res.data.country)
  })
}
var getcountry = LocalStorage.getItem('country')
getcountry = getcountry || 'United States'
var getlang = ''
if (getcountry === 'China') {
  getlang = 'zh-hans'
} else {
  getlang = 'en-us'
}
var lang = LocalStorage.getItem('lang')
lang = lang || getlang

const i18n = new VueI18n({
  locale: lang,
  fallbackLocale: lang,
  messages
})

export default ({ app }) => {
  app.i18n = i18n
}

export { i18n }
