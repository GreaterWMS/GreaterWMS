import Vue from 'vue'
import axios from 'axios'
import { LocalStorage } from 'quasar'

const baseurl = 'http://127.0.0.1:8000/'
const wsurl = 'ws://127.0.0.1:8000/'

const axiosInstance = axios.create({
  baseURL: baseurl,
  timeout: 5000
})

const axiosInstanceAuth = axios.create({
  baseURL: baseurl,
  timeout: 5000
})

axiosInstanceAuth.interceptors.request.use(
  function (config) {
    config.headers.post['Content-Type'] = 'application/json, charset="utf-8"'
    config.headers.patch['Content-Type'] = 'application/json, charset="utf-8"'
    config.headers.put['Content-Type'] = 'application/json, charset="utf-8"'
    config.headers.token = LocalStorage.getItem('openid')
    return config
  },
  function (error) {
    return Promise.reject(error)
  }
)

axiosInstanceAuth.interceptors.response.use(
  function (response) {
    return response.data
  },
  function (error) {
    return Promise.reject(error)
  }
)

axiosInstance.interceptors.request.use(
  function (config) {
    config.headers.post['Content-Type'] = 'application/json, charset="utf-8"'
    return config
  },
  function (error) {
    return Promise.reject(error)
  }
)

axiosInstance.interceptors.response.use(
  function (response) {
    return response.data
  },
  function (error) {
    return Promise.reject(error)
  }
)

function getauth (url) {
  return axiosInstanceAuth.get(url)
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

Vue.prototype.$axios = axios

export { baseurl, wsurl, post, getauth, postauth, putauth, deleteauth, patchauth, ViewPrintAuth }
