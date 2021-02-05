import { autoUpdater } from 'electron-updater'
import { ipcMain } from 'electron'
import { baseurl } from '../../src/boot/axios_request'

let mainWindow = null

export function updateHandle (window) {
  mainWindow = window
  autoUpdater.autoDownload = false
  autoUpdater.setFeedURL(baseurl + 'media/')
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
