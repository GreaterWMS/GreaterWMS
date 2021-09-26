<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-column-table shadow-24"
        row-key="id"
        :table-style="{ height: height }"
        flat
      >
        <template v-slot:top>
          <div class="q-pa-md">
            <div class="q-gutter-md row items-start">
              <q-uploader
                style="width:300px;height:200px"
                :url = capitalfile_pathname
                :label="$t('upload_center.uploadcapitalfile') + '  ' + '(for <10M size)'"
                accept=".csv, xlsx,xls/*"
                :filter="checkFileSize"
                @rejected="onRejected"
                @added="getfileinfo"
              />
            </div>
          </div>
          <div class="q-pa-md">
            <div class="q-gutter-md row items-start">
              <q-uploader
                style="width:300px;height:200px"
                :url = customerfile_pathname
                :label="$t('upload_center.uploadcustomerfile') + '  ' + '(for <10M size)'"
                accept=".csv, xlsx,xls/*"
                :filter="checkFileSize"
                @rejected="onRejected"
                @added="getfileinfo"
              />
            </div>
          </div>
          <div class="q-pa-md">
            <div class="q-gutter-md row items-start">
              <q-uploader
                style="width:300px;height:200px"
                :url = freightfile_pathname
                :label="$t('upload_center.uploadfreightfile') + '  ' + '(for <10M size)'"
                accept=".csv, xlsx,xls/*"
                :filter="checkFileSize"
                @rejected="onRejected"
                @added="getfileinfo"
              />
            </div>
          </div>
          <div class="q-pa-md">
            <div class="q-gutter-md row items-start">
              <q-uploader
                style="width:300px;height:200px"
                :url = goodslistfile_pathname
                :label="$t('upload_center.uploadgoodslistfile') + '  ' + '(for <10M size)'"
                accept=".csv, xlsx,xls/*"
                :filter="checkFileSize"
                @rejected="onRejected"
                @added="getfileinfo"
              />
            </div>
          </div>
          <div class="q-pa-md">
            <div class="q-gutter-md row items-start">
              <q-uploader
                style="width:300px;height:200px"
                :url = supplierfile_pathname
                :label="$t('upload_center.uploadsupplierfile') + '  ' + '(for <10M size)'"
                accept=".csv, xlsx,xls/*"
                :filter="checkFileSize"
                @rejected="onRejected"
                @added="getfileinfo"
              />
            </div>
          </div>
        </template>
      </q-table>
    </transition>
  </div>
</template>
<router-view />

<script>
import { baseurl } from 'boot/axios_request'
export default {
  name: 'Pagecapital',
  data () {
    return {
      height: '',
      capitalfile_pathname: baseurl + 'uploadfile/capitalfile/',
      customerfile_pathname: baseurl + 'uploadfile/customerfile/',
      freightfile_pathname: baseurl + 'uploadfile/freightfile/',
      goodslistfile_pathname: baseurl + 'uploadfile/goodslistfile/',
      supplierfile_pathname: baseurl + 'uploadfile/supplierfile/'
    }
  },
  methods: {
    checkFileSize (files) {
      return files.filter(file => file.size < 10485760)
    },
    checkFileType (files) {
      return files.filter(file => file.type === '.xlsx, xls,csv/*')
    },
    onRejected (rejectedEntries) {
      this.$q.notify({
        type: 'negative',
        message: `${rejectedEntries.length} file(s) did not pass validation constraints`
      })
    },
    getfileinfo (files) {
      console.log(files)
    }
  },
  mounted () {
    var _this = this
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height - 260) + 'px'
    } else {
      _this.height = _this.$q.screen.height - 260 + '' + 'px'
    }
  },
  updated () {
  },
  destroyed () {
  }
}
</script>
