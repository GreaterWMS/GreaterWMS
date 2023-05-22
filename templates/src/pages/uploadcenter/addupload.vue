<template>
  <div class="shadow-24 q-pa-md" :style="{ height: height, background: 'white',borderRadius: '4px' }">
    <q-btn-group push>
      <q-btn :label="$t('upload_center.downloadgoodstemplate')" icon="cloud_download" @click="downloadgoodstemplate()">
        <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('upload_center.downloadgoodstemplate') }}</q-tooltip>
      </q-btn>
      <q-btn :label="$t('upload_center.downloadcustomertemplate')" icon="cloud_download" @click="downloadcustomertemplate()">
        <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('upload_center.downloadcustomertemplate') }}</q-tooltip>
      </q-btn>
      <q-btn :label="$t('upload_center.downloadsuppliertemplate')" icon="cloud_download" @click="downloadsuppliertemplate()">
        <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('upload_center.downloadsuppliertemplate') }}</q-tooltip>
      </q-btn>
    </q-btn-group>
    <div style="display: flex;">
      <div class="q-pt-md q-gutter-md row items-start">
        <q-uploader
          style="width:300px;height:200px"
          :url="goodslistfile_pathname"
          method="post"
          :headers="[{ name: 'token', value: token }, { name: 'language', value: lang }, { name: 'operator', value: login_id }]"
          :field-name="file => 'file'"
          :label="$t('upload_center.uploadgoodslistfile')"
          accept=".xlsx,csv,xls/*"
          @rejected="onRejected"
          @added="getfileinfo"
        />
      </div>

      <div class="q-pa-md q-gutter-md row items-start">
        <q-uploader
          style="width:300px;height:200px"
          :url="customerfile_pathname"
          method="post"
          :headers="[{ name: 'token', value: token }, { name: 'language', value: lang }, { name: 'operator', value: login_id }]"
          :field-name="file => 'file'"
          :label="$t('upload_center.uploadcustomerfile')"
          accept=".xlsx,csv,xls/*"
          @rejected="onRejected"
          @added="getfileinfo"
        />
      </div>

      <div class="q-pt-md q-gutter-md row items-start">
        <q-uploader
          style="width:300px;height:200px"
          :url="supplierfile_pathname"
          method="post"
          :headers="[{ name: 'token', value: token }, { name: 'language', value: lang }, { name: 'operator', value: login_id }]"
          :field-name="file => 'file'"
          :label="$t('upload_center.uploadsupplierfile')"
          accept=".xlsx,csv,xls/*"
          @rejected="onRejected"
          @added="getfileinfo"
        />
      </div>
    </div>
  </div>
</template>
<router-view />

<script>
import { baseurl } from 'boot/axios_request';
import { LocalStorage, openURL } from 'quasar';

export default {
  name: 'Pageaddupload',
  data() {
    return {
      height: '',
      token: LocalStorage.getItem('openid'),
      lang: LocalStorage.getItem('lang'),
      login_id: LocalStorage.getItem('login_id'),
      capitalfile_pathname: baseurl + '/uploadfile/capitalfileadd/',
      customerfile_pathname: baseurl + '/uploadfile/customerfileadd/',
      freightfile_pathname: baseurl + '/uploadfile/freightfileadd/',
      goodslistfile_pathname: baseurl + '/uploadfile/goodslistfileadd/',
      supplierfile_pathname: baseurl + '/uploadfile/supplierfileadd/'
    };
  },
  methods: {
    checkFileType(files) {
      return files.filter(file => file.type === '.xlsx, xls,csv/*');
    },
    onRejected(rejectedEntries) {
      this.$q.notify({
        type: 'negative',
        message: `${rejectedEntries.length} file(s) did not pass validation constraints`
      });
    },
    getfileinfo(files) {
      console.log(1, files);
    },
    downloadgoodstemplate() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        if (LocalStorage.has('lang')) {
          if (LocalStorage.getItem('lang') === 'zh-hans') {
            openURL(baseurl + '/media/upload_example/goodslist_cn.xlsx');
          } else {
            openURL(baseurl + '/media/upload_example/goodslist_en.xlsx');
          }
        } else {
          openURL(baseurl + '/media/upload_example/goodslist_en.xlsx');
        }
      } else {
        _this.$q.notify({
          message: _this.$t('notice.loginerror'),
          color: 'negative',
          icon: 'warning'
        });
      }
    },
    downloadcustomertemplate() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        if (LocalStorage.has('lang')) {
          if (LocalStorage.getItem('lang') === 'zh-hans') {
            openURL(baseurl + '/media/upload_example/customer_cn.xlsx');
          } else {
            openURL(baseurl + '/media/upload_example/customer_en.xlsx');
          }
        } else {
          openURL(baseurl + '/media/upload_example/customer_en.xlsx');
        }
      } else {
        _this.$q.notify({
          message: _this.$t('notice.loginerror'),
          color: 'negative',
          icon: 'warning'
        });
      }
    },
    downloadsuppliertemplate() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        if (LocalStorage.has('lang')) {
          if (LocalStorage.getItem('lang') === 'zh-hans') {
            openURL(baseurl + '/media/upload_example/supplier_cn.xlsx');
          } else {
            openURL(baseurl + '/media/upload_example/supplier_en.xlsx');
          }
        } else {
          openURL(baseurl + '/media/upload_example/supplier_en.xlsx');
        }
      } else {
        _this.$q.notify({
          message: _this.$t('notice.loginerror'),
          color: 'negative',
          icon: 'warning'
        });
      }
    }
  },
  mounted() {
    var _this = this;
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height - 185) + 'px';
    } else {
      _this.height = _this.$q.screen.height - 185 + '' + 'px';
    }
  },
  updated() {},
  destroyed() {}
};
</script>
