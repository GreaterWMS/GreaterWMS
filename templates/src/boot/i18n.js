import Vue from 'vue'
import VueI18n from 'vue-i18n'
import messages from 'src/i18n'
import Quasar from 'quasar'

Vue.use(VueI18n)

var getlang = Quasar.lang.getLocale().split('-')[0].toLowerCase()
if (getlang === 'zh') {
  getlang = 'zh-hans'
} else {
  getlang = 'en-us'
}
var lang = localStorage.getItem('lang')
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
