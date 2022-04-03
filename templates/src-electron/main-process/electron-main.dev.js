import electronDebug from 'electron-debug'
import installExtension, { VUEJS_DEVTOOLS } from 'electron-devtools-installer'
import { app } from 'electron'

// Install `electron-debug` with `devtron`
electronDebug({ showDevTools: true })

// Install vuejs devtools
app.whenReady().then(() => {
  installExtension(VUEJS_DEVTOOLS)
    .then(name => {
      console.log(`Added Extension: ${name}`)
    })
    .catch(err => {
      console.log('An error occurred: ', err)
    })
})

import './electron-main'
