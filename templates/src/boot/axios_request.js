import Vue from 'vue'
import axios from 'axios'
import { SessionStorage, LocalStorage, Notify, Loading } from 'quasar'
import { i18n } from './i18n'
import Bus from './bus.js'

function getBaseUrl (name) {
  const xhr = new XMLHttpRequest()
  const okStatus = document.location.protocol === 'file:' ? 0 : 200
  xhr.open('GET', '../../statics/' + name, false)
  xhr.overrideMimeType('text/html; charset=utf-8')
  xhr.send(null)
  return xhr.status === okStatus ? xhr.responseText : null
}

const baseurl = getBaseUrl('baseurl.txt')

const axiosInstance = axios.create({
  baseURL: baseurl,
})

const axiosInstanceVersion = axios.create({
  baseURL: baseurl,
})

const axiosInstanceAuth = axios.create({
  baseURL: baseurl,
})

const axiosInstanceAuthScan = axios.create({
  baseURL: baseurl,
})

var lang = LocalStorage.getItem('lang')
if (LocalStorage.has('lang')) {
  lang = lang || 'en-US'
} else {
  LocalStorage.set('lang', 'en-US')
  lang = 'en-US'
}

const axiosFile = axios.create({
  baseURL: baseurl,
})

axiosInstanceAuth.interceptors.request.use(
  function (config) {
    const auth = LocalStorage.getItem('auth')
    const login = SessionStorage.getItem('axios_check')
    if (auth || login) {
      config.headers.post['Content-Type'] = 'application/json, charset="utf-8"'
      config.headers.patch['Content-Type'] = 'application/json, charset="utf-8"'
      config.headers.put['Content-Type'] = 'application/json, charset="utf-8"'
      config.headers.token = LocalStorage.getItem('openid')
      config.headers.operator = LocalStorage.getItem('login_id')
      config.headers.language = lang
      if (config.method === 'post' || config.method === 'patch' || config.method === 'put' || config.method === 'delete') {
        Loading.show()
      }
      return config
    } else {
      Loading.hide()
      Bus.$emit('needLogin', true)
    }
  },
  function (error) {
    Loading.hide()
    return Promise.reject(error)
  }
)

axiosInstanceAuth.interceptors.response.use(
  function (response) {
    if (response.data.detail) {
      if (response.data.detail !== 'success') {
        Notify.create({
          message: response.data.detail,
          icon: 'close',
          color: 'negative',
          timeout: 1500
        })
      }
    }
    if (response.data.results) {
      var sslcheck = baseurl.split(':')
      if (response.data.next !== null) {
        if (sslcheck.length === 2) {
          var nextlinkcheck = (response.data.next).toString().split(sslcheck[1])
          response.data.next = nextlinkcheck[1]
        } else {
          var nextlinkcheck1 = (response.data.next).toString().split(sslcheck[1] + ':' + sslcheck[2])
          response.data.next = nextlinkcheck1[1]
        }
      } else {
        response.data.next = null
      }
      if (response.data.previous !== null) {
        if (sslcheck.length === 2) {
          var previouslinkcheck = (response.data.previous).toString().split(sslcheck[1])
          response.data.previous = previouslinkcheck[1]
        } else {
          var previouslinkcheck1 = (response.data.previous).toString().split(sslcheck[1] + ':' + sslcheck[2])
          response.data.previous = previouslinkcheck1[1]
        }
      } else {
        response.data.previous = null
      }
      Loading.hide()
      return response.data
    }
    Loading.hide()
    return response.data
  },
  function (error) {
    const defaultNotify = {
      message: i18n.t('notice.unknow_error'),
      icon: 'close',
      color: 'negative',
      timeout: 1500
    }
    if (error.code === 'ECONNABORTED' || error.message.indexOf('timeout') !== -1 || error.message === 'Network Error') {
      defaultNotify.message = i18n.t('notice.network_error')
      Notify.create(defaultNotify)
      Loading.hide()
      return Promise.reject(error)
    }
    switch (error.response.status) {
      case 400:
        defaultNotify.message = i18n.t('notice.400')
        Notify.create(defaultNotify)
        break
      case 401:
        defaultNotify.message = i18n.t('notice.401')
        Notify.create(defaultNotify)
        break
      case 403:
        defaultNotify.message = i18n.t('notice.403')
        Notify.create(defaultNotify)
        break
      case 404:
        defaultNotify.message = i18n.t('notice.404')
        Notify.create(defaultNotify)
        break
      case 405:
        defaultNotify.message = i18n.t('notice.405')
        Notify.create(defaultNotify)
        break
      case 408:
        defaultNotify.message = i18n.t('notice.408')
        Notify.create(defaultNotify)
        break
      case 409:
        defaultNotify.message = i18n.t('notice.409')
        Notify.create(defaultNotify)
        break
      case 410:
        defaultNotify.message = i18n.t('notice.410')
        Notify.create(defaultNotify)
        break
      case 500:
        defaultNotify.message = i18n.t('notice.500')
        Notify.create(defaultNotify)
        break
      case 501:
        defaultNotify.message = i18n.t('notice.501')
        Notify.create(defaultNotify)
        break
      case 502:
        defaultNotify.message = i18n.t('notice.502')
        Notify.create(defaultNotify)
        break
      case 503:
        defaultNotify.message = i18n.t('notice.503')
        Notify.create(defaultNotify)
        break
      case 504:
        defaultNotify.message = i18n.t('notice.504')
        Notify.create(defaultNotify)
        break
      case 505:
        defaultNotify.message = i18n.t('notice.505')
        Notify.create(defaultNotify)
        break
      default:
        Notify.create(defaultNotify)
        break
    }
    Loading.hide()
    return Promise.reject(error)
  }
)

