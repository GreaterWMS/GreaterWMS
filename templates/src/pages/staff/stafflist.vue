<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        id="table"
        class="my-sticky-header-column-table shadow-24"
        :data="table_list"
        row-key="id"
        :separator="separator"
        :loading="loading"
        :columns="columns"
        hide-bottom
        :pagination.sync="pagination"
        no-data-label="No data"
        no-results-label="No data you want"
        :table-style="{ height: height }"
        flat
        bordered
      >
        <template v-slot:top>
          <q-btn-group push>
            <q-btn
              v-show="
                $q.localStorage.getItem('staff_type') !== 'Supplier' &&
                  $q.localStorage.getItem('staff_type') !== 'Customer' &&
                  $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                  $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                  $q.localStorage.getItem('staff_type') !== 'StockControl'
              "
              :label="$t('new')"
              icon="add"
              @click="newForm = true"
            >
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('newtip') }}</q-tooltip>
            </q-btn>
            <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('refreshtip') }}</q-tooltip>
            </q-btn>
            <q-btn :label="$t('download')" icon="cloud_download" @click="downloadData()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('downloadtip') }}</q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
          <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @input="getSearchList()">
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <template v-if="props.row.id === editid">
              <q-td key="staff_name" :props="props">
                <q-input
                  dense
                  outlined
                  square
                  v-model="editFormData.staff_name"
                  :label="$t('staff.view_staff.staff_name')"
                  autofocus
                  :rules="[val => (val && val.length > 0) || error1]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="staff_name" :props="props">{{ props.row.staff_name }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="staff_type" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.staff_type"
                  :options="staff_type_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('staff.view_staff.staff_type')"
                  :rules="[val => (val && val.length > 0) || error2]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="staff_type" :props="props">{{ props.row.staff_type }}</q-td>
            </template>
            <q-td key="create_time" :props="props">{{ props.row.create_time }}</q-td>
            <q-td key="update_time" :props="props">{{ props.row.update_time }}</q-td>
            <template v-if="!editMode">
              <q-td key="action" :props="props" style="width: 240px">
                <q-btn
                  v-show="
                    $q.localStorage.getItem('staff_type') !== 'Supplier' &&
                      $q.localStorage.getItem('staff_type') !== 'Customer' &&
                      $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                      $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                      $q.localStorage.getItem('staff_type') !== 'StockControl'
                  "
                  round
                  flat
                  push
                  color="purple"
                  icon="edit"
                  @click="editData(props.row)"
                >
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('edit') }}</q-tooltip>
                </q-btn>
                <q-btn
                  v-show="
                    $q.localStorage.getItem('staff_type') !== 'Supplier' &&
                      $q.localStorage.getItem('staff_type') !== 'Customer' &&
                      $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                      $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                      $q.localStorage.getItem('staff_type') !== 'StockControl'
                  "
                  round
                  flat
                  push
                  color="dark"
                  icon="delete"
                  @click="deleteData(props.row.id)"
                >
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('delete') }}</q-tooltip>
                </q-btn>
                <q-btn color="teal" :label="$t('contact')" icon="contacts" @click="ChatWith(props.row.staff_name)">
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('sendmessage') }}</q-tooltip>
                </q-btn>
              </q-td>
            </template>
            <template v-else-if="editMode">
              <template v-if="props.row.id === editid">
                <q-td key="action" :props="props" style="width: 150px">
                  <q-btn round flat push color="secondary" icon="check" @click="editDataSubmit()">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('confirmedit') }}</q-tooltip>
                  </q-btn>
                  <q-btn round flat push color="red" icon="close" @click="editDataCancel()">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('canceledit') }}</q-tooltip>
                  </q-btn>
                </q-td>
              </template>
              <template v-else-if="props.row.id !== editid"></template>
            </template>
          </q-tr>
        </template>
      </q-table>
    </transition>
    <template>
      <div class="q-pa-lg flex flex-center">
        <q-btn v-show="pathname_previous" flat push color="purple" :label="$t('previous')" icon="navigate_before" @click="getListPrevious()">
          <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('previous') }}</q-tooltip>
        </q-btn>
        <q-btn v-show="pathname_next" flat push color="purple" :label="$t('next')" icon-right="navigate_next" @click="getListNext()">
          <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('next') }}</q-tooltip>
        </q-btn>
        <q-btn v-show="!pathname_previous && !pathname_next" flat push color="dark" :label="$t('no_data')"></q-btn>
      </div>
    </template>
    <q-dialog v-model="newForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ $t('newtip') }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">
          <q-input
            dense
            outlined
            square
            v-model.trim="newFormData.staff_name"
            :label="$t('staff.view_staff.staff_name')"
            autofocus
            :rules="[val => (val && val.length > 0) || error1]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.staff_type"
            :options="staff_type_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('staff.view_staff.staff_type')"
            :rules="[val => (val && val.length > 0) || error2]"
            @keyup.enter="newDataSubmit()"
            style="margin-top: 5px"
          />
        </q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="newDataSubmit()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
    <q-dialog v-model="deleteForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ $t('delete') }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">{{ $t('deletetip') }}</q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="deleteDataCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="deleteDataSubmit()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
    <q-dialog v-model="chat">
      <q-card style="width: 600px">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ receiver }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[20, 20]" content-style="font-size: 12px" @click="ChatClose()">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-separator />
        <q-card-section id="chat_scroll" style="max-height: 50vh; height: 50vh" class="scroll">
          <template>
            <div class="q-pa-md row justify-center">
              <q-btn flat rounded :label="$t('loadmore')" @click="LoadChatList()" v-show="chat_next !== null"></q-btn>
              <div style="width: 100%">
                <q-chat-message v-show="chat_next === null" :label="$t('nomoremessage')" />
                <div v-for="item in chat_list" :key="item.id">
                  <q-chat-message
                    v-if="item.sender === sender + '-' + openid"
                    :name="sender"
                    :text="[item.detail]"
                    bg-color="light-green-4"
                    name-sanitize
                    sent
                    text-sanitize
                    :stamp="item.create_time"
                  />
                  <q-chat-message v-else :name="receiver" :text="[item.detail]" text-sanitize name-sanitize bg-color="grey-4" />
                </div>
              </div>
            </div>
          </template>
        </q-card-section>
        <q-separator />
        <q-card-actions align="right">
          <q-input
            maxlength="200"
            autofocus
            dense
            outlined
            square
            counter
            v-model="chat_text"
            :placeholder="$t('sendmessage')"
            class="bg-white col"
            @keyup.enter="websocketsend()"
            @keyup.esc="ChatClose()"
          />
          <q-btn flat :label="$t('send')" color="primary" @click="websocketsend()"></q-btn>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>
