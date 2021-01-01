import Vue from 'vue'
import VueI18n from 'vue-i18n'
import messages from 'src/i18n'
import axios from 'axios'
import { LocalStorage } from 'quasar'

Vue.use(VueI18n)

var lang = LocalStorage.getItem('lang')
lang = lang || 'en-us'

const i18n = new VueI18n({
  locale: lang,
  fallbackLocale: lang,
  messages
})

export default ({ app }) => {
  app.i18n = i18n
}

export { i18n }
