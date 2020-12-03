<template>
<div class="q-pa-md">
     <q-uploader
            :url="property"
            label="选择文件"
            color="purple"
            square
            flat
            bordered
            auto-upload
            method="put"
            :field-name="(file) => 'file'"
            @finish="successUpload()"
            @failed="failUpload()"
            style="max-width: 100%"
           >
             <template v-slot:header="scope">
        <div class="row no-wrap items-center q-pa-sm q-gutter-xs">
          <q-btn v-if="scope.queuedFiles.length > 0" icon="clear_all" @click="scope.removeQueuedFiles" round dense flat >
            <q-tooltip>移除所有上传的文件</q-tooltip>
          </q-btn>
          <q-btn v-if="scope.uploadedFiles.length > 0" icon="done_all" @click="scope.removeUploadedFiles" round dense flat >
            <q-tooltip>移除上传的文件</q-tooltip>
          </q-btn>
          <q-spinner v-if="scope.isUploading" class="q-uploader__spinner" />
          <div class="col">
            <div class="q-uploader__title">上传库位属性</div>
            <div class="q-uploader__subtitle">{{ scope.uploadSizeLabel }} / {{ scope.uploadProgressLabel }}</div>
          </div>
          <q-btn v-if="scope.canAddFiles" type="a" icon="add_box" round dense flat>
            <q-uploader-add-trigger />
            <q-tooltip>选择一个文件</q-tooltip>
          </q-btn>
          <q-btn v-if="scope.canUpload" icon="cloud_upload" @click="scope.upload" round dense flat >
            <q-tooltip>上传到服务器</q-tooltip>
          </q-btn>

          <q-btn v-if="scope.isUploading" icon="clear" @click="scope.abort" round dense flat >
            <q-tooltip>Abort Upload</q-tooltip>
          </q-btn>
        </div>
      </template>
           </q-uploader>
  <q-uploader
            :url="property"
            label="选择文件"
            color="purple"
            square
            flat
            bordered
            auto-upload
            method="put"
            :field-name="(file) => 'file'"
            @finish="successUpload()"
            @failed="failUpload()"
            style="max-width: 100%"
           >
             <template v-slot:header="scope">
        <div class="row no-wrap items-center q-pa-sm q-gutter-xs">
          <q-btn v-if="scope.queuedFiles.length > 0" icon="clear_all" @click="scope.removeQueuedFiles" round dense flat >
            <q-tooltip>移除所有上传的文件</q-tooltip>
          </q-btn>
          <q-btn v-if="scope.uploadedFiles.length > 0" icon="done_all" @click="scope.removeUploadedFiles" round dense flat >
            <q-tooltip>移除上传的文件</q-tooltip>
          </q-btn>
          <q-spinner v-if="scope.isUploading" class="q-uploader__spinner" />
          <div class="col">
            <div class="q-uploader__title">上传现有库存《文件小于1MB》</div>
            <div class="q-uploader__subtitle">{{ scope.uploadSizeLabel }} / {{ scope.uploadProgressLabel }}</div>
          </div>
          <q-btn v-if="scope.canAddFiles" type="a" icon="add_box" round dense flat>
            <q-uploader-add-trigger />
            <q-tooltip>选择一个文件</q-tooltip>
          </q-btn>
          <q-btn v-if="scope.canUpload" icon="cloud_upload" @click="scope.upload" round dense flat >
            <q-tooltip>上传到服务器</q-tooltip>
          </q-btn>

          <q-btn v-if="scope.isUploading" icon="clear" @click="scope.abort" round dense flat >
            <q-tooltip>Abort Upload</q-tooltip>
          </q-btn>
        </div>
      </template>
  </q-uploader>
  <template>
  <div class="q-pa-md">
      <v-distpicker province="广东省" city="广州市" area="海珠区" @selected='areaData'></v-distpicker>
  </div>
</template>
  </div>
</template>

<script>
import { baseurl } from 'boot/axios_request'
import VDistpicker from 'v-distpicker'
export default {
  name: 'PageIndex',
  // eslint-disable-next-line vue/no-unused-components
  components: { VDistpicker },
  data () {
    return {
      property: '',
      city: ''
    }
  },
  methods: {
    successUpload () {
      this.$q.notify({
        message: '上传成功',
        icon: 'check',
        color: 'positive',
        position: 'right',
        timeout: 1500
      })
    },
    failUpload () {
      this.$q.notify({
        message: '网络原因无法上传成功',
        icon: 'close',
        color: 'negative',
        position: 'right',
        timeout: 1500
      })
    },
    areaData (data) {
      this.city = data.province.value + ' ' + data.city.value + ' ' + data.area.value
    }
  },
  created () {
    this.property = baseurl + 'property/?openid=' + this.$q.localStorage.getItem('openid') + '&getfile=1'
  }
}
</script>
