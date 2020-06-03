import { app, BrowserWindow, nativeTheme, screen, Menu, session } from 'electron'

try {
  if (process.platform === 'win32' && nativeTheme.shouldUseDarkColors === true) {
    require('fs').unlinkSync(require('path').join(app.getPath('userData'), 'DevTools Extensions'))
  }
} catch (_) { }

/**
 * Set `__statics` path to static files in production;
 * The reason we are setting it here is that the path needs to be evaluated at runtime
 */
if (process.env.PROD) {
  global.__statics = require('path').join(__dirname, 'statics').replace(/\\/g, '\\\\')
}

let mainWindow

function createWindow (x, y) {
  /**
   * Initial window options
   */
  Menu.setApplicationMenu(null)
  mainWindow = new BrowserWindow({
    width: x,
    height: y,
    minWidth: 1000,
    minHeight: 600,
    useContentSize: true,
    webPreferences: {
      // Change from /quasar.conf.js > electron > nodeIntegration;
      // More info: https://quasar.dev/quasar-cli/developing-electron-apps/node-integration
      // eslint-disable-next-line no-undef
      nodeIntegration: QUASAR_NODE_INTEGRATION,
      // eslint-disable-next-line no-undef
      nodeIntegrationInWorker: QUASAR_NODE_INTEGRATION,

      // More info: /quasar-cli/developing-electron-apps/electron-preload-script
      // preload: path.resolve(__dirname, 'electron-preload.js')
    }
  })
  var cookie = { url: 'file://', name: 'dummy_name', value: 'dummy' }
  session.defaultSession.cookies.set(cookie, function (error) {
    if (error) { console.error(error) }
  })
  // eslint-disable-next-line handle-callback-err
  session.defaultSession.cookies.get({ url: 'file://' }, function (error, cookies) {
    console.log(cookies)
  })
  mainWindow.loadURL(process.env.APP_URL)

  mainWindow.on('closed', () => {
    mainWindow = null
  })
}

const gotTheLock = app.requestSingleInstanceLock()
if (!gotTheLock) {
  app.quit()
} else {
  app.on('second-instance', (event, commandLine, workingDirectory) => {
    if (mainWindow) {
      if (mainWindow.isMinimized()) mainWindow.restore()
      mainWindow.focus()
      mainWindow.show()
    }
  })
}

app.on('ready', () => {
  createWindow(screen.getPrimaryDisplay().workArea.width, screen.getPrimaryDisplay().workArea.height)
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow()
  }
})
