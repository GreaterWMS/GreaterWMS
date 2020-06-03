<template>
    <q-page>

    <template>
    <div class="q-pa-md" style="width: 100%">
      <q-table
        title="Treats"
        dense
        :data="data"
        :columns="columns"
        row-key="name"
        :separator="separator"
        :loading="loading"
        hide-bottom
        :pagination.sync="pagination"
        no-data-label="没有找到任何数据"
        no-results-label="没有找到您想要的数据"
        :table-style="{ height: height }"
      >
         <template v-slot:top>
           <q-uploader
            :url="uploaded"
            label="选择文件"
            color="purple"
            square
            flat
            bordered
            auto-upload
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
            <div class="q-uploader__title">上传基础信息《文件小于1MB》</div>
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
<!--       <q-btn unelevated label="上传" icon="cloud_upload" @click="onRefresh">-->
<!--         <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">-->
<!--          批量上传-->
<!--        </q-tooltip>-->
<!--       </q-btn>-->
             <q-space />
       <template>
  <div class="q-pa-md">
    <q-btn-dropdown
      class="glossy"
      color="purple"
      menu-anchor="bottom right"
      label="上传模板下载"
    >
      <div class="row no-wrap q-pa-md">
        <div class="column">
          <div class="text-h6 q-mb-md">模板须知</div>
          <q-btn label="一次只支持上传一个文件，文件的大小不得超过1MB" size="md" align="left" flat icon="warning"/>
          <q-btn label="创建时间为系统后台时间，无需输入" size="md" align="left" flat icon="warning"/>
          <q-btn label="文件格式只接受xls和xlsx，其他格式的文件不会被保存" size="md" align="left" flat icon="warning"/>
          <q-btn label="所有的时间都是以天来计算" size="md" align="left" flat icon="warning"/>
          <q-btn label="每页仅显示50条记录，如果需要显示多条，请根据开放的API自行调整" size="md" align="left" flat icon="warning"/>
        </div>

        <q-separator vertical inset class="q-mx-lg" />

        <div class="flex flex-center">

          <q-btn
            color="secondary"
            label="下载"
            icon="cloud_download"
            glossy
            v-close-popup
            @click="downloadexample()"
          />
        </div>
      </div>
    </q-btn-dropdown>
  </div>
</template>
      </template>
        <template v-slot:no-data="{ icon, message, filter }">
        <div class="full-width row flex-center text-accent q-gutter-sm">
          <q-icon size="2em" name="sentiment_dissatisfied" />
          <span>
            Well this is sad... {{ message }}
          </span>
          <q-icon size="2em" :name="filter ? 'filter_b_and_w' : icon" />
        </div>
      </template>
      </q-table>
<template>
        <div class="q-pa-lg flex flex-center">
          <q-pagination
            v-model="current"
            color="purple"
            :max="totlepage"
            :max-pages="5"
            :boundary-links="true"
            :direction-links="true"
            :boundary-numbers="true"
            style="z-index: 1000"
            @click="pageChange()"
          >
          </q-pagination>
        </div>
      </template>
  </div>
</template>
    <router-view />
  </q-page>
</template>

<script>
import { get } from 'boot/axios'
import { openURL } from 'quasar'
export default {
  name: 'baseinfo',
  data () {
    return {
      separator: 'vertical',
      loading: false,
      mobileData: true,
      bluetooth: false,
      totlepage: 1,
      current: 1,
      height: '',
      uploaded: '',
      columns: [
        { name: 'goods_code', required: true, label: '商品编号', align: 'left', field: 'goods_code' },
        { name: 'sup_product_day', label: '供应商生产周期(天)', field: 'sup_product_day' },
        { name: 'sup_intransit', label: '供应商送货在途时间(天)', field: 'sup_intransit' },
        { name: 'loading_inspect', label: '到货卸货和检验时间(天)', field: 'loading_inspect' },
        { name: 'create_time', label: '创建时间', field: 'create_time' }
      ],
      data: [
      ],
      pagination: {
        sortBy: 'goods_code',
        descending: true,
        page: 1,
        rowsPerPage: 100
        // rowsNumber: xx if getting data from a server
      }
    }
  },
  methods: {
    getList () {
      var openid = this.$q.localStorage.getItem('openid')
      get('baseinfo/list/', { openid: openid, page: this.current, max_page: 50 }).then(response => {
        if (response.data.results.code === '200') {
          this.data = response.data.results.data
          this.totlepage = response.data.results.totlepage
        } else {}
      }).catch(error => { console.log(error) })
    },
    getSelectedString () {
      return this.selected.length === 0 ? '' : `${this.selected.length} record${this.selected.length > 1 ? 's' : ''} selected of ${this.data.length}`
    },
    successUpload () {
      this.getList()
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
    pageChange () {
      this.getList()
    },
    downloadexample () {
      openURL('https://scmapi.56yhz.com/baseinfo/ex/')
    }
  },
  created () {
    this.uploaded = 'https://scmapi.56yhz.com/baseinfo/?openid=' + this.$q.localStorage.getItem('openid')
  },
  mounted () {
    if (this.$q.localStorage.has('openid')) {
      this.getList()
    } else {}
    if (this.$q.platform.is.electron) {
      this.height = String(this.$q.screen.height - 275) + 'px'
    } else {
      this.height = this.$q.screen.height - 275 + '' + 'px'
    }
  },
  updated () {
  }
}
</script>
