import { boot } from 'quasar/wrappers';
import { createI18n } from 'vue-i18n';
import messages from 'src/i18n';
import { LocalStorage } from 'quasar';

var lang
try {
  lang = JSON.parse(LocalStorage.getItem('vuex')).langchange.lang
} catch (err) {
  lang = 'en-US'
}

const i18n = createI18n({
  locale: lang,
  globalInjection: true,
  messages
});

export default boot(({ app }) => {
  app.use(i18n);
  app.provide('trans', i18n)
});
