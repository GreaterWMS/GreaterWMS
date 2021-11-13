<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-column-table shadow-24"
        row-key="id"
        :table-style="{ height: height }"
        flat
        hide-bottom
      >
        <template v-slot:top>
          <div class="q-pa-md">
            <div>
              <div class="row">
                <q-btn-group>
                  <q-btn :label="$t('upload_center.downloadgoodstemplate')" icon="cloud_download" @click="downloadgoodstemplate()">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                      {{ $t('upload_center.downloadgoodstemplate') }}
                    </q-tooltip>
                  </q-btn>
                  <q-btn :label="$t('upload_center.downloadcustomertemplate')" icon="cloud_download" @click="downloadcustomertemplate()">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                      {{ $t('upload_center.downloadcustomertemplate') }}
                    </q-tooltip>
                  </q-btn>
                  <q-btn :label="$t('upload_center.downloadsuppliertemplate')" icon="cloud_download" @click="downloadsuppliertemplate()">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                      {{ $t('upload_center.downloadsuppliertemplate') }}
                    </q-tooltip>
                  </q-btn>
                </q-btn-group>
              </div>
              <q-tr>
                <q-td key="uploadgoodslistfile">
                  <div class="q-pa-md">
                    <div class="q-gutter-md row items-start">
                      <q-uploader
                        style="width:300px;height:200px"
                        :url = goodslistfile_pathname
                        method="post"
                        :headers="[{name:'token',value:token}, {name: 'language', value: lang}]"
                        :field-name="(file)=>file"
                        :label="$t('upload_center.uploadgoodslistfile')"
                        accept=".xlsx,csv,xls/*"
                        @rejected="onRejected"
                        @added="getfileinfo"
                      />
                    </div>
                  </div>
                </q-td>
                <q-td key="uploadcustomerfile">
                  <div class="q-pa-md">
                    <div class="q-gutter-md row items-start">
                      <q-uploader
                        style="width:300px;height:200px"
                        :url = customerfile_pathname
                        method="post"
                        :headers="[{name: 'token',value: token}, {name: 'language', value: lang}]"
                        :field-name="(file)=>'file'"
                        :label="$t('upload_center.uploadcustomerfile')"
                        accept=".xlsx,csv,xls/*"
                        @rejected="onRejected"
                        @added="getfileinfo"
                      />
                    </div>
                  </div>
                </q-td>
                <q-td key="uploadsupplierfile">
                  <div class="q-pa-md">
                    <div class="q-gutter-md row items-start">
                      <q-uploader
                        style="width:300px;height:200px"
                        :url = supplierfile_pathname
                        method="post"
                        :headers="[{name:'token',value:token}, {name: 'language', value: lang}]"
                        :field-name="(file)=>file"
                        :label="$t('upload_center.uploadsupplierfile')"
                        accept=".xlsx,csv,xls/*"
                        @rejected="onRejected"
                        @added="getfileinfo"
                      />
                    </div>
                  </div>
                </q-td>
              </q-tr>
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
import { LocalStorage, openURL } from 'quasar'

export default {
  name: 'Pageaddupload',
  data () {
    return {
      height: '',
      token: LocalStorage.getItem('openid'),
      lang: LocalStorage.getItem('lang'),
      capitalfile_pathname: baseurl + 'uploadfile/capitalfileadd/',
      customerfile_pathname: baseurl + 'uploadfile/customerfileadd/',
      freightfile_pathname: baseurl + 'uploadfile/freightfileadd/',
      goodslistfile_pathname: baseurl + 'uploadfile/goodslistfileadd/',
      supplierfile_pathname: baseurl + 'uploadfile/supplierfileadd/'
    }
  },
  methods: {
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
    },
    downloadgoodstemplate () {
      if (LocalStorage.has('lang')) {
        if (LocalStorage.getItem('lang') === 'zh-hans') {
          openURL(baseurl + 'media/upload_example/goodslist_cn.xlsx')
        } else {
          openURL(baseurl + 'media/upload_example/goodslist_en.xlsx')
        }
      } else {
        openURL(baseurl + 'media/upload_example/goodslist_en.xlsx')
      }
    },
    downloadcustomertemplate () {
      if (LocalStorage.has('lang')) {
        if (LocalStorage.getItem('lang') === 'zh-hans') {
          openURL(baseurl + 'media/upload_example/customer_cn.xlsx')
        } else {
          openURL(baseurl + 'media/upload_example/customer_en.xlsx')
        }
      } else {
        openURL(baseurl + 'media/upload_example/customer_en.xlsx')
      }
    },
    downloadsuppliertemplate () {
      if (LocalStorage.has('lang')) {
        if (LocalStorage.getItem('lang') === 'zh-hans') {
          openURL(baseurl + 'media/upload_example/supplier_cn.xlsx')
        } else {
          openURL(baseurl + 'media/upload_example/supplier_en.xlsx')
        }
      } else {
        openURL(baseurl + 'media/upload_example/supplier_en.xlsx')
      }
    }
  },
  mounted () {
    var _this = this
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height - 480) + 'px'
    } else {
      _this.height = _this.$q.screen.height - 480 + '' + 'px'
    }
  },
  updated () {
  },
  destroyed () {
  }
}
</script>