<router-view />

<script>
import { getauth, postauth, putauth, deleteauth, wsurl, getfile } from 'boot/axios_request';
import { date, exportFile, LocalStorage } from 'quasar';
var ws;

export default {
  name: 'Pagestafflist',
  data() {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'staff/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      staff_type_list: ['Manager', 'Inbound', 'Outbound', 'Supervisor', 'StockControl', 'Customer', 'Supplier'],
      columns: [
        { name: 'staff_name', required: true, label: this.$t('staff.view_staff.staff_name'), align: 'left', field: 'staff_name' },
        { name: 'staff_type', label: this.$t('staff.view_staff.staff_type'), field: 'staff_type', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' },
        { name: 'action', label: this.$t('action'), align: 'right' }
      ],
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      newForm: false,
      newFormData: {
        staff_name: '',
        staff_type: '',
        check_code: ''
      },
      editid: 0,
      editFormData: {},
      editMode: false,
      deleteForm: false,
      deleteid: 0,
      sender: '',
      receiver: '',
      chat: false,
      chat_list: [],
      chat_text: '',
      chat_next: null,
      filter: '',
      error1: this.$t('staff.view_staff.error1'),
      error2: this.$t('staff.view_staff.error2')
    };
  },
  methods: {
    getList() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname, {})
          .then(res => {
            _this.table_list = res.results;
            _this.pathname_previous = res.previous;
            _this.pathname_next = res.next;
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else {
      }
    },
    getSearchList() {
      var _this = this;
      _this.filter = _this.filter.replace(/\s+/g, '');
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + '?staff_name__icontains=' + _this.filter, {})
          .then(res => {
            _this.table_list = res.results;
            _this.pathname_previous = res.previous;
            _this.pathname_next = res.next;
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else {
      }
    },
    getListPrevious() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_previous, {})
          .then(res => {
            _this.table_list = res.results;
            _this.pathname_previous = res.previous;
            _this.pathname_next = res.next;
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else {
      }
    },
    getListNext() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_next, {})
          .then(res => {
            _this.table_list = res.results;
            _this.pathname_previous = res.previous;
            _this.pathname_next = res.next;
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else {
      }
    },
    reFresh() {
      var _this = this;
      _this.getList();
    },
    RandomCheckCode() {
      var _this = this;
      var code = '';
      var codeLength = 4;
      var random = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
      for (var i = 0; i < codeLength; i++) {
        var index = Math.floor(Math.random() * 9);
        code += random[index];
      }
      _this.newFormData.check_code = code;
    },
    newDataSubmit() {
      var _this = this;
      var staffs = [];
      _this.table_list.forEach(i => {
        staffs.push(i.staff_name);
      });
      if (staffs.indexOf(_this.newFormData.staff_name) === -1 && _this.newFormData.staff_name.length !== 0 && _this.newFormData.staff_type) {
        _this.RandomCheckCode();
        postauth(_this.pathname, _this.newFormData)
          .then(res => {
            _this.getList();
            _this.newDataCancel();
            _this.$q.notify({
              message: 'Success Create',
              icon: 'check',
              color: 'green'
            });
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else if (staffs.indexOf(_this.newFormData.staff_name) !== -1) {
        _this.$q.notify({
          message: _this.$t('notice.userererror'),
          icon: 'close',
          color: 'negative'
        });
      } else if (_this.newFormData.staff_name.length === 0) {
        _this.$q.notify({
          message: _this.$t('staff.view_staff.error1'),
          icon: 'close',
          color: 'negative'
        });
      } else if (!_this.newFormData.staff_type) {
        _this.$q.notify({
          message: _this.$t('staff.view_staff.error2'),
          icon: 'close',
          color: 'negative'
        });
      }
    },
    newDataCancel() {
      var _this = this;
      _this.newForm = false;
      _this.newFormData = {
        staff_name: '',
        staff_type: ''
      };
    },
    editData(e) {
      var _this = this;
      _this.editMode = true;
      _this.editid = e.id;
      _this.editFormData = {
        staff_name: e.staff_name,
        staff_type: e.staff_type
      };
    },
    editDataSubmit() {
      var _this = this;
      putauth(_this.pathname + _this.editid + '/', _this.editFormData)
        .then(res => {
          _this.editDataCancel();
          _this.getList();
          _this.$q.notify({
            message: 'Success Edit Data',
            icon: 'check',
            color: 'green'
          });
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    editDataCancel() {
      var _this = this;
      _this.editMode = false;
      _this.editid = 0;
      _this.editFormData = {
        staff_name: '',
        staff_type: ''
      };
    },
    deleteData(e) {
      var _this = this;
      _this.deleteForm = true;
      _this.deleteid = e;
    },
    deleteDataSubmit() {
      var _this = this;
      deleteauth(_this.pathname + _this.deleteid + '/')
        .then(res => {
          _this.deleteDataCancel();
          _this.getList();
          _this.$q.notify({
            message: 'Success Edit Data',
            icon: 'check',
            color: 'green'
          });
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    deleteDataCancel() {
      var _this = this;
      _this.deleteForm = false;
      _this.deleteid = 0;
    },
    initWebSocket() {
      var _this = this;
      ws = new WebSocket(wsurl + '?sender=' + _this.login_name + '&receiver=' + _this.receiver + '&openid=' + _this.openid);
      ws.onmessage = _this.websocketonmessage;
      ws.onopen = _this.websocketonopen;
      ws.onerror = _this.websocketonerror;
      ws.onclose = _this.websocketclose;
    },
    websocketonopen() {
      console.log('Success Connect');
    },
    websocketonerror() {
      var _this = this;
      _this.initWebSocket();
    },
    websocketonmessage(e) {
      var _this = this;
      if (_this.$q.sessionStorage.getItem('receiver') === JSON.parse(e.data).sender) {
        _this.chat_list.push(JSON.parse(e.data));
      } else {
      }
      _this.Readnum();
      _this.$q.notify({
        message: JSON.parse(e.data).sender + ' Send you a message',
        color: 'deep-purple',
        icon: 'textsms',
        position: 'right',
        actions: [
          {
            label: 'VIEW',
            color: 'yellow',
            handler: () => {
              _this.ChatWith(JSON.parse(e.data).sender);
            }
          }
        ]
      });
    },
    websocketsend() {
      var _this = this;
      if (_this.chat_text === '') {
      } else {
        ws.send(_this.chat_text);
        _this.chat_list.push({
          sender: _this.sender + '-' + _this.openid,
          receiver: _this.receiver,
          detail: _this.chat_text,
          create_time: date.formatDate(Date.now(), 'YYYY-MM-DD HH:mm:ss')
        });
        _this.chat_text = '';
      }
    },
    websocketclose(e) {
      console.log('Disconnect', e);
    },
    ChatWith(e) {
      var _this = this;
      _this.sender = _this.login_name;
      _this.receiver = e;
      _this.$q.sessionStorage.set('receiver', e);
      if (_this.sender === _this.receiver) {
        _this.$q.notify({
          message: 'Cannot Chat with yourself',
          icon: 'close',
          color: 'negative'
        });
      } else {
        _this.chat = true;
        _this.chat_text = '';
        _this.initWebSocket();
        getauth('chat/?' + 'sender=' + _this.sender + '&receiver=' + _this.receiver)
          .then(res => {
            _this.chat_list = res.results.reverse();
            _this.chat_next = res.next;
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      }
    },
    LoadChatList() {
      var _this = this;
      getauth(_this.chat_next)
        .then(res => {
          res.results.forEach(c => {
            _this.chat_list.unshift(c);
          });
          _this.chat_next = res.next;
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    ChatClose() {
      var _this = this;
      _this.receiver = '';
      _this.$q.sessionStorage.set('receiver', '');
      _this.chat_list = [];
      _this.chat_text = '';
      _this.chat_next = null;
    },
    downloadData() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        getfile(_this.pathname + 'file/?lang=' + LocalStorage.getItem('lang')).then(res => {
          var timeStamp = Date.now();
          var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS');
          const status = exportFile(_this.pathname + formattedString + '.csv', '\uFEFF' + res.data, 'text/csv');
          if (status !== true) {
            this.$q.notify({
              message: 'Browser denied file download...',
              color: 'negative',
              icon: 'warning'
            });
          }
        });
      } else {
        _this.$q.notify({
          message: _this.$t('notice.loginerror'),
          color: 'negative',
          icon: 'warning'
        });
      }
    }
  },
  created() {
    var _this = this;
    if (LocalStorage.has('openid')) {
      _this.openid = LocalStorage.getItem('openid');
    } else {
      _this.openid = '';
      LocalStorage.set('openid', '');
    }
    if (LocalStorage.has('login_name')) {
      _this.login_name = LocalStorage.getItem('login_name');
    } else {
      _this.login_name = '';
      LocalStorage.set('login_name', '');
    }
    if (LocalStorage.has('auth')) {
      _this.authin = '1';
      _this.getList();
    } else {
      _this.authin = '0';
    }
  },
  mounted() {
    var _this = this;
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height - 290) + 'px';
    } else {
      _this.height = _this.$q.screen.height - 290 + '' + 'px';
    }
  },
  updated() {
    if (document.getElementById('chat_scroll')) {
      document.getElementById('chat_scroll').scrollTop = document.getElementById('chat_scroll').scrollHeight;
    } else {
    }
  },
  destroyed() {
    if (ws) {
      if (ws.readyState === ws.OPEN) {
        ws.close();
      }
    }
  }
};
</script>
