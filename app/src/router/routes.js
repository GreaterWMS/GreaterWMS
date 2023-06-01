
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'home', component: () => import('pages/IndexPage.vue') },
      { path: 'server', name: 'server', component: () => import('pages/settings/SettingsServer.vue') },
      { path: 'login', name: 'login', component: () => import('pages/UserLogin.vue') },
      { path: 'scanapp', name: 'scanapp', component: () => import('pages/ScanAPP.vue'),
        children: [
          { path: 'goods', name: 'goods', component: () => import('pages/inventory/GoodsQuery.vue') },
          { path: 'goodsstock', name: 'goodsstock', component: () => import('pages/inventory/GoodsStock.vue') },
          { path: 'binstock', name: 'binstock', component: () => import('pages/inventory/BinStock.vue') },
          { path: 'emptybin', name: 'emptybin', component: () => import('pages/inventory/EmptyBin.vue') },
          { path: 'handcount', name: 'handcount', component: () => import('pages/inventory/HandCount.vue') },
          { path: 'asnlist', name: 'asnlist', component: () => import('pages/asn/AsnList.vue') },
          { path: 'asndetail', name: 'asndetail', component: () => import('pages/asn/AsnDetail.vue') },
          { path: 'dnlist', name: 'dnlist', component: () => import('pages/dn/DNList.vue') },
          { path: 'dndetail', name: 'dndetail', component: () => import('pages/dn/DNDetail.vue') },
          { path: 'pickinglist', name: 'pickinglist', component: () => import('pages/dn/PickingList.vue') },
          { path: 'equipment', name: 'equipment', component: () => import('pages/settings/EquipmentSupport.vue') }
        ]
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
