import { app, BrowserWindow, ipcMain, nativeTheme } from 'electron'
import { autoUpdater } from 'electron-updater'
import isDev from 'electron-is-dev'
import path from 'path'
import { PosPrinter } from 'electron-pos-printer'

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
  global.__statics = __dirname
}

let mainWindow

function createWindow () {
  /**
   * Initial window options
   */
  mainWindow = new BrowserWindow({
    width: 1000,
    height: 600,
    useContentSize: true,
    webPreferences: {
      // Change from /quasar.conf.js > electron > nodeIntegration;
      // More info: https://quasar.dev/quasar-cli/developing-electron-apps/node-integration
      nodeIntegration: process.env.QUASAR_NODE_INTEGRATION,
      nodeIntegrationInWorker: process.env.QUASAR_NODE_INTEGRATION,

      // More info: /quasar-cli/developing-electron-apps/electron-preload-script
      preload: path.resolve(__dirname, 'electron-preload.js')
    }
  })
  mainWindow.maximize()
  mainWindow.loadURL(process.env.APP_URL).then(r => console.log(r))
  if (isDev) {
    mainWindow.webContents.openDevTools()
  }
  mainWindow.setMenuBarVisibility(false)
  mainWindow.on('closed', () => {
    mainWindow = null
  })
  if (!isDev) {
    autoUpdater.autoDownload = false
    autoUpdater.on('error', (error) => {
      sendUpdateMessage({
        cmd: 'error',
        message: error
      })
    })
    autoUpdater.on('checking-for-update', (info) => {
      sendUpdateMessage({
        cmd: 'checking-for-update',
        message: info
      })
    })
    autoUpdater.on('update-available', (info) => {
      sendUpdateMessage({
        cmd: 'update-available',
        message: info
      })
    })
    autoUpdater.on('update-not-available', (info) => {
      sendUpdateMessage({
        cmd: 'update-not-available',
        message: info
      })
    })
    autoUpdater.on('download-progress', function (progressObj) {
      sendUpdateMessage({
        cmd: 'download-progress',
        message: progressObj
      })
    })
    autoUpdater.on('update-downloaded', function (event, releaseNotes, releaseName, releaseDate, updateUrl) {
      sendUpdateMessage({
        cmd: 'update-downloaded',
        message: {
          releaseNotes: releaseNotes,
          releaseName: releaseName,
          releaseDate: releaseDate,
          updateUrl: updateUrl
        }
      })
    })
    ipcMain.on('checkForUpdate', (e, arg) => {
      autoUpdater.setFeedURL(arg)
      autoUpdater.checkForUpdates()
    })
    ipcMain.on('downloadUpdate', (e, arg) => {
      autoUpdater.downloadUpdate()
    })
    ipcMain.on('updateNow', (e, arg) => {
      autoUpdater.quitAndInstall()
    })
    ipcMain.on('printData', (e, arg) => {
      const data = JSON.parse(arg)
      PosPrinter.print(JSON.parse(arg.data), {
        copies: 1,
        timeOutPerLine: 400,
        silent: true,
        preview: true,
        printerName: data.printer
      }).catch(err => {
        console.log(err)
      })
    })
  }
}

function sendUpdateMessage (text) {
  mainWindow.webContents.send('message', text)
}

app.on('ready', () => {
  createWindow()
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
