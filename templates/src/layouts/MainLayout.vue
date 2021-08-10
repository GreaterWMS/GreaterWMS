<template>
  <q-layout view="hhh LpR lFf" :style="{ height: $q.screen.height, width: $q.screen.width }">
    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar class="main-headers text-white shadow-18 rounded-borders">
        <transition appear enter-active-class="animated zoomIn">
          <q-btn flat @click="drawerleft = !drawerleft" round dense icon="menu">
            <q-tooltip content-class="bg-indigo" :offset="[15, 15]" content-style="font-size: 12px">
              {{ $t('index.hide_menu') }}
            </q-tooltip>
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-toolbar-title v-show="$q.platform.is.desktop" shrink class="text-weight-bold">
            {{ $t('index.title') }}
          </q-toolbar-title>
        </transition>
        <q-space />
        <transition appear enter-active-class="animated zoomIn">
          <q-btn v-show="$q.platform.is.desktop && !$q.platform.is.electron" icon="img:statics/icons/logo.png" stretch flat :label="$t('index.home')" to="/">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              {{ $t('index.title_tip') }}
            </q-tooltip>
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <a v-show="$q.platform.is.desktop && !$q.platform.is.electron" href="/docs/" style="text-decoration:none; color: #c8e6c9">
            <q-btn icon="api" round dense flat style="margin: 0 10px 0 10px">
              <q-tooltip content-class="bg-indigo" :offset="[15, 15]" content-style="font-size: 12px">
                {{ $t('index.api') }}
              </q-tooltip>
            </q-btn>
          </a>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-btn v-show="$q.platform.is.desktop && !$q.platform.is.electron" icon="img:statics/icons/GitHub.png" round dense flat @click="brownlink('https://github.com/Singosgu/GreaterWMS')" style="margin: 0 10px 0 10px">
            <q-tooltip content-class="bg-indigo" :offset="[15, 15]" content-style="font-size: 12px">
              GitHub Link
            </q-tooltip>
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-btn round dense flat color="white" icon="translate" style="margin: 0 10px 0 10px">
            <q-tooltip content-class="bg-indigo" :offset="[15, 15]" content-style="font-size: 12px">
              {{ $t('index.translate') }}
            </q-tooltip>
            <q-menu>
              <q-list style="min-width: 100px">
                <q-item clickable v-close-popup v-for="(language, index) in langOptions" :key="index" @click="langChange(language.value)">
                  <q-item-section>{{ language.label }}</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        </transition>
        <q-separator vertical />
        <template v-if="authin === '1'">
        <transition appear enter-active-class="animated zoomIn">
          <q-btn round dense flat color="white" icon="notifications" @click="read = true" style="margin: 0 10px 0 10px">
            <q-badge v-if="read_num" color="red" text-color="white" floating>
              {{ read_num }}
            </q-badge>
            <q-tooltip content-class="bg-indigo" :offset="[15, 15]" content-style="font-size: 12px">
                {{ $t('index.unread') }}
            </q-tooltip>
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-btn-dropdown stretch flat color="white-8" icon="account_circle" @click="chat = false">
            <div class="row no-wrap q-pa-md">
              <div class="column" style="width: 200px">
                <div class="text-h6 q-mb-md">
                  {{ $t('index.user_center') }}
                </div>
                  <q-btn flat rounded class="full-width" align="left" icon="connect_without_contact" :label="$t('index.change_user')" @click="login = true">
                      <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                          {{ $t('index.change_user') }}
                      </q-tooltip>
                  </q-btn>
                  <q-btn flat rounded class="full-width" align="left" icon="list" :label="$t('index.view_my_openid')" @click="authid = true">
                      <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                          {{ $t('index.view_my_openid') }}
                      </q-tooltip>
                  </q-btn>
                  <q-btn flat rounded class="full-width" align="left" icon="img:statics/icons/profile.png" :label="$t('index.contact_list')" @click="Friend()">
                      <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                          {{ $t('index.contact_list') }}
                      </q-tooltip>
                  </q-btn>
                  <q-btn v-show="$q.platform.is.cordova || $q.platform.is.mobile" flat rounded class="full-width" align="left" icon="logout" :label="$t('index.logout')" @click="Logout()">
                      <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                          {{ $t('index.contact_list') }}
                      </q-tooltip>
                  </q-btn>
                </div>
                <q-separator v-show="$q.platform.is.desktop" vertical inset class="q-mx-lg" />
              <div class="column items-center" v-show="$q.platform.is.desktop">
                <q-avatar size="72px">
                    <q-img src="statics/staff/stafftype.png"></q-img>
                </q-avatar>
                <div class="text-subtitle1 q-mt-md q-mb-xs">{{ login_name }}</div>
                <q-btn
                  color="primary"
                  :label="$t('index.logout')"
                  push
                  size="sm"
                  v-close-popup
                  icon="img:statics/icons/logout.png"
                  @click="Logout()"
                ><q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('index.logout') }}</q-tooltip></q-btn>
              </div>
            </div>
          </q-btn-dropdown>
        </transition>
        </template>
        <template v-if="authin === '0'">
          <transition appear enter-active-class="animated zoomIn">
            <q-btn :label="$t('index.login')" color="primary" @click="login = true" style="margin-left: 10px">
              <q-tooltip content-class="bg-indigo" :offset="[15, 15]" content-style="font-size: 12px">
                {{ $t('index.login_tip') }}
              </q-tooltip>
            </q-btn>
          </transition>
          <transition appear enter-active-class="animated zoomIn">
            <q-btn :label="$t('index.register')" color="primary" @click="register = true" style="margin-left: 10px">
              <q-tooltip content-class="bg-indigo" :offset="[15, 15]" content-style="font-size: 12px">
                {{ $t('index.register_tip') }}
              </q-tooltip>
            </q-btn>
          </transition>
        </template>
      </q-toolbar>
    </q-header>
    <q-drawer
        v-model="drawerleft"
        show-if-above
        :mini="miniState"
        @mouseover="miniState = false"
        @mouseout="miniState = true"
        :width="200"
        :breakpoint="500"
        bordered
        content-class="bg-grey-3 shadow-24"
      >
      <q-scroll-area class="fit" style="overflow-y: auto"
      >
        <q-list>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound'
                         "
                  v-if="$q.platform.is.desktop"
            clickable to="/inbound/asn" @click="linkChange('inbound')" v-ripple exact :active="link === 'inbound'" :class="{ 'my-menu-link': link === 'inbound' }">
            <q-item-section avatar>
              <q-icon name="speaker_notes" />
            </q-item-section>
            <q-item-section>
              {{ $t('menuItem.inbound') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound'
                         "
                  v-if="$q.platform.is.desktop"
            clickable to="/outbound/dn" @click="linkChange('outbound')" v-ripple exact :active="link === 'outbound'" :class="{ 'my-menu-link': link === 'outbound' }">
            <q-item-section avatar>
              <q-icon name="rv_hookup" />
            </q-item-section>
            <q-item-section>
              {{ $t('menuItem.outbound') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         "
                  v-if="$q.platform.is.desktop"
            clickable to="/stock/stocklist" @click="linkChange('stock')" v-ripple exact :active="link === 'stock'" :class="{ 'my-menu-link': link === 'stock' }">
            <q-item-section avatar>
              <q-icon name="multiline_chart" />
            </q-item-section>
            <q-item-section>
              {{ $t('menuItem.stock') }}
            </q-item-section>
          </q-item>
          <q-separator v-show="$q.platform.is.desktop"/>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                          $q.localStorage.getItem('staff_type') !== 'StockControl'
                         "
                  v-if="$q.platform.is.desktop"
            clickable to="/finance/capitallist" @click="linkChange('finance')" v-ripple exact :active="link === 'finance'" :class="{ 'my-menu-link': link === 'finance' }">
            <q-item-section avatar>
              <q-icon name="devices_other" />
            </q-item-section>
            <q-item-section>
              {{ $t('menuItem.finance') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound'
                         "
                  v-if="$q.platform.is.desktop"
                  clickable to="/goods/goodslist" @click="linkChange('goods')" v-ripple exact :active="link === 'goods'" :class="{ 'my-menu-link': link === 'goods' }">
            <q-item-section avatar>
              <q-icon name="shop_two" />
            </q-item-section>
            <q-item-section>
              {{ $t('menuItem.goods') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                          $q.localStorage.getItem('staff_type') !== 'StockControl'
                         "
                  v-if="$q.platform.is.desktop"
            clickable to="/baseinfo/company" @click="linkChange('baseinfo')" v-ripple exact :active="link === 'baseinfo'" :class="{ 'my-menu-link': link === 'baseinfo' }">
            <q-item-section avatar>
              <q-icon name="info" />
            </q-item-section>
            <q-item-section>
              {{ $t('menuItem.baseinfo') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound'
                         "
                  v-if="$q.platform.is.desktop"
            clickable to="/warehouse/warehouseset" @click="linkChange('warehouse')" v-ripple exact :active="link === 'warehouse'" :class="{ 'my-menu-link': link === 'warehouse' }">
            <q-item-section avatar>
              <q-icon name="settings" />
            </q-item-section>
            <q-item-section>
              {{ $t('menuItem.warehouse') }}
            </q-item-section>
          </q-item>
          <q-separator v-show="$q.platform.is.desktop"/>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         "
                  v-if="$q.platform.is.desktop"
            clickable to="/staff/stafflist" @click="linkChange('staff')" v-ripple exact :active="link === 'staff'" :class="{ 'my-menu-link': link === 'staff' }">
            <q-item-section avatar>
              <q-icon name="assignment_ind" />
            </q-item-section>
            <q-item-section>
              {{ $t('menuItem.staff') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'StockControl'
                         "
                  v-if="$q.platform.is.desktop"
            clickable to="/driver/driverlist" @click="linkChange('driver')" v-ripple exact :active="link === 'driver'" :class="{ 'my-menu-link': link === 'driver' }">
            <q-item-section avatar>
              <q-icon name="img:statics/staff/driver.png" />
            </q-item-section>
            <q-item-section>
              {{ $t('menuItem.driver') }}
            </q-item-section>
          </q-item>
          <q-separator v-show="$q.platform.is.desktop"/>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Supervisor' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                          $q.localStorage.getItem('staff_type') !== 'StockControl' &&
                          $q.localStorage.getItem('staff_type') !== 'Manager' &&
                          $q.localStorage.getItem('staff_type') !== 'Admin'
                         "
                  v-if="$q.platform.is.desktop"
            clickable to="/customerdn" @click="linkChange('customerdn')" v-ripple exact :active="link === 'customerdn'" :class="{ 'my-menu-link': link === 'customerdn' }">
            <q-item-section avatar>
              <q-icon name="img:statics/outbound/dnlist.png" />
            </q-item-section>
            <q-item-section>
              {{ $t('menuItem.customerdn') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'StockControl'
                         "
                  v-if="$q.platform.is.cordova"
            clickable to="/scan_sorting" @click="linkChange('scan_sorting')" v-ripple exact :active="link === 'scan_sorting'" :class="{ 'my-menu-link': link === 'scan_sorting' }">
            <q-item-section avatar>
              <q-icon name="img:statics/inbound/preloadstock.png" />
            </q-item-section>
            <q-item-section>
              {{ $t('scan.scan_sorting') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                          $q.localStorage.getItem('staff_type') !== 'StockControl'
                         "
                  v-if="$q.platform.is.cordova"
            clickable to="/scan_uptobin" @click="linkChange('scan_uptobin')" v-ripple exact :active="link === 'scan_uptobin'" :class="{ 'my-menu-link': link === 'scan_uptobin' }">
            <q-item-section avatar>
              <q-icon name="img:statics/inbound/presortstock.png" />
            </q-item-section>
            <q-item-section>
              {{ $t('scan.scan_uptobin') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'StockControl'
                         "
                  v-if="$q.platform.is.cordova"
            clickable to="/scan_picking" @click="linkChange('scan_picking')" v-ripple exact :active="link === 'scan_picking'" :class="{ 'my-menu-link': link === 'scan_picking' }">
            <q-item-section avatar>
              <q-icon name="img:statics/outbound/picked.png" />
            </q-item-section>
            <q-item-section>
              {{ $t('scan.scan_picking') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'StockControl'
                         "
                  v-if="$q.platform.is.cordova"
                  clickable to="/scan_shipping" @click="linkChange('scan_shipping')" v-ripple exact :active="link === 'scan_shipping'" :class="{ 'my-menu-link': link === 'scan_shipping' }">
            <q-item-section avatar>
              <q-icon name="rv_hookup" />
            </q-item-section>
            <q-item-section>
              {{ $t('dispatch') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound'
                         "
                  v-if="$q.platform.is.cordova"
            clickable to="/scan_movetobin" @click="linkChange('scan_movetobin')" v-ripple exact :active="link === 'scan_movetobin'" :class="{ 'my-menu-link': link === 'scan_movetobin' }">
            <q-item-section avatar>
              <q-icon name="move_to_inbox" />
            </q-item-section>
            <q-item-section>
              {{ $t('movetobin') }}
            </q-item-section>
          </q-item>
          <q-separator v-show="$q.platform.is.cordova" />
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound'
                         "
                  v-if="$q.platform.is.cordova || $q.platform.is.mobile"
            clickable to="/scan_asn" @click="linkChange('scan_asn')" v-ripple exact :active="link === 'scan_asn'" :class="{ 'my-menu-link': link === 'scan_asn' }">
            <q-item-section avatar>
              <q-icon name="img:statics/inbound/asn.png" />
            </q-item-section>
            <q-item-section>
              {{ $t('scan.scan_asn') }}
            </q-item-section>
          </q-item>
                    <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound'
                         "
                  v-if="$q.platform.is.cordova || $q.platform.is.mobile"
            clickable to="/scan_dn" @click="linkChange('scan_dn')" v-ripple exact :active="link === 'scan_dn'" :class="{ 'my-menu-link': link === 'scan_dn' }">
            <q-item-section avatar>
              <q-icon name="img:statics/outbound/dnlist.png" />
            </q-item-section>
            <q-item-section>
              {{ $t('scan.scan_dn') }}
            </q-item-section>
          </q-item>
          <q-separator v-show="$q.platform.is.cordova"/>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                          $q.localStorage.getItem('staff_type') !== 'Outbound'
                         "
                  v-if="$q.platform.is.cordova || $q.platform.is.mobile"
            clickable to="/scan_emptybin" @click="linkChange('scan_emptybin')" v-ripple exact :active="link === 'scan_emptybin'" :class="{ 'my-menu-link': link === 'scan_emptybin' }">
            <q-item-section avatar>
              <q-icon name="all_out" />
            </q-item-section>
            <q-item-section>
              {{ $t('stock.emptybin') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         "
                  v-if="$q.platform.is.cordova || $q.platform.is.mobile"
            clickable to="/scan_stockbinlist" @click="linkChange('scan_stockbinlist')" v-ripple exact :active="link === 'scan_stockbinlist'" :class="{ 'my-menu-link': link === 'scan_stockbinlist' }">
            <q-item-section avatar>
              <q-icon name="img:statics/warehouse/binset.png" />
            </q-item-section>
            <q-item-section>
              {{ $t('stock.stockbinlist') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         "
                  v-if="$q.platform.is.cordova || $q.platform.is.mobile"
            clickable to="/scan_stocklist" @click="linkChange('scan_stocklist')" v-ripple exact :active="link === 'scan_stocklist'" :class="{ 'my-menu-link': link === 'scan_stocklist' }">
            <q-item-section avatar>
              <q-icon name="img:statics/stock/stocklist.png" />
            </q-item-section>
            <q-item-section>
              {{ $t('stock.stocklist') }}
            </q-item-section>
          </q-item>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Supplier'
                         "
                  v-if="$q.platform.is.cordova || $q.platform.is.mobile"
            clickable to="/scan_goodslist" @click="linkChange('scan_goodslist')" v-ripple exact :active="link === 'scan_goodslist'" :class="{ 'my-menu-link': link === 'scan_goodslist' }">
            <q-item-section avatar>
              <q-icon name="img:statics/goods/goodslist.png" />
            </q-item-section>
            <q-item-section>
              {{ $t('goods.goods_list') }}
            </q-item-section>
          </q-item>
          <q-separator v-show="$q.platform.is.cordova || $q.platform.is.mobile"/>
          <q-item v-show="$q.localStorage.getItem('staff_type') !== 'Customer' &&
                          $q.localStorage.getItem('staff_type') !== 'Supplier'
                         "
                  v-if="$q.platform.is.cordova || $q.platform.is.mobile"
            clickable to="/scan_stafflist" @click="linkChange('scan_stafflist')" v-ripple exact :active="link === 'scan_stafflist'" :class="{ 'my-menu-link': link === 'scan_stafflist' }">
            <q-item-section avatar>
              <q-icon name="perm_contact_calendar" />
            </q-item-section>
            <q-item-section>
              {{ $t('staff.staff') }}
            </q-item-section>
          </q-item>
          <q-separator v-show="$q.platform.is.cordova || $q.platform.is.mobile"/>
        </q-list>
      </q-scroll-area>
    </q-drawer>
    <q-page-container class="main-page" :style="{
       height: container_height,
       width: $q.screen.width
    }">
      <router-view />
    </q-page-container>
    <q-dialog v-model="chat">
    <q-card style="width: 600px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>{{ receiver }}</div>
        <q-space/>
        <q-btn dense flat icon="close" v-close-popup>
          <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px" @click="ChatClose()">{{ $t('index.close') }}</q-tooltip>
        </q-btn>
      </q-bar>
      <q-separator/>
      <q-card-section id="chat_scroll" style="max-height: 50vh; height: 50vh" class="scroll">
        <template>
          <div class="q-pa-md row justify-center">
            <q-btn flat rounded :label="$t('index.chat_more')" @click="LoadChatList()" v-show="chat_next !== null"></q-btn>
            <div style="width: 100%">
              <q-chat-message v-show="chat_next === null" :label="$t('index.chat_no_more')" />
              <div v-for="item in chat_list" :key="item.id">
                <q-chat-message v-if="item.sender === sender + '-' + openid"
                                :name="sender"
                                :text="[item.detail]"
                                bg-color="light-green-4"
                                name-sanitize
                                sent
                                text-sanitize
                />
                <q-chat-message v-else
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
      <q-separator/>
      <q-card-actions align="right">
        <q-input autofocus dense outlined square v-model="chat_text" placeholder="Send Message" class="bg-white col" @keyup.enter="websocketsend()" @keyup.esc="ChatClose()" />
        <q-btn flat :label="$t('index.chat_send')" color="primary" @click="websocketsend()"></q-btn>
      </q-card-actions>
    </q-card>
    </q-dialog>
    <q-dialog v-model="read" position="right">
      <q-card style="width: 300px">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
            <div>{{ $t('index.unread') }}({{ read_num }})</div>
            <q-space></q-space>
            <q-btn dense flat icon="close" v-close-popup>
                <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">{{ $t('index.close') }}</q-tooltip>
            </q-btn>
        </q-bar>
        <q-separator></q-separator>
        <q-card-section style="max-height: 50vh; height: 50vh" class="scroll">
          <q-list>
            <div v-for="item in read_list" :key="item.id">
              <q-item clickable v-ripple>
                <q-item-section>
                  <q-item-label @click="ChatWith(item.sender.split('-')[0])">{{ item.sender.split('-')[0] }}</q-item-label>
                  <q-item-label caption lines="2" @click="ChatWith(item.sender.split('-')[0])">{{ item.detail }}</q-item-label>
                </q-item-section>
              </q-item>
            </div>
          </q-list>
        </q-card-section>
        <q-separator v-show="read_num > 30"></q-separator>
        <q-card-actions align="left">
          <q-btn flat v-show="read_previous !== null" :label="$t('index.previous')" color="primary" @click="ReadnumPrevious()"></q-btn>
          <q-btn flat v-show="read_next !== null" :label="$t('index.next')" color="primary" @click="ReadnumNext()"></q-btn>
        </q-card-actions>
      </q-card>
  </q-dialog>
  <q-dialog v-model="authid" transition-show="jump-down" transition-hide="jump-up">
    <q-card style="min-width: 350px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>{{ $t('index.your_openid') }}</div>
        <q-space></q-space>
        <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">{{ $t('index.close') }}</q-tooltip>
        </q-btn>
      </q-bar>
      <q-card-section class="q-pt-md">
        <q-input dense outlined square label="Openid" v-model="openid" readonly />
      </q-card-section>
    </q-card>
  </q-dialog>
  <q-dialog v-model="friend" position="right">
    <q-card style="width: 300px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>{{ $t('index.contact_list') }}({{ friend_num }})</div>
        <q-space />
        <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">关闭</q-tooltip>
        </q-btn>
      </q-bar>
      <q-separator v-show="$q.platform.is.desktop"/>
      <q-card-section style="max-height: 50vh; height: 50vh" class="scroll">
        <q-list>
          <template v-for="item in friend_list">
            <q-item clickable v-ripple v-bind:key="item.id">
              <q-item-section>
                <q-item-label @click="ChatWith(item.staff_name)">{{ item.staff_name }}</q-item-label>
              </q-item-section>
            </q-item>
          </template>
        </q-list>
      </q-card-section>
      <q-separator v-show="friend_num > 30"></q-separator>
      <q-card-actions align="left">
        <q-btn flat v-show="friend_previous !== null" :label="$t('index.previous')" color="primary" @click="Friend_previous()"></q-btn>
        <q-btn flat v-show="friend_next !== null" :label="$t('index.next')" color="primary" @click="Friend_next()"></q-btn>
      </q-card-actions>
    </q-card>
  </q-dialog>
  <q-dialog v-model="login" transition-show="jump-down" transition-hide="jump-up">
    <q-card style="min-width: 350px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>{{ $t('index.user_login') }}</div>
        <q-space />
        <template v-if="admin">
          <q-btn dense flat :label="$t('index.user_login')" @click="admin = false">
              <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">{{ $t('index.user_login') }}</q-tooltip>
          </q-btn>
        </template>
        <template v-else-if="!admin">
          <q-btn dense flat :label="$t('index.admin_login')"  @click="admin = true">
              <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">{{ $t('index.admin_login') }}</q-tooltip>
          </q-btn>
        </template>
        <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">{{ $t('index.close') }}</q-tooltip>
        </q-btn>
      </q-bar>
      <q-card-section class="q-pt-md">
        <template v-if="admin">
          <q-input dense outlined square :label="$t('index.admin_name')" v-model="adminlogin.name" autofocus @keyup.enter="adminLogin()"/>
          <q-input dense outlined square :label="$t('index.password')"
                   :type="isPwd ? 'password' : 'text'"
                   v-model="adminlogin.password" @keyup.enter="adminLogin()" style="margin-top: 5px">
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
          <q-input dense outlined square :label="$t('index.your_openid')" v-model="openid" @keyup.enter="Login()"/>
          <q-input dense outlined square :label="$t('index.staff_name')" v-model="login_name" autofocus @keyup.enter="Login()" style="margin-top: 5px"/>
        </template>
      </q-card-section>
      <q-card-actions align="left" class="text-primary">
        <q-input v-show="!admin" v-model="check_code" dense style="width: 40%; margin-left: 10px"  @keyup.enter="Login()">
          <template v-slot:prepend>
            <div style="color: black; font-size: 15px!important">
              {{ $t('staff.check_code') }}
            </div>
          </template>
        </q-input>
        <q-space />
        <q-btn flat :label="$t('index.cancel')" v-close-popup />
        <template v-if="admin">
          <q-btn color="primary" :label="$t('index.login')" @click="adminLogin()"/>
        </template>
        <template v-if="!admin">
          <q-btn color="primary" :label="$t('index.login')" @click="Login()"/>
        </template>
      </q-card-actions>
    </q-card>
  </q-dialog>
<q-dialog v-model="register" transition-show="jump-down" transition-hide="jump-up">
    <q-card style="min-width: 350px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>{{ $t('index.register_tip') }}</div>
        <q-space></q-space>
        <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">{{ $t('index.close') }}</q-tooltip>
        </q-btn>
      </q-bar>
      <q-card-section class="q-pt-md">
        <q-input dense outlined square :label="$t('index.staff_name')" v-model="registerform.name" autofocus @keyup.enter="Register()"/>
        <q-input dense outlined square
                 :label="$t('index.password')" v-model="registerform.password1"
                 :type="isPwd ? 'password' : 'text'"
                 @keyup.enter="Register()" style="margin-top: 5px">
          <template v-slot:append>
            <q-icon
              :name="isPwd ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwd = !isPwd"
            />
          </template>
        </q-input>
        <q-input dense outlined square
                 :label="$t('index.confirm_password')" v-model="registerform.password2"
                 :type="isPwd2 ? 'password' : 'text'"
                 @keyup.enter="Register()" style="margin-top: 5px">
          <template v-slot:append>
            <q-icon
              :name="isPwd2 ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwd2 = !isPwd2"
            />
          </template>
        </q-input>
      </q-card-section>
      <q-card-actions align="right" class="text-primary">
        <q-btn flat :label="$t('index.cancel')" v-close-popup />
        <q-btn color="primary" :label="$t('index.register')" @click="Register()"/>
      </q-card-actions>
    </q-card>
  </q-dialog>
    <q-dialog v-model="verCheck" transition-show="jump-down" transition-hide="jump-up" persistent>
    <q-card style="min-width: 350px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>{{ $t('index.updatetitle') }}</div>
        <q-space></q-space>
        <q-btn dense flat icon="close" v-close-popup @click="NewVersionignore()">
            <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">{{ $t('index.close') }}</q-tooltip>
        </q-btn>
      </q-bar>
      <q-card-section class="q-pt-md">
        {{ version }} {{ $t('index.updatedesc') }}
      </q-card-section>
      <q-card-actions align="right" class="text-primary">
        <q-btn v-show="!downloadprocess" flat :label="$t('index.cancel')" v-close-popup @click="NewVersionignore()" />
        <q-btn v-show="!downloadprocess" color="primary" :label="$t('index.download')" @click="NewVersionDownload()"/>
        <q-linear-progress v-show="downloadprocess" size="25px" :value="(processpercent / 100)" color="accent">
          <div class="absolute-full flex flex-center">
            <q-badge color="white" text-color="accent" :label="processpercent.toFixed(2) + '' + '%' " />
          </div>
        </q-linear-progress>
      </q-card-actions>
    </q-card>
  </q-dialog>
    <q-dialog v-model="updateNow" transition-show="jump-down" transition-hide="jump-up" persistent>
    <q-card style="min-width: 350px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>{{ $t('index.updatetitle') }}</div>
        <q-space></q-space>
      </q-bar>
      <q-card-section class="q-pt-md">
        {{ version }} {{ $t('index.updatedesc') }}
      </q-card-section>
      <q-card-actions align="right" class="text-primary">
        <q-btn color="primary" :label="$t('index.update')" @click="NewVersionUpdate()"/>
      </q-card-actions>
    </q-card>
  </q-dialog>
  </q-layout>
</template>
<script>
import { versioncheck, getauth, post, wsurl } from 'boot/axios_request'
import { date, LocalStorage, openURL } from 'quasar'

var ws
export default {
  data () {
    return {
      lang: this.$i18n.locale,
      verCheck: false,
      version: '',
      updateNow: false,
      processpercent: 0,
      downloadprocess: false,
      container_height: '',
      langOptions: [
        { value: 'en-us', label: 'English' },
        { value: 'zh-hans', label: '中文简体' },
        { value: 'zh-hant', label: '中文繁體' },
        { value: 'ja', label: '日本語' }
      ],
      title: this.$t('index.webtitle'),
      admin: false,
      adminlogin: {
        name: '',
        password: ''
      },
      openid: '',
      isPwd: true,
      isPwd2: true,
      authin: '0',
      authid: false,
      left: false,
      drawerleft: false,
      miniState: true,
      tab: '',
      login: false,
      link: localStorage.getItem('menulink'),
      login_name: '',
      check_code: '',
      register: false,
      registerform: {
        name: '',
        password1: '',
        password2: ''
      },
      friend: false,
      friend_num: 0,
      friend_list: [],
      friend_previous: null,
      friend_next: null,
      sender: '',
      receiver: '',
      chat: false,
      chat_list: [],
      chat_text: '',
      chat_next: null,
      read: false,
      read_num: 0,
      read_list: [],
      read_previous: '',
      read_next: ''
    }
  },
  meta () {
    var _this = this
    return {
      title: _this.title
    }
  },
  methods: {
    linkChange (e) {
      var _this = this
      localStorage.setItem('menulink', e)
      _this.link = e
    },
    drawerClick (e) {
      var _this = this
      if (_this.miniState) {
        _this.miniState = false
        e.stopPropagation()
      }
    },
    brownlink (e) {
      openURL(e)
    },
    Login () {
      var _this = this
      if (_this.login_name === '') {
        _this.$q.notify({
          message: 'Please enter the login name',
          color: 'negative',
          icon: 'close'
        })
      } else {
        if (_this.openid === '') {
          _this.$q.notify({
            message: 'Please Enter The Openid',
            icon: 'close',
            color: 'negative'
          })
        } else {
          if (_this.check_code === '') {
            _this.$q.notify({
              message: 'Please Enter The Check Code',
              icon: 'close',
              color: 'negative'
            })
          } else {
            _this.$q.localStorage.set('openid', _this.openid)
            getauth('staff/?staff_name=' + _this.login_name + '&check_code=' + _this.check_code).then(res => {
              if (res.count === 1) {
                _this.authin = '1'
                _this.login = false
                _this.$q.localStorage.set('auth', '1')
                _this.$q.localStorage.set('login_name', _this.login_name)
                _this.$q.notify({
                  message: 'Success Login',
                  icon: 'check',
                  color: 'green'
                })
                window.location.reload()
              } else {
                _this.$q.notify({
                  message: "No User's Data Or Check Code Wrong",
                  icon: 'close',
                  color: 'negative'
                })
              }
            }).catch(err => {
              _this.$q.notify({
                message: err.detail,
                icon: 'close',
                color: 'negative'
              })
            })
          }
        }
      }
    },
    adminLogin () {
      var _this = this
      if (_this.admin_name === '') {
        _this.$q.notify({
          message: 'Please enter the admin name',
          color: 'negative',
          icon: 'close'
        })
      } else {
        if (_this.admin_password === '') {
          _this.$q.notify({
            message: 'Please enter the admin password',
            icon: 'close',
            color: 'negative'
          })
        } else {
          post('login/', _this.adminlogin).then(res => {
            if (res.code === '200') {
              _this.authin = '1'
              _this.login = false
              _this.admin = false
              _this.openid = res.data.openid
              _this.login_name = res.data.name
              _this.$q.localStorage.set('auth', '1')
              _this.$q.localStorage.set('openid', res.data.openid)
              _this.$q.localStorage.set('login_name', _this.login_name)
              _this.$q.notify({
                message: 'Success Login',
                icon: 'check',
                color: 'green'
              })
              window.location.reload()
            } else {
              _this.$q.notify({
                message: "No user's Data",
                icon: 'close',
                color: 'negative'
              })
            }
          }).catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
        }
      }
    },
    Logout () {
      var _this = this
      _this.authin = '0'
      _this.login_name = ''
      _this.$q.localStorage.remove('auth')
      _this.$q.localStorage.set('login_name', '')
      _this.$q.notify({
        message: 'Success Logout',
        icon: 'check',
        color: 'negative'
      })
      _this.staffType()
      window.location.reload()
    },
    Register () {
      var _this = this
      post('register/', _this.registerform).then(res => {
        if (res.code === '200') {
          _this.register = false
          _this.openid = res.data.openid
          _this.login_name = _this.registerform.name
          _this.authin = '1'
          _this.$q.localStorage.set('openid', res.data.openid)
          _this.$q.localStorage.set('login_name', _this.registerform.name)
          _this.$q.localStorage.set('auth', '1')
          _this.registerform = {
            name: '',
            password1: '',
            password2: ''
          }
          _this.$q.notify({
            message: res.msg,
            icon: 'check',
            color: 'green'
          })
          _this.staffType()
          window.location.reload()
        } else {
          _this.$q.notify({
            message: res.msg,
            icon: 'close',
            color: 'negative'
          })
        }
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    staffType () {
      var _this = this
      getauth('staff/?staff_name=' + _this.login_name).then(res => {
        _this.$q.localStorage.set('staff_type', res.results[0].staff_type)
      })
    },
    initWebSocket () {
      var _this = this
      ws = new WebSocket(wsurl + '?sender=' + _this.login_name + '&receiver=' + _this.receiver + '&openid=' + _this.openid)
      ws.onmessage = _this.websocketonmessage
      ws.onopen = _this.websocketonopen
      ws.onerror = _this.websocketonerror
      ws.onclose = _this.websocketclose
    },
    websocketonopen () {
      console.log('Success Connect')
    },
    websocketonerror () {
      var _this = this
      _this.initWebSocket()
    },
    websocketonmessage (e) {
      var _this = this
      if (_this.$q.sessionStorage.getItem('receiver') === JSON.parse(e.data).sender) {
        _this.chat_list.push(JSON.parse(e.data))
      } else {
      }
      _this.Readnum()
      _this.$q.notify({
        message: JSON.parse(e.data).sender + ' Send you a message',
        color: 'deep-purple',
        icon: 'textsms',
        position: 'right',
        actions: [
          {
            label: 'View',
            color: 'yellow',
            handler: () => {
              _this.ChatWith(JSON.parse(e.data).sender)
            }
          }
        ]
      })
    },
    websocketsend () {
      var _this = this
      if (_this.chat_text === '') {
      } else {
        ws.send(_this.chat_text)
        _this.chat_list.push({
          sender: _this.sender + '-' + _this.openid,
          receiver: _this.receiver,
          detail: _this.chat_text,
          create_time: date.formatDate(Date.now(), 'YYYY-MM-DD HH:mm:ss')
        })
        _this.chat_text = ''
      }
    },
    websocketclose (e) {
      console.log('Disconnect', e)
    },
    ChatWith (e) {
      var _this = this
      _this.sender = _this.login_name
      _this.receiver = e
      _this.$q.sessionStorage.set('receiver', e)
      if (_this.sender === _this.receiver) {
        _this.$q.notify({
          message: 'Cannot Chat with yourself',
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.chat = true
        _this.chat_text = ''
        _this.initWebSocket()
        getauth('chat/?' + 'sender=' + _this.sender + '&receiver=' + _this.receiver).then(res => {
          _this.chat_list = res.results.reverse()
          _this.Readnum()
          _this.chat_next = res.next
        }).catch(err => {
          console.log(err)
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      }
    },
    LoadChatList () {
      var _this = this
      getauth(_this.chat_next).then(res => {
        res.results.forEach(c => {
          _this.chat_list.unshift(c)
        })
        _this.chat_next = res.next
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    ChatClose () {
      var _this = this
      _this.receiver = ''
      _this.$q.sessionStorage.set('receiver', '')
      _this.chat_list = []
      _this.chat_text = ''
      _this.chat_next = null
    },
    Readnum () {
      var _this = this
      getauth('chat/read/?' + 'sender=' + _this.login_name).then(res => {
        _this.read_previous = res.previous
        _this.read_next = res.next
        _this.read_list = res.results
        _this.read_num = res.count
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    ReadnumPrevious () {
      var _this = this
      getauth(_this.read_previous, {
      }).then(res => {
        _this.read_list = res.results
        _this.read_previous = res.previous
        _this.read_next = res.next
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    ReadnumNext () {
      var _this = this
      getauth(_this.read_next, {
      }).then(res => {
        _this.read_list = res.results
        _this.read_previous = res.previous
        _this.read_next = res.next
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    Friend () {
      var _this = this
      _this.friend = true
      getauth('staff/', {
      }).then(res => {
        _this.friend_list = res.results
        _this.friend_previous = res.previous
        _this.friend_next = res.next
        _this.friend_num = res.count
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    Friend_previous () {
      var _this = this
      getauth(_this.friend_previous, {
      }).then(res => {
        _this.friend_list = res.results
        _this.friend_previous = res.previous
        _this.friend_next = res.next
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    Friend_next () {
      var _this = this
      getauth(_this.friend_next, {
      }).then(res => {
        _this.friend_list = res.results
        _this.friend_previous = res.previous
        _this.friend_next = res.next
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    langChange (e) {
      var _this = this
      _this.lang = e
      window.setTimeout(() => {
        location.reload()
      }, 1)
    },
    NewVersionignore () {
      var _this = this
      _this.verCheck = false
      _this.version = ''
    },
    NewVersionDownload () {
      var _this = this
      _this.version = ''
      require('electron').ipcRenderer.send('downloadUpdate')
      console.log(_this.processpercent)
      if (_this.processpercent === 100) {
        _this.verCheck = false
        _this.downloadprocess = false
      } else {
        _this.downloadprocess = true
      }
    },
    NewVersionUpdate () {
      var _this = this
      require('electron').ipcRenderer.send('updateNow')
      _this.updateNow = false
    }
  },
  created () {
    var _this = this
    if (_this.$q.platform.is.cordova || _this.$q.platform.is.mobile) {
      _this.container_height = _this.$q.screen.height - 90 + '' + 'px'
    } else {
      _this.container_height = _this.$q.screen.height
    }
    if (_this.$q.localStorage.has('openid')) {
      _this.openid = _this.$q.localStorage.getItem('openid')
    } else {
      _this.openid = ''
      _this.$q.localStorage.set('openid', '')
    }
    if (_this.$q.localStorage.has('login_name')) {
      _this.login_name = _this.$q.localStorage.getItem('login_name')
    } else {
      _this.login_name = ''
      _this.$q.localStorage.set('login_name', '')
    }
    if (_this.$q.localStorage.has('auth')) {
      _this.authin = '1'
      _this.initWebSocket()
      _this.staffType()
      _this.Readnum()
    } else {
      _this.$q.localStorage.set('staff_type', 'Admin')
      _this.authin = '0'
    }
  },
  mounted () {
    var _this = this
    if (_this.$q.platform.is.electron) {
      if (LocalStorage.has('openid')) {
        versioncheck('vcheck/' + '?openid=' + LocalStorage.getItem('openid') + '&platform=' + process.platform).then(res => {
          if (!res.detail) {
            const ipcRenderer = require('electron').ipcRenderer
            window.setTimeout(() => {
              ipcRenderer.send('checkForUpdate', res.upurl.toString())
            }, 1000)
            ipcRenderer.on('message', (event, arg) => {
              if (arg.cmd === 'update-available') {
                _this.verCheck = true
                _this.version = arg.message.version
              } else if (arg.cmd === 'download-progress') {
                _this.processpercent = arg.message.percent
              } else if (arg.cmd === 'update-downloaded') {
                _this.processpercent = 100
                _this.verCheck = false
                _this.downloadprocess = false
                _this.updateNow = true
              } else if (arg.cmd === 'check') {
                console.log(arg)
              }
            })
            clearTimeout()
          }
        }).catch(err => {
          console.log(err)
        })
      }
    }
  },
  updated () {
    if (document.getElementById('chat_scroll')) {
      document.getElementById('chat_scroll').scrollTop = document.getElementById('chat_scroll').scrollHeight
    } else if (document.getElementById('m_chat_scroll')) {
      document.getElementById('m_chat_scroll').scrollTop = document.getElementById('m_chat_scroll').scrollHeight
    } else {
    }
  },
  beforeDestroy () {
    require('electron').ipcRenderer.removeAllListeners(['message', 'updateNow', 'downloadUpdate', 'checkForUpdate'])
  },
  destroyed () {
    if (ws) {
      if (ws.readyState === ws.OPEN) {
        ws.close()
      }
    }
  },
  watch: {
    lang (lang) {
      var _this = this
      LocalStorage.set('lang', lang)
      _this.$i18n.locale = lang
    }
  }
}
</script>