axiosInstanceAuthScan.interceptors.request.use(
  function (config) {
    const auth = LocalStorage.getItem('auth')
    const login = SessionStorage.getItem('axios_check')
    if (auth || login) {
      config.headers.post['Content-Type'] = 'application/json, charset="utf-8"'
      config.headers.patch['Content-Type'] = 'application/json, charset="utf-8"'
      config.headers.put['Content-Type'] = 'application/json, charset="utf-8"'
      config.headers.token = LocalStorage.getItem('openid')
      config.headers.operator = LocalStorage.getItem('login_id')
      config.headers.language = lang
      if (config.method === 'post' || config.method === 'patch' || config.method === 'put' || config.method === 'delete') {
        Loading.show()
      }
      return config
    } else {
      Loading.hide()
      Bus.$emit('needLogin', true)
    }
  },
  function (error) {
    Loading.hide()
    return Promise.reject(error)
  }
)

axiosInstanceAuthScan.interceptors.response.use(
  function (response) {
    if (response.data.results) {
      var sslcheck = baseurl.split(':')
      if (response.data.next !== null) {
        if (sslcheck.length === 2) {
          var nextlinkcheck = (response.data.next).toString().split(sslcheck[1])
          response.data.next = nextlinkcheck[1]
        } else {
          var nextlinkcheck1 = (response.data.next).toString().split(sslcheck[1] + ':' + sslcheck[2])
          response.data.next = nextlinkcheck1[1]
        }
      } else {
        response.data.next = null
      }
      if (response.data.previous !== null) {
        if (sslcheck.length === 2) {
          var previouslinkcheck = (response.data.previous).toString().split(sslcheck[1])
          response.data.previous = previouslinkcheck[1]
        } else {
          var previouslinkcheck1 = (response.data.previous).toString().split(sslcheck[1] + ':' + sslcheck[2])
          response.data.previous = previouslinkcheck1[1]
        }
      } else {
        response.data.previous = null
      }
      Loading.hide()
      return response.data
    }
    Loading.hide()
    return response.data
  },
  function (error) {
    const defaultNotify = {
      message: i18n.t('notice.unknow_error'),
      icon: 'close',
      color: 'negative',
      timeout: 1500
    }
    if (error.code === 'ECONNABORTED' || error.message.indexOf('timeout') !== -1 || error.message === 'Network Error') {
      defaultNotify.message = i18n.t('notice.network_error')
      Notify.create(defaultNotify)
      Loading.hide()
      return Promise.reject(error)
    }
    switch (error.response.status) {
      case 400:
        defaultNotify.message = i18n.t('notice.400')
        Notify.create(defaultNotify)
        break
      case 401:
        defaultNotify.message = i18n.t('notice.401')
        Notify.create(defaultNotify)
        break
      case 403:
        defaultNotify.message = i18n.t('notice.403')
        Notify.create(defaultNotify)
        break
      case 404:
        defaultNotify.message = i18n.t('notice.404')
        Notify.create(defaultNotify)
        break
      case 405:
        defaultNotify.message = i18n.t('notice.405')
        Notify.create(defaultNotify)
        break
      case 408:
        defaultNotify.message = i18n.t('notice.408')
        Notify.create(defaultNotify)
        break
      case 409:
        defaultNotify.message = i18n.t('notice.409')
        Notify.create(defaultNotify)
        break
      case 410:
        defaultNotify.message = i18n.t('notice.410')
        Notify.create(defaultNotify)
        break
      case 500:
        defaultNotify.message = i18n.t('notice.500')
        Notify.create(defaultNotify)
        break
      case 501:
        defaultNotify.message = i18n.t('notice.501')
        Notify.create(defaultNotify)
        break
      case 502:
        defaultNotify.message = i18n.t('notice.502')
        Notify.create(defaultNotify)
        break
      case 503:
        defaultNotify.message = i18n.t('notice.503')
        Notify.create(defaultNotify)
        break
      case 504:
        defaultNotify.message = i18n.t('notice.504')
        Notify.create(defaultNotify)
        break
      case 505:
        defaultNotify.message = i18n.t('notice.505')
        Notify.create(defaultNotify)
        break
      default:
        Notify.create(defaultNotify)
        break
    }
    Loading.hide()
    return Promise.reject(error)
  }
)

