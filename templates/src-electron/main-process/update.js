import { autoUpdater } from 'electron-updater'
import { ipcMain } from 'electron'
import { LocalStorage } from 'quasar'
let mainWindow = null

autoUpdater.logger = require('electron-log')
autoUpdater.logger.transports.file.level = 'info'

export function updateHandle (window) {
  mainWindow = window
  autoUpdater.autoDownload = false
  if (LocalStorage.has('openid')) {
    autoUpdater.setFeedURL('https://wms.56yhz.com/' + 'media/' + LocalStorage.getItem('openid') + '/')
  }
  autoUpdater.on('error', function (error) {
    sendUpdateMessage({
      cmd: 'error',
      message: error
    })
  })
  autoUpdater.on('checking-for-update', function () {
    sendUpdateMessage({
      cmd: 'checking-for-update',
      message: 'checking-for-update'
    })
  })
  autoUpdater.on('update-available', function (info) {
    sendUpdateMessage({
      cmd: 'update-available',
      message: info
    })
  })
  autoUpdater.on('update-not-available', function () {
    sendUpdateMessage({
      cmd: 'update-not-available',
      message: 'update-not-available'
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
        releaseNotes,
        releaseName,
        releaseDate,
        updateUrl
      }
    })
  })
  ipcMain.on('checkForUpdate', (e, arg) => {
    autoUpdater.checkForUpdates()
  })
  ipcMain.on('downloadUpdate', (e, arg) => {
    autoUpdater.downloadUpdate()
  })
  ipcMain.on('updateNow', (e, arg) => {
    autoUpdater.quitAndInstall()
  })
}

function sendUpdateMessage (text) {
  mainWindow.webContents.send('message', text)
}
