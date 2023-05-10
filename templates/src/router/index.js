import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './routes'
import { LocalStorage } from "quasar";

Vue.use(VueRouter)

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function (location) {
  try {
    return originalPush.call(this, location).catch(err => err)
  } catch (error) {
    console.error(error)
  }
}

var openid = LocalStorage.getItem('lang')
if (LocalStorage.has('openid')) {
  openid = openid || ''
} else {
  LocalStorage.set('openid', '')
  openid = ''
}

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default function (/* { store, ssrContext } */) {
  const Router = new VueRouter({
    scrollBehavior: () => ({ x: 0, y: 0 }),
    routes,

    // Leave these as they are and change in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  })

  return Router
}
