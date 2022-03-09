<template>
  <q-layout
    view="hHh LpR fFf"
    :style="{ height: $q.screen.height, width: $q.screen.width }"
  >
    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar class="main-headers text-white rounded-borders">
        <transition appear enter-active-class="animated zoomIn">
          <q-btn flat @click="drawerleft = !drawerleft" round dense icon="menu">
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[15, 15]"
              content-style="font-size: 12px"
              >{{ $t("index.hide_menu") }}</q-tooltip
            >
          </q-btn>
        </transition>
        <q-space />
        <transition appear enter-active-class="animated zoomIn">
          <q-btn
            round
            dense
            flat
            color="white"
            icon="translate"
            style="margin: 0 10px 0 10px"
          >
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[15, 15]"
              content-style="font-size: 12px"
              >{{ $t("index.translate") }}</q-tooltip
            >
            <q-menu>
              <q-list style="min-width: 100px">
                <q-item
                  clickable
                  v-close-popup
                  v-for="(language, index) in langOptions"
                  :key="index"
                  @click="langChange(language.value)"
                >
                  <q-item-section>{{ language.label }}</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        </transition>
        <q-separator vertical />
        <template v-if="authin === '1'">
          <transition appear enter-active-class="animated zoomIn">
            <q-btn-dropdown
              stretch
              flat
              color="white-8"
              icon="account_circle"
              @click="chat = false"
            >
              <div class="row no-wrap q-pa-md">
                <div class="column" style="width: 150px">
                  <div
                    style="
                      width: 100%;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    <span style="margin-left: 9%; font-weight: bold"
                      >{{ $t("index.current_user") }}:</span
                    >
                    <span style="margin-left: 6%; font-weight: bold">{{
                      login_name
                    }}</span>
                  </div>
                  <hr
                    style="
                      height: 2px;
                      border: none;
                      border-top: 1px solid #e1e1e1;
                      width: 121%;
                      margin-left: -10.5%;
                      margin-top: 8%;
                    "
                  />
                  <q-btn
                    flat
                    rounded
                    class="full-width"
                    align="left"
                    :label="$t('index.change_user')"
                    @click="login = true"
                  >
                    <q-tooltip
                      content-class="bg-amber text-black shadow-4"
                      :offset="[10, 10]"
                      content-style="font-size: 12px"
                      >{{ $t("index.change_user") }}</q-tooltip
                    >
                  </q-btn>
                  <q-btn
                    flat
                    rounded
                    class="full-width"
                    align="left"
                    :label="$t('index.view_my_openid')"
                    @click="authid = true"
                  >
                    <q-tooltip
                      content-class="bg-amber text-black shadow-4"
                      :offset="[10, 10]"
                      content-style="font-size: 12px"
                      >{{ $t("index.view_my_openid") }}</q-tooltip
                    >
                  </q-btn>
                  <hr
                    style="
                      height: 2px;
                      border: none;
                      border-top: 1px solid #e1e1e1;
                      width: 121%;
                      margin-left: -10.5%;
                      margin-top: 8%;
                    "
                  />
                  <q-btn
                    flat
                    rounded
                    class="full-width"
                    align="left"
                    :label="$t('index.logout')"
                    @click="Logout()"
                  >
                    <q-tooltip
                      content-class="bg-amber text-black shadow-4"
                      :offset="[10, 10]"
                      content-style="font-size: 12px"
                      >{{ $t("index.contact_list") }}</q-tooltip
                    >
                  </q-btn>
                </div>
              </div>
            </q-btn-dropdown>
          </transition>
        </template>
        <template v-if="authin === '0'">
          <transition appear enter-active-class="animated zoomIn">
            <q-btn
              :label="$t('index.login')"
              color="primary"
              @click="login = true"
              style="margin-left: 10px"
            >
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[15, 15]"
                content-style="font-size: 12px"
                >{{ $t("index.login_tip") }}</q-tooltip
              >
            </q-btn>
          </transition>
          <transition appear enter-active-class="animated zoomIn">
            <q-btn
              :label="$t('index.register')"
              color="primary"
              @click="register = true"
              style="margin-left: 10px"
            >
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[15, 15]"
                content-style="font-size: 12px"
                >{{ $t("index.register_tip") }}</q-tooltip
              >
            </q-btn>
          </transition>
        </template>
      </q-toolbar>
    </q-header>
    <q-drawer
      v-model="drawerleft"
      show-if-above
      :width="200"
      :breakpoint="500"
      bordered
      content-class="bg-grey-3 shadow-24"
    >
      <q-scroll-area class="fit" style="overflow-y: auto">
        <q-list>
          <q-item
            clickable
            :to="{ name: 'mp_inboundAndOutbound' }"
            @click="linkChange('dashboard')"
            v-ripple
            exact
            :active="link === 'dashboard' && link !== ''"
            :class="{ 'my-menu-link': link === 'dashboard' && link !== '' }"
          >
            <q-item-section avatar><q-icon name="auto_graph" /></q-item-section>
            <q-item-section>{{ $t("menuItem.dashboard") }}</q-item-section>
          </q-item>
          <q-separator />
          <q-item
            clickable
            :to="{ name: 'mp_asn' }"
            @click="linkChange('inbound')"
            v-ripple
            exact
            :active="link === 'inbound' && link !== ''"
            :class="{ 'my-menu-link': link === 'inbound' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="speaker_notes"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.inbound") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'mp_dn' }"
            @click="linkChange('outbound')"
            v-ripple
            exact
            :active="link === 'outbound' && link !== ''"
            :class="{ 'my-menu-link': link === 'outbound' && link !== '' }"
          >
            <q-item-section avatar><q-icon name="rv_hookup" /></q-item-section>
            <q-item-section>{{ $t("menuItem.outbound") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'mp_stocklist' }"
            @click="linkChange('stock')"
            v-ripple
            exact
            :active="link === 'stock' && link !== ''"
            :class="{ 'my-menu-link': link === 'stock' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="multiline_chart"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.stock") }}</q-item-section>
          </q-item>
          <q-separator />
          <q-item
            clickable
            :to="{ name: 'mp_capitallist' }"
            @click="linkChange('finance')"
            v-ripple
            exact
            :active="link === 'finance' && link !== ''"
            :class="{ 'my-menu-link': link === 'finance' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="devices_other"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.finance") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'mp_goodslist' }"
            @click="linkChange('goods')"
            v-ripple
            exact
            :active="link === 'goods' && link !== ''"
            :class="{ 'my-menu-link': link === 'goods' && link !== '' }"
          >
            <q-item-section avatar><q-icon name="shop_two" /></q-item-section>
            <q-item-section>{{ $t("menuItem.goods") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'mp_supplier' }"
            @click="linkChange('baseinfo')"
            v-ripple
            exact
            :active="link === 'baseinfo' && link !== ''"
            :class="{ 'my-menu-link': link === 'baseinfo' && link !== '' }"
          >
            <q-item-section avatar><q-icon name="info" /></q-item-section>
            <q-item-section>{{ $t("menuItem.baseinfo") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'mp_warehouseset' }"
            @click="linkChange('warehouse')"
            v-ripple
            exact
            :active="link === 'warehouse' && link !== ''"
            :class="{ 'my-menu-link': link === 'warehouse' && link !== '' }"
          >
            <q-item-section avatar><q-icon name="settings" /></q-item-section>
            <q-item-section>{{ $t("menuItem.warehouse") }}</q-item-section>
          </q-item>
          <q-separator />
          <q-item
            clickable
            :to="{ name: 'mp_stafflist' }"
            @click="linkChange('staff')"
            v-ripple
            exact
            :active="link === 'staff' && link !== ''"
            :class="{ 'my-menu-link': link === 'staff' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="assignment_ind"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.staff") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'mp_driverlist' }"
            @click="linkChange('driver')"
            v-ripple
            exact
            :active="link === 'driver' && link !== ''"
            :class="{ 'my-menu-link': link === 'driver' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="transfer_within_a_station"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.driver") }}</q-item-section>
          </q-item>
          <q-separator />
           <q-item
            clickable
            @click="brownlink('pdf/GreaterWMS_price.pdf')"
            v-ripple
            exact
            v-show="lang === 'zh-hans'"
          >
            <q-item-section avatar
              ><q-icon name="add_shopping_cart"
            /></q-item-section>
            <q-item-section>适配硬件清单</q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>
    <q-page-container
      class="main-page"
      :style="{
        height: container_height,
        width: $q.screen.width,
      }"
    >
      <router-view />
    </q-page-container>
    <q-dialog v-model="chat">
      <q-card style="width: 600px">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <div>{{ receiver }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[20, 20]"
              content-style="font-size: 12px"
              @click="ChatClose()"
              >{{ $t("index.close") }}</q-tooltip
            >
          </q-btn>
        </q-bar>
        <q-separator />
        <q-card-section
          id="chat_scroll"
          style="max-height: 50vh; height: 50vh"
          class="scroll"
        >
          <template>
            <div class="q-pa-md row justify-center">
              <q-btn
                flat
                rounded
                :label="$t('index.chat_more')"
                @click="LoadChatList()"
                v-show="chat_next !== null"
              ></q-btn>
              <div style="width: 100%">
                <q-chat-message
                  v-show="chat_next === null"
                  :label="$t('index.chat_no_more')"
                />
                <div v-for="item in chat_list" :key="item.id">
                  <q-chat-message
                    v-if="item.sender === sender + '-' + openid"
                    :name="sender"
                    :text="[item.detail]"
                    bg-color="light-green-4"
                    name-sanitize
                    sent
                    text-sanitize
                  />
                  <q-chat-message
                    v-else
                    :name="receiver"
                    :text="[item.detail]"
                    text-sanitize
                    name-sanitize
                    bg-color="grey-4"
                  />
                </div>
              </div>
            </div>
          </template>
        </q-card-section>
        <q-separator />
        <q-card-actions align="right">
          <q-input
            autofocus
            dense
            outlined
            square
            v-model="chat_text"
            placeholder="Send Message"
            class="bg-white col"
            @keyup.enter="websocketsend()"
            @keyup.esc="ChatClose()"
          />
          <q-btn
            flat
            :label="$t('index.chat_send')"
            color="primary"
            @click="websocketsend()"
          ></q-btn>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="read" position="right">
      <q-card style="width: 300px">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <div>{{ $t("index.unread") }}({{ read_num }})</div>
          <q-space></q-space>
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[20, 20]"
              content-style="font-size: 12px"
              >{{ $t("index.close") }}</q-tooltip
            >
          </q-btn>
        </q-bar>
        <q-separator></q-separator>
        <q-card-section style="max-height: 50vh; height: 50vh" class="scroll">
          <q-list>
            <div v-for="item in read_list" :key="item.id">
              <q-item clickable v-ripple>
                <q-item-section>
                  <q-item-label @click="ChatWith(item.sender.split('-')[0])">{{
                    item.sender.split("-")[0]
                  }}</q-item-label>
                  <q-item-label
                    caption
                    lines="2"
                    @click="ChatWith(item.sender.split('-')[0])"
                    >{{ item.detail }}</q-item-label
                  >
                </q-item-section>
              </q-item>
            </div>
          </q-list>
        </q-card-section>
        <q-separator v-show="read_num > 30"></q-separator>
        <q-card-actions align="left">
          <q-btn
            flat
            v-show="read_previous !== null"
            :label="$t('index.previous')"
            color="primary"
            @click="ReadnumPrevious()"
          ></q-btn>
          <q-btn
            flat
            v-show="read_next !== null"
            :label="$t('index.next')"
            color="primary"
            @click="ReadnumNext()"
          ></q-btn>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog
      v-model="authid"
      transition-show="jump-down"
      transition-hide="jump-up"
    >
      <q-card style="min-width: 350px">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <div>{{ $t("index.your_openid") }}</div>
          <q-space></q-space>
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[20, 20]"
              content-style="font-size: 12px"
              >{{ $t("index.close") }}</q-tooltip
            >
          </q-btn>
        </q-bar>
        <q-card-section class="q-pt-md"
          ><q-input
            dense
            outlined
            square
            label="Openid"
            v-model="openid"
            readonly
        /></q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog v-model="friend" position="right">
      <q-card style="width: 300px">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <div>{{ $t("index.contact_list") }}({{ friend_num }})</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[20, 20]"
              content-style="font-size: 12px"
              >关闭</q-tooltip
            >
          </q-btn>
        </q-bar>
        <q-separator v-show="$q.platform.is.desktop" />
        <q-card-section style="max-height: 50vh; height: 50vh" class="scroll">
          <q-list>
            <template v-for="item in friend_list">
              <q-item clickable v-ripple v-bind:key="item.id">
                <q-item-section>
                  <q-item-label @click="ChatWith(item.staff_name)">{{
                    item.staff_name
                  }}</q-item-label>
                </q-item-section>
              </q-item>
            </template>
          </q-list>
        </q-card-section>
        <q-separator v-show="friend_num > 30"></q-separator>
        <q-card-actions align="left">
          <q-btn
            flat
            v-show="friend_previous !== null"
            :label="$t('index.previous')"
            color="primary"
            @click="Friend_previous()"
          ></q-btn>
          <q-btn
            flat
            v-show="friend_next !== null"
            :label="$t('index.next')"
            color="primary"
            @click="Friend_next()"
          ></q-btn>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog
      v-model="login"
      transition-show="jump-down"
      transition-hide="jump-up"
    >
      <q-card style="min-width: 350px">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <q-tabs v-model="activeTab" class="tabs">
            <q-tab name="user" @click="admin = false">
              {{ $t("index.user_login") }}
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[5, 5]"
                content-style="font-size: 12px"
                >{{ $t("index.user_login") }}</q-tooltip
              >
            </q-tab>
            <q-tab name="admin" @click="admin = true">
              {{ $t("index.admin_login") }}
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[5, 5]"
                content-style="font-size: 12px"
                >{{ $t("index.admin_login") }}</q-tooltip
              >
            </q-tab>
          </q-tabs>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[20, 20]"
              content-style="font-size: 12px"
              >{{ $t("index.close") }}</q-tooltip
            >
          </q-btn>
        </q-bar>
        <q-card-section class="q-pt-md">
          <template v-if="admin">
            <q-input
              dense
              outlined
              square
              :label="$t('index.admin_name')"
              v-model="adminlogin.name"
              autofocus
              @keyup.enter="adminLogin()"
            />
            <q-input
              dense
              outlined
              square
              :label="$t('index.password')"
              :type="isPwd ? 'password' : 'text'"
              v-model="adminlogin.password"
              @keyup.enter="adminLogin()"
              style="margin-top: 5px"
            >
              <template v-slot:append>
                <q-icon
                  :name="isPwd ? 'visibility_off' : 'visibility'"
                  class="cursor-pointer"
                  @click="isPwd = !isPwd"
                />
              </template>
            </q-input>
          </template>
          <template v-if="!admin">
            <q-input
              dense
              outlined
              square
              :label="$t('index.your_openid')"
              v-model="openid"
              @keyup.enter="Login()"
            />
            <q-input
              dense
              outlined
              square
              :label="$t('index.staff_name')"
              v-model="login_name"
              autofocus
              @keyup.enter="Login()"
              style="margin-top: 5px"
            />
            <q-input
              dense
              outlined
              square
              :label="$t('staff.check_code')"
              v-model.number="check_code"
              type="number"
              autofocus
              @keyup.enter="Login()"
              style="margin-top: 5px"
            />
          </template>
        </q-card-section>
        <q-card-actions align="left" class="text-primary">
          <q-space />
          <template>
            <q-btn
              color="primary"
              :label="$t('index.login')"
              style="font-size: 16px; margin: 0 8px; width: 100%"
              @click="admin ? adminLogin() : Login()"
            />
          </template>
          <div class="q-mx-auto">
            <q-btn
              flat
              class="text-teal-4 q-mt-sm"
              @click="
                login = false;
                register = true;
              "
            >
              {{ $t("index.register_tip") }}
            </q-btn>
          </div>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog
      v-model="register"
      transition-show="jump-down"
      transition-hide="jump-up"
    >
      <q-card style="min-width: 350px">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <div>{{ $t("index.register_tip") }}</div>
          <q-space></q-space>
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[20, 20]"
              content-style="font-size: 12px"
              >{{ $t("index.close") }}</q-tooltip
            >
          </q-btn>
        </q-bar>
        <q-card-section class="q-pt-md">
          <q-input
            dense
            outlined
            square
            :label="$t('index.staff_name')"
            v-model="registerform.name"
            autofocus
            @keyup.enter="Register()"
          />
          <q-input
            dense
            outlined
            square
            :label="$t('index.password')"
            v-model="registerform.password1"
            :type="isPwd ? 'password' : 'text'"
            @keyup.enter="Register()"
            style="margin-top: 5px"
          >
            <template v-slot:append>
              <q-icon
                :name="isPwd ? 'visibility_off' : 'visibility'"
                class="cursor-pointer"
                @click="isPwd = !isPwd"
              />
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            :label="$t('index.confirm_password')"
            v-model="registerform.password2"
            :type="isPwd2 ? 'password' : 'text'"
            @keyup.enter="Register()"
            style="margin-top: 5px"
          >
            <template v-slot:append>
              <q-icon
                :name="isPwd2 ? 'visibility_off' : 'visibility'"
                class="cursor-pointer"
                @click="isPwd2 = !isPwd2"
              />
            </template>
          </q-input>
        </q-card-section>
        <q-card-actions align="right" class="text-primary q-mx-sm"
          ><q-btn
            class="full-width"
            color="primary"
            :label="$t('index.register')"
            @click="Register()"
        /></q-card-actions>
        <q-card-actions align="center" style="margin-top: -8px">
          <q-btn
            class="text-teal-4"
            flat
            :label="$t('index.return_to_login')"
            @click="
              login = true;
              register = false;
            "
          ></q-btn>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-layout>
</template>
<script>
import { versioncheck, getauth, post, wsurl } from "boot/axios_request";
import { date, LocalStorage, SessionStorage, openURL, Platform } from "quasar";
import Bus from "boot/bus.js";

var ws;
export default {
  data() {
    return {
      activeTab: "user",
      device: LocalStorage.getItem("device"),
      device_name: LocalStorage.getItem("device_name"),
      lang: this.$i18n.locale,
      verCheck: false,
      version: "",
      updateNow: false,
      processpercent: 0,
      downloadprocess: false,
      container_height: this.$q.screen.height + "" + "px",
      langOptions: [
        { value: "en-us", label: "English" },
        { value: "zh-hans", label: "中文简体" },
        { value: "zh-hant", label: "中文繁體" },
        { value: "fr", label: "Français" },
        { value: "pt", label: "Português" },
        { value: "ru", label: "Español" },
        { value: "de", label: "Deutsch" },
        { value: "ru", label: "русский язык" },
        { value: "ar", label: "Arabic" },
        { value: "fr", label: "Italiano" },
        { value: "ja", label: "日本語" },
      ],
      title: this.$t("index.webtitle"),
      admin: false,
      adminlogin: {
        name: "",
        password: "",
      },
      openid: "",
      isPwd: true,
      isPwd2: true,
      authin: "0",
      authid: false,
      left: false,
      drawerleft: false,
      tab: "",
      login: false,
      link: "",
      login_name: "",
      check_code: "",
      register: false,
      registerform: {
        name: "",
        password1: "",
        password2: "",
      },
      friend: false,
      friend_num: 0,
      friend_list: [],
      friend_previous: null,
      friend_next: null,
      sender: "",
      receiver: "",
      chat: false,
      chat_list: [],
      chat_text: "",
      chat_next: null,
      read: false,
      read_num: 0,
      read_list: [],
      read_previous: "",
      read_next: "",
      needLogin: "",
    };
  },
  methods: {
    linkChange(e) {
      var _this = this;
      localStorage.removeItem("menulink", "");
      localStorage.setItem("menulink", e);
      _this.link = e;
    },
    drawerClick(e) {
      var _this = this;
      if (_this.miniState) {
        _this.miniState = false;
        e.stopPropagation();
      }
    },
    brownlink(e) {
      openURL(e);
    },
    Login() {
      var _this = this;
      if (_this.login_name === "") {
        _this.$q.notify({
          message: "Please enter the login name",
          color: "negative",
          icon: "close",
        });
      } else {
        if (_this.openid === "") {
          _this.$q.notify({
            message: "Please Enter The Openid",
            icon: "close",
            color: "negative",
          });
        } else {
          if (_this.check_code === "") {
            _this.$q.notify({
              message: "Please Enter The Check Code",
              icon: "close",
              color: "negative",
            });
          } else {
            LocalStorage.set("openid", _this.openid);
            SessionStorage.set("axios_check", "false");
            getauth(
              "staff/?staff_name=" +
                _this.login_name +
                "&check_code=" +
                _this.check_code
            )
              .then((res) => {
                if (res.count === 1) {
                  _this.authin = "1";
                  _this.login = false;
                  LocalStorage.set("auth", "1");
                  LocalStorage.set("login_name", _this.login_name);
                  LocalStorage.set("login_mode", "user");
                  _this.$q.notify({
                    message: "Success Login",
                    icon: "check",
                    color: "green",
                  });
                  _this.$router.push("/mobile");
                } else {
                  _this.$q.notify({
                    message: "No User's Data Or Check Code Wrong",
                    icon: "close",
                    color: "negative",
                  });
                }
              })
              .catch((err) => {
                _this.$q.notify({
                  message: err.detail,
                  icon: "close",
                  color: "negative",
                });
              });
          }
        }
      }
    },
    adminLogin() {
      var _this = this;
      if (!_this.adminlogin.name) {
        _this.$q.notify({
          message: "Please enter the admin name",
          color: "negative",
          icon: "close",
        });
      } else {
        if (!_this.adminlogin.password) {
          _this.$q.notify({
            message: "Please enter the admin password",
            icon: "close",
            color: "negative",
          });
        } else {
          SessionStorage.set("axios_check", "false");
          post("login/", _this.adminlogin)
            .then((res) => {
              if (res.code === "200") {
                _this.authin = "1";
                _this.login = false;
                _this.admin = false;
                _this.openid = res.data.openid;
                _this.login_name = res.data.name;
                LocalStorage.set("auth", "1");
                LocalStorage.set("openid", res.data.openid);
                LocalStorage.set("login_name", _this.login_name);
                LocalStorage.set("login_mode", "admin");
                _this.$q.notify({
                  message: "Success Login",
                  icon: "check",
                  color: "green",
                });
                _this.$router.push("/mobile");
              } else {
                _this.$q.notify({
                  message: res.msg,
                  icon: "close",
                  color: "negative",
                });
              }
            })
            .catch((err) => {
              _this.$q.notify({
                message: err.detail,
                icon: "close",
                color: "negative",
              });
            });
        }
      }
    },
    Logout() {
      var _this = this;
      _this.authin = "0";
      _this.login_name = "";
      LocalStorage.remove("auth");
      SessionStorage.remove("axios_check");
      LocalStorage.set("login_name", "");
      _this.$q.notify({
        message: "Success Logout",
        icon: "check",
        color: "negative",
      });
      // _this.staffType();
      _this.$router.push("/mobile");
    },
    Register() {
      var _this = this;
      SessionStorage.set("axios_check", "false");
      post("register/", _this.registerform)
        .then((res) => {
          if (res.code === "200") {
            _this.register = false;
            _this.openid = res.data.openid;
            _this.login_name = _this.registerform.name;
            _this.authin = "1";
            LocalStorage.set("openid", res.data.openid);
            LocalStorage.set("login_name", _this.registerform.name);
            LocalStorage.set("auth", "1");
            LocalStorage.set("login_mode", "admin");
            _this.registerform = {
              name: "",
              password1: "",
              password2: "",
            };
            _this.$q.notify({
              message: res.msg,
              icon: "check",
              color: "green",
            });
            _this.staffType();
            _this.$router.push("/mobile");
          } else {
            _this.$q.notify({
              message: res.msg,
              icon: "close",
              color: "negative",
            });
          }
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: "close",
            color: "negative",
          });
        });
    },
    staffType() {
      var _this = this;
      getauth("staff/?staff_name=" + _this.login_name).then((res) => {
        LocalStorage.set("staff_type", res.results[0].staff_type);
      });
    },
    initWebSocket() {
      var _this = this;
      ws = new WebSocket(
        wsurl +
          "?sender=" +
          _this.login_name +
          "&receiver=" +
          _this.receiver +
          "&openid=" +
          _this.openid
      );
      ws.onmessage = _this.websocketonmessage;
      ws.onopen = _this.websocketonopen;
      ws.onerror = _this.websocketonerror;
      ws.onclose = _this.websocketclose;
    },
    websocketonopen() {
      console.log("Success Connect");
    },
    websocketonerror() {
      var _this = this;
      _this.initWebSocket();
    },
    websocketonmessage(e) {
      var _this = this;
      if (SessionStorage.getItem("receiver") === JSON.parse(e.data).sender) {
        _this.chat_list.push(JSON.parse(e.data));
      }
      _this.Readnum();
      _this.$q.notify({
        message: JSON.parse(e.data).sender + " Send you a message",
        color: "deep-purple",
        icon: "textsms",
        position: "right",
        actions: [
          {
            label: "View",
            color: "yellow",
            handler: () => {
              _this.ChatWith(JSON.parse(e.data).sender);
            },
          },
        ],
      });
    },
    websocketsend() {
      var _this = this;
      if (_this.chat_text !== "") {
        ws.send(_this.chat_text);
        _this.chat_list.push({
          sender: _this.sender + "-" + _this.openid,
          receiver: _this.receiver,
          detail: _this.chat_text,
          create_time: date.formatDate(Date.now(), "YYYY-MM-DD HH:mm:ss"),
        });
        _this.chat_text = "";
      }
    },
    websocketclose(e) {
      console.log("Disconnect", e);
    },
    ChatWith(e) {
      var _this = this;
      _this.sender = _this.login_name;
      _this.receiver = e;
      SessionStorage.set("receiver", e);
      if (_this.sender === _this.receiver) {
        _this.$q.notify({
          message: "Cannot Chat with yourself",
          icon: "close",
          color: "negative",
        });
      } else {
        _this.chat = true;
        _this.chat_text = "";
        _this.initWebSocket();
        getauth(
          "chat/?" + "sender=" + _this.sender + "&receiver=" + _this.receiver
        )
          .then((res) => {
            _this.chat_list = res.results.reverse();
            _this.Readnum();
            _this.chat_next = res.next;
          })
          .catch((err) => {
            console.log(err);
            _this.$q.notify({
              message: err.detail,
              icon: "close",
              color: "negative",
            });
          });
      }
    },
    LoadChatList() {
      var _this = this;
      getauth(_this.chat_next)
        .then((res) => {
          res.results.forEach((c) => {
            _this.chat_list.unshift(c);
          });
          _this.chat_next = res.next;
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: "close",
            color: "negative",
          });
        });
    },
    ChatClose() {
      var _this = this;
      _this.receiver = "";
      SessionStorage.set("receiver", "");
      _this.chat_list = [];
      _this.chat_text = "";
      _this.chat_next = null;
    },
    Readnum() {
      var _this = this;
      getauth("chat/read/?" + "sender=" + _this.login_name)
        .then((res) => {
          _this.read_previous = res.previous;
          _this.read_next = res.next;
          _this.read_list = res.results;
          _this.read_num = res.count;
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: "close",
            color: "negative",
          });
        });
    },
    ReadnumPrevious() {
      var _this = this;
      getauth(_this.read_previous, {})
        .then((res) => {
          _this.read_list = res.results;
          _this.read_previous = res.previous;
          _this.read_next = res.next;
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: "close",
            color: "negative",
          });
        });
    },
    ReadnumNext() {
      var _this = this;
      getauth(_this.read_next, {})
        .then((res) => {
          _this.read_list = res.results;
          _this.read_previous = res.previous;
          _this.read_next = res.next;
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: "close",
            color: "negative",
          });
        });
    },
    Friend() {
      var _this = this;
      _this.friend = true;
      getauth("staff/", {})
        .then((res) => {
          _this.friend_list = res.results;
          _this.friend_previous = res.previous;
          _this.friend_next = res.next;
          _this.friend_num = res.count;
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: "close",
            color: "negative",
          });
        });
    },
    Friend_previous() {
      var _this = this;
      getauth(_this.friend_previous, {})
        .then((res) => {
          _this.friend_list = res.results;
          _this.friend_previous = res.previous;
          _this.friend_next = res.next;
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: "close",
            color: "negative",
          });
        });
    },
    Friend_next() {
      var _this = this;
      getauth(_this.friend_next, {})
        .then((res) => {
          _this.friend_list = res.results;
          _this.friend_previous = res.previous;
          _this.friend_next = res.next;
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: "close",
            color: "negative",
          });
        });
    },
    langChange(e) {
      var _this = this;
      _this.lang = e;
      window.setTimeout(() => {
        location.reload();
      }, 1);
    },
    isLoggedIn() {
      let login_mode = this.$q.localStorage.getItem("login_mode");
      if (login_mode) {
        this.activeTab = login_mode;
      }
      if (this.$q.localStorage.getItem("openid")) {
        this.login = true;
        if (this.activeTab === "admin") {
          this.admin = true;
        } else {
          this.admin = false;
        }
      } else {
        this.register = true;
      }
    },
  },
  beforeCreate() {},
  created() {
    var _this = this;
    if (LocalStorage.has("openid")) {
      _this.openid = LocalStorage.getItem("openid");
    } else {
      _this.openid = "";
      LocalStorage.set("openid", "");
    }
    if (LocalStorage.has("login_name")) {
      _this.login_name = LocalStorage.getItem("login_name");
    } else {
      _this.login_name = "";
      LocalStorage.set("login_name", "");
    }
    if (LocalStorage.has("auth")) {
      _this.authin = "1";
      _this.initWebSocket();
      _this.staffType();
      _this.Readnum();
    } else {
      LocalStorage.set("staff_type", "Admin");
      _this.authin = "0";
      _this.isLoggedIn();
    }
    if (LocalStorage.has("device")) {
      _this.device = LocalStorage.getItem("device");
    } else {
      _this.device = 0;
    }
    if (LocalStorage.has("device_name")) {
      _this.device_name = LocalStorage.getItem("device_name");
    } else {
      _this.device_name = "";
    }
  },
  mounted() {
    var _this = this;
    _this.link = localStorage.getItem("menulink");
    Bus.$on("needLogin", (val) => {
      _this.isLoggedIn();
    });
  },
  updated() {
    if (document.getElementById("chat_scroll")) {
      document.getElementById("chat_scroll").scrollTop =
        document.getElementById("chat_scroll").scrollHeight;
    } else if (document.getElementById("m_chat_scroll")) {
      document.getElementById("m_chat_scroll").scrollTop =
        document.getElementById("m_chat_scroll").scrollHeight;
    }
  },
  beforeDestroy() {
    Bus.$off("needLogin");
  },
  destroyed() {
    if (ws) {
      if (ws.readyState === ws.OPEN) {
        ws.close();
      }
    }
  },
  watch: {
    lang(lang) {
      var _this = this;
      LocalStorage.set("lang", lang);
      _this.$i18n.locale = lang;
    },
  },
};
</script>
<style>
.tabs .q-tab__indicator {
  width: 25%;
  height: 1.5px;
  margin: auto;
  color: #d6d7d7;
}
.tabs .absolute-bottom {
  bottom: 8px;
}
</style>