axiosInstance.interceptors.request.use(
  function (config) {
    config.headers.post['Content-Type'] = 'application/json, charset="utf-8"'
    config.headers.language = lang
    if (config.method === 'post' || config.method === 'patch' || config.method === 'put' || config.method === 'delete') {
        Loading.show()
      }
    return config
  },
  function (error) {
    Loading.hide()
    return Promise.reject(error)
  }
)

axiosInstance.interceptors.response.use(
  function (response) {
    if (response.data.detail) {
      if (response.data.detail !== 'success') {
        Notify.create({
          message: response.data.detail,
          icon: 'close',
          color: 'negative',
          timeout: 1500
        })
      }
    }
    Loading.hide()
    return response.data
  },
  function (error) {
    const defaultNotify = {
      message: i18n.t('notice.network_error'),
      icon: 'close',
      color: 'negative',
      timeout: 1500
    }
    if (error.code === 'ECONNABORTED' || error.message.indexOf('timeout') !== -1 || error.message === 'Network Error') {
      defaultNotify.message = i18n.t('notice.network_error')
      Notify.create(defaultNotify)
      Loading.hide()
      return Promise.reject(error)
    }
    switch (error.response.status) {
      case 400:
        defaultNotify.message = i18n.t('notice.400')
        Notify.create(defaultNotify)
        break
      case 401:
        defaultNotify.message = i18n.t('notice.401')
        Notify.create(defaultNotify)
        break
      case 403:
        defaultNotify.message = i18n.t('notice.403')
        Notify.create(defaultNotify)
        break
      case 404:
        defaultNotify.message = i18n.t('notice.404')
        Notify.create(defaultNotify)
        break
      case 405:
        defaultNotify.message = i18n.t('notice.405')
        Notify.create(defaultNotify)
        break
      case 408:
        defaultNotify.message = i18n.t('notice.408')
        Notify.create(defaultNotify)
        break
      case 409:
        defaultNotify.message = i18n.t('notice.409')
        Notify.create(defaultNotify)
        break
      case 410:
        defaultNotify.message = i18n.t('notice.410')
        Notify.create(defaultNotify)
        break
      case 500:
        defaultNotify.message = i18n.t('notice.500')
        Notify.create(defaultNotify)
        break
      case 501:
        defaultNotify.message = i18n.t('notice.501')
        Notify.create(defaultNotify)
        break
      case 502:
        defaultNotify.message = i18n.t('notice.502')
        Notify.create(defaultNotify)
        break
      case 503:
        defaultNotify.message = i18n.t('notice.503')
        Notify.create(defaultNotify)
        break
      case 504:
        defaultNotify.message = i18n.t('notice.504')
        Notify.create(defaultNotify)
        break
      case 505:
        defaultNotify.message = i18n.t('notice.505')
        Notify.create(defaultNotify)
        break
      default:
        Notify.create(defaultNotify)
        break
    }
    Loading.hide()
    return Promise.reject(error)
  }
)

axiosInstanceVersion.interceptors.request.use(
  function (config) {
    const auth = LocalStorage.getItem('auth')
    const login = SessionStorage.getItem('axios_check')
    if (auth || login) {
      if (config.method === 'post' || config.method === 'patch' || config.method === 'put' || config.method === 'delete') {
        Loading.show()
      }
      return config
    } else {
      Loading.hide()
      Bus.$emit('needLogin', true)
    }
  },
  function (error) {
    Loading.hide()
    return Promise.reject(error)
  }
)

