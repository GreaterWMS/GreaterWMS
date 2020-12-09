import Vue from 'vue'
import VueI18n from 'vue-i18n'
import messages from 'src/i18n'
import axios from 'axios'

Vue.use(VueI18n)

var getcountry = localStorage.getItem('country')
if (!getcountry) {
  axios.post('https://www.56yhz.com/area/').then(res => {
    localStorage.setItem('country', res.data.country)
  })
}
getcountry = getcountry || 'United States'
var getlang = ''
if (getcountry === 'China') {
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
