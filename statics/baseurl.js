import axios from 'axios'
import Vue from 'vue'

const baseurl = 'http://127.0.0.1:8000/'
const axiosInstance = axios.create({
  baseURL: baseurl,
  timeout: 5000
})

Vue.prototype.$axios = axiosInstance

export { baseurl }
