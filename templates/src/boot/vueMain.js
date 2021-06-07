import Print from 'vue-print-nb'
import VDistpicker from 'v-distpicker'
import vueQr from "vue-qr"
export default async ({ app, router, store, Vue }) => {
  Vue.component('v-distpicker', VDistpicker)
  Vue.use(Print)
  Vue.use(vueQr)
  console.log('Welcome To GreaterWMS')
  console.log('Home Page ------ https://www.56yhz.com/')
  console.log('Demo Page ------ https://wms.56yhz.com/')
  console.log('Gitee Page ------ https://gitee.com/Singosgu/GreaterWMS')
  console.log('GitHub Page ------ https://github.com/Singosgu/GreaterWMS')
}