axiosInstanceVersion.interceptors.response.use(
  function (response) {
    Loading.hide()
    return response.data
  },
  function (error) {
    Loading.hide()
    return Promise.reject(error)
  }
)

axiosFile.interceptors.request.use(
  function (config) {
    const auth = LocalStorage.getItem('auth')
    const login = SessionStorage.getItem('axios_check')
    if (auth || login) {
      config.headers.get['Content-Type'] = 'application/vnd.ms-excel'
      config.headers.token = LocalStorage.getItem('openid')
      config.headers.operator = LocalStorage.getItem('login_id')
      config.headers.language = lang
      if (config.method === 'post' || config.method === 'patch' || config.method === 'put' || config.method === 'delete') {
        Loading.show()
      }
      return config
    } else {
      Loading.hide()
      Bus.$emit('needLogin', true)
    }
  },
  function (error) {
    Loading.hide()
    return Promise.reject(error)
  }
)

axiosFile.interceptors.response.use(
  function (response) {
    if (response.data.detail) {
      if (response.data.detail !== 'success') {
        Notify.create({
          message: response.data.detail,
          icon: 'close',
          color: 'negative',
          timeout: 1500
        })
      }
    }
    Loading.hide()
    return response
  },
  function (error) {
    const defaultNotify = {
      message: i18n.t('notice.network_error'),
      icon: 'close',
      color: 'negative',
      timeout: 1500
    }
    if (error.code === 'ECONNABORTED' || error.message.indexOf('timeout') !== -1 || error.message === 'Network Error') {
      defaultNotify.message = i18n.t('notice.network_error')
      Notify.create(defaultNotify)
      Loading.hide()
      return Promise.reject(error)
    }
    switch (error.response.status) {
      case 400:
        defaultNotify.message = i18n.t('notice.400')
        Notify.create(defaultNotify)
        break
      case 401:
        defaultNotify.message = i18n.t('notice.401')
        Notify.create(defaultNotify)
        break
      case 403:
        defaultNotify.message = i18n.t('notice.403')
        Notify.create(defaultNotify)
        break
      case 404:
        defaultNotify.message = i18n.t('notice.404')
        Notify.create(defaultNotify)
        break
      case 405:
        defaultNotify.message = i18n.t('notice.405')
        Notify.create(defaultNotify)
        break
      case 408:
        defaultNotify.message = i18n.t('notice.408')
        Notify.create(defaultNotify)
        break
      case 409:
        defaultNotify.message = i18n.t('notice.409')
        Notify.create(defaultNotify)
        break
      case 410:
        defaultNotify.message = i18n.t('notice.410')
        Notify.create(defaultNotify)
        break
      case 500:
        defaultNotify.message = i18n.t('notice.500')
        Notify.create(defaultNotify)
        break
      case 501:
        defaultNotify.message = i18n.t('notice.501')
        Notify.create(defaultNotify)
        break
      case 502:
        defaultNotify.message = i18n.t('notice.502')
        Notify.create(defaultNotify)
        break
      case 503:
        defaultNotify.message = i18n.t('notice.503')
        Notify.create(defaultNotify)
        break
      case 504:
        defaultNotify.message = i18n.t('notice.504')
        Notify.create(defaultNotify)
        break
      case 505:
        defaultNotify.message = i18n.t('notice.505')
        Notify.create(defaultNotify)
        break
      default:
        Notify.create(defaultNotify)
        break
    }
    Loading.hide()
    return Promise.reject(error)
  }
)

function getauth (url) {
  return axiosInstanceAuth.get(url)
}

function get (url) {
  return axiosInstance.get(url)
}

function versioncheck (url) {
  return axiosInstanceVersion.get(url)
}

function post (url, data) {
  return axiosInstance.post(url, data)
}

function postauth (url, data) {
  return axiosInstanceAuth.post(url, data)
}

function putauth (url, data) {
  return axiosInstanceAuth.put(url, data)
}

function patchauth (url, data) {
  return axiosInstanceAuth.patch(url, data)
}

function deleteauth (url) {
  return axiosInstanceAuth.delete(url)
}

function ViewPrintAuth (url) {
  return axiosInstanceAuth.get(url)
}

function scangetauth (url) {
  return axiosInstanceAuthScan.get(url)
}

function scanpostauth (url, data) {
  return axiosInstanceAuthScan.post(url, data)
}

function getfile (url) {
  return axiosFile.get(url)
}

Vue.prototype.$axios = axios

export { baseurl, get, versioncheck, post, getauth, postauth, putauth, deleteauth, patchauth, ViewPrintAuth, getfile, scangetauth, scanpostauth }
