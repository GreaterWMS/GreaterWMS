import { store } from 'quasar/wrappers';
import { createStore } from 'vuex';
import fabchange from './fabchange';
import langchange from './langchange';
import loginauth from './loginauth';
import screenchange from './screenchange';
import settings from './settings';
import scanchanged from './scanchanged';
import linkchange from './linkchange';
import VuexPersistence from 'vuex-persist';

// import example from './module-example'

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

const vuexLocal = new VuexPersistence({
    storage: window.localStorage
});

export default store(function (/* { ssrContext } */) {
  const Store = createStore({
    modules: {
      fabchange,
      langchange,
      loginauth,
      screenchange,
      settings,
      scanchanged,
      linkchange
    },
    plugins: [vuexLocal.plugin],

    // enable strict mode (adds overhead!)
    // for dev mode and --debug builds only
    strict: process.env.DEBUGGING
  })

  return Store
})
