/* eslint-disable */
/**
 * THIS FILE IS GENERATED AUTOMATICALLY.
 * DO NOT EDIT.
 *
 * You are probably looking on adding startup/initialization code.
 * Use "quasar new boot <name>" and add it there.
 * One boot file per concern. Then reference the file(s) in quasar.config.js > boot:
 * boot: ['file', ...] // do not add ".js" extension to it.
 *
 * Boot files are your "main.js"
 **/
import { createApp, unref } from 'vue'


import '@quasar/extras/roboto-font/roboto-font.css'

import '@quasar/extras/material-icons/material-icons.css'




// We load Quasar stylesheet file
import 'quasar/dist/quasar.sass'




import 'src/css/app.scss'


import createQuasarApp from './app.js'
import quasarUserOptions from './quasar-user-options.js'



const publicPath = `/`


const httpRE = /^https?:\/\//

function getRedirectUrl (url, router) {
  if (typeof url === 'string' && httpRE.test(url) === true) {
    return url
  }

  try { return router.resolve(url).href }
  catch (err) {}

  return url
}

const { components, directives, ...qUserOptions } = quasarUserOptions


const bootFiles = Promise.all([
  
  import('boot/i18n'),
  
  import('boot/axios'),
  
  import('boot/notify-defaults'),
  
  import('boot/vueMain')
  
]).then(bootFiles => bootFiles.map(entry => entry.default).filter(entry => typeof entry === 'function'))


// This is where we perform data-prefetching to determine the
// state of our application before actually rendering it.
// Since data fetching is async, this function is expected to
// return a Promise that resolves to the app instance.
export default ssrContext => {
  return new Promise(async (resolve, reject) => {
    
    const bootFunctions = await bootFiles
    

    const {
      app, router, store
    } = await createQuasarApp(createApp, qUserOptions, ssrContext)

    
    let hasRedirected = false
    const redirect = (url, httpStatusCode) => {
      hasRedirected = true
      reject({ url: getRedirectUrl(url, router), code: httpStatusCode })
    }

    for (let i = 0; hasRedirected === false && i < bootFunctions.length; i++) {
      try {
        await bootFunctions[i]({
          app,
          router,
          store,
          ssrContext,
          redirect,
          urlPath: ssrContext.req.url,
          publicPath
        })
      }
      catch (err) {
        reject(err)
        return
      }
    }

    if (hasRedirected === true) {
      return
    }
    

    app.use(router)
    

    const url = ssrContext.req.url
    const { fullPath } = router.resolve(url)

    if (fullPath !== url) {
      return reject({ url: fullPath })
    }

    // set router's location
    router.push(url).catch(() => {})

    // wait until router has resolved possible async hooks
    router.isReady().then(() => {
      let matchedComponents = router.currentRoute.value.matched
        .filter(record => record.components !== void 0)
        .flatMap(record => Object.values(record.components))

      // no matched routes
      if (matchedComponents.length === 0) {
        return reject({ code: 404 })
      }

      

        ssrContext.state = unref(store.state)

        resolve(app)

      
    }).catch(reject)
  })
}
