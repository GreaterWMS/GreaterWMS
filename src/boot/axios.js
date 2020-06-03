import Vue from 'vue'
import axios from 'axios'
import { LocalStorage } from 'quasar'

const baseurl = 'https://scmapi.56yhz.com/'
const axiosInstance = axios.create({
  baseURL: baseurl,
  timeout: 5000
})

const axiosInstancelogin = axios.create({
  baseURL: baseurl,
  timeout: 5000
})

const axiosInstanceAuth = axios.create({
  baseURL: baseurl,
  timeout: 5000
})

const axiosInstanceDelete = axios.create({
  baseURL: baseurl,
  timeout: 5000
})

axiosInstanceAuth.interceptors.request.use(
  function (config) {
    return config
  },
  function (error) {
    return Promise.reject(error)
  }
)

axiosInstanceAuth.interceptors.response.use(
  function (response) {
    return response
  },
  function (error) {
    return Promise.reject(error)
  }
)

axiosInstancelogin.interceptors.request.use(
  function (config) {
    const authid = LocalStorage.getItem('authid')
    config.params = { openid: authid }
    return config
  },
  function (error) {
    return Promise.reject(error)
  }
)

axiosInstancelogin.interceptors.response.use(
  function (response) {
    return response
  },
  function (error) {
    return Promise.reject(error)
  }
)

axiosInstance.interceptors.request.use(
  function (config) {
    return config
  },
  function (error) {
    return Promise.reject(error)
  }
)

axiosInstance.interceptors.response.use(
  function (response) {
    return response
  },
  function (error) {
    return Promise.reject(error)
  }
)

axiosInstanceDelete.interceptors.request.use(
  function (config) {
    const openid = LocalStorage.getItem('openid')
    config.params = { openid: openid }
    return config
  },
  function (error) {
    return Promise.reject(error)
  }
)

axiosInstanceDelete.interceptors.response.use(
  function (response) {
    return response
  },
  function (error) {
    return Promise.reject(error)
  }
)

function get (url, params) {
  return axiosInstance.get(url, { params })
}

function post (url, params, data) {
  return axiosInstance.post(url, data, { params })
}

function postlogin (url, data) {
  return axiosInstancelogin.post(url, data)
}

function postauth (url, data) {
  return axiosInstanceAuth.post(url, data)
}

function patch (url, params, data) {
  return axiosInstance.patch(url, data, { params })
}

function del (url, params, data) {
  return axiosInstanceDelete.delete(url, data, {
    params
  })
}

Vue.prototype.$axios = axiosInstance

export { get, post, patch, del, postlogin, postauth }
