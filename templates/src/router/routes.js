const routes = [{
  path: '/',
  component: () => import('layouts/MainLayout.vue'),
  children: [{
      path: '',
      name: 'index',
      component: () => import('pages/Index.vue')
    },
    {
      path: 'dashboard',
      name: 'dashboard',
      component: () => import('pages/dashboard/dashboard.vue'),
      children: [{
          path: 'outbounddashboard',
          name: 'outbounddashboard',
          component: () => import('pages/dashboard/outbound.vue')
        },
        {
          path: 'inbounddashboard',
          name: 'inbounddashboard',
          component: () => import('pages/dashboard/inbound.vue')
        },
        {
          path: 'inboundAndOutbound',
          name: 'inboundAndOutbound',
          component: () => import('pages/dashboard/inboundAndOutbound.vue')
        }
      ]
    },
    {
      path: 'inbound',
      name: 'inbound',
      component: () => import('pages/inbound/inbound.vue'),
      children: [{
          path: 'asn',
          name: 'asn',
          component: () => import('pages/inbound/asn.vue')
        },
        {
          path: 'predeliverystock',
          name: 'predeliverystock',
          component: () => import('pages/inbound/predeliverystock.vue')
        },
        {
          path: 'preloadstock',
          name: 'preloadstock',
          component: () => import('pages/inbound/preloadstock.vue')
        },
        {
          path: 'presortstock',
          name: 'presortstock',
          component: () => import('pages/inbound/presortstock.vue')
        },
        {
          path: 'sortstock',
          name: 'sortstock',
          component: () => import('pages/inbound/sortstock.vue')
        },
        {
          path: 'shortage',
          name: 'shortage',
          component: () => import('pages/inbound/shortage.vue')
        },
        {
          path: 'more',
          name: 'more',
          component: () => import('pages/inbound/more.vue')
        },
        {
          path: 'asnfinish',
          name: 'asnfinish',
          component: () => import('pages/inbound/asnfinish.vue')
        }
      ]
    },
    {
      path: 'outbound',
      name: 'outbound',
      component: () => import('pages/outbound/outbound.vue'),
      children: [{
          path: 'dn',
          name: 'dn',
          component: () => import('pages/outbound/dn.vue')
        },
        {
          path: 'freshorder',
          name: 'freshorder',
          component: () => import('pages/outbound/freshorder.vue')
        },
        {
          path: 'neworder',
          name: 'neworder',
          component: () => import('pages/outbound/neworder.vue')
        },
        {
          path: 'pickstock',
          name: 'pickstock',
          component: () => import('pages/outbound/pickstock.vue')
        },
        {
          path: 'pickedstock',
          name: 'pickedstock',
          component: () => import('pages/outbound/pickedstock.vue')
        },
        {
          path: 'pickinglist',
          name: 'pickinglist',
          component: () => import('pages/outbound/pickinglist.vue')
        },
        {
          path: 'shippedstock',
          name: 'shippedstock',
          component: () => import('pages/outbound/shippedstock.vue')
        },
        {
          path: 'backorder',
          name: 'backorder',
          component: () => import('pages/outbound/backorder.vue')
        },
        {
          path: 'pod',
          name: 'pod',
          component: () => import('pages/outbound/pod.vue')
        }
      ]
    },
    {
      path: 'stock',
      name: 'stock',
      component: () => import('pages/stock/stock.vue'),
      children: [{
          path: 'stocklist',
          name: 'stocklist',
          component: () => import('pages/stock/stocklist.vue')
        },
        {
          path: 'stockbinlist',
          name: 'stockbinlist',
          component: () => import('pages/stock/stockbinlist.vue')
        },
        {
          path: 'emptybin',
          name: 'emptybin',
          component: () => import('pages/stock/emptybin.vue')
        },
        {
          path: 'occupiedbin',
          name: 'occupiedbin',
          component: () => import('pages/stock/occupiedbin.vue')
        },
        {
          path: 'cyclecount',
          name: 'cyclecount',
          component: () => import('pages/stock/cyclecount.vue')
        },
        {
          path: 'cyclecountrecorder',
          name: 'cyclecountrecorder',
          component: () => import('pages/stock/cyclecountrecorder.vue')
        }
      ]
    },
    {
      path: 'goods',
      name: 'goods',
      component: () => import('pages/goods/goods.vue'),
      children: [{
          path: 'goodslist',
          name: 'goodslist',
          component: () => import('pages/goods/goodslist.vue')
        },
        {
          path: 'goodsunit',
          name: 'goodsunit',
          component: () => import('pages/goods/goodsunit.vue')
        },
        {
          path: 'goodsclass',
          name: 'goodsclass',
          component: () => import('pages/goods/goodsclass.vue')
        },
        {
          path: 'goodsbrand',
          name: 'goodsbrand',
          component: () => import('pages/goods/goodsbrand.vue')
        },
        {
          path: 'goodscolor',
          name: 'goodscolor',
          component: () => import('pages/goods/goodscolor.vue')
        },
        {
          path: 'goodsspecs',
          name: 'goodsspecs',
          component: () => import('pages/goods/goodsspecs.vue')
        },
        {
          path: 'goodsshape',
          name: 'goodsshape',
          component: () => import('pages/goods/goodsshape.vue')
        },
        {
          path: 'goodsorigin',
          name: 'goodsorigin',
          component: () => import('pages/goods/goodsorigin.vue')
        }
      ]
    },
    {
      path: 'baseinfo',
      name: 'baseinfo',
      component: () => import('pages/baseinfo/baseinfo.vue'),
      children: [{
          path: 'company',
          name: 'company',
          component: () => import('pages/baseinfo/company.vue')
        },
        {
          path: 'supplier',
          name: 'supplier',
          component: () => import('pages/baseinfo/supplier.vue')
        },
        {
          path: 'customer',
          name: 'customer',
          component: () => import('pages/baseinfo/customer.vue')
        }
      ]
    },
    {
      path: 'warehouse',
      name: 'warehouse',
      component: () => import('pages/warehouse/warehouse.vue'),
      children: [{
          path: 'warehouseset',
          name: 'warehouseset',
          component: () => import('pages/warehouse/warehouseset.vue')
        },
        {
          path: 'binset',
          name: 'binset',
          component: () => import('pages/warehouse/binset.vue')
        },
        {
          path: 'binsize',
          name: 'binsize',
          component: () => import('pages/warehouse/binsize.vue')
        },
        {
          path: 'property',
          name: 'property',
          component: () => import('pages/warehouse/property.vue')
        }
      ]
    },
    {
      path: 'finance',
      name: 'finance',
      component: () => import('pages/finance/finance.vue'),
      children: [{
          path: 'capitallist',
          name: 'capitallist',
          component: () => import('pages/finance/capitallist.vue')
        },
        {
          path: 'freight',
          name: 'freight',
          component: () => import('pages/finance/freight.vue')
        }
      ]
    },
    {
      path: 'staff',
      name: 'staff',
      component: () => import('pages/staff/staff.vue'),
      children: [{
          path: 'stafflist',
          name: 'stafflist',
          component: () => import('pages/staff/stafflist.vue')
        },
        {
          path: 'stafflist_check_code',
          name: 'stafflist_check_code',
          component: () => import('pages/staff/stafflist_check_code.vue')
        },
        {
          path: 'stafftype',
          name: 'stafftype',
          component: () => import('pages/staff/stafftype.vue')
        }
      ]
    },
    {
      path: 'driver',
      name: 'driver',
      component: () => import('pages/driverlist/driver.vue'),
      children: [{
          path: 'driverlist',
          name: 'driverlist',
          component: () => import('pages/driverlist/driverlist.vue')
        },
        {
          path: 'dispatchlist',
          name: 'dispatchlist',
          component: () => import('pages/driverlist/dispatchlist.vue')
        }
      ]
    },
    {
      path: 'customerdn',
      name: 'customerdn',
      component: () => import('pages/customerdn/customer.vue'),
      children: [{
          path: 'customerdnlist',
          name: 'customerdnlist',
          component: () => import('pages/customerdn/customerdnlist.vue')
        },
        {
          path: 'customerpod',
          name: 'customerpod',
          component: () => import('pages/customerdn/pod.vue')
        }
      ]
    },
    {
      path: 'supplierasn',
      name: 'supplierasn',
      component: () => import('pages/supplierasn/supplier.vue'),
      children: [{
          path: 'supplierasnlist',
          name: 'supplierasnlist',
          component: () => import('pages/supplierasn/supplierasnlist.vue')
        },
        {
          path: 'supplierasnfinish',
          name: 'supplierasnfinish',
          component: () => import('pages/supplierasn/supplierasnfinish.vue')
        }
      ]
    },
    {
      path: 'zebra_goodslist',
      name: 'zebra_goodslist',
      component: () => import('pages/scan/zebra_goodslist.vue')
    },
    {
      path: 'zebra_stocklist',
      name: 'zebra_stocklist',
      component: () => import('pages/scan/zebra_stocklist.vue')
    },
    {
      path: 'zebra_movetobin',
      name: 'zebra_movetobin',
      component: () => import('pages/scan/zebra_movetobin.vue')
    },
    {
      path: 'zebra_shipping',
      name: 'zebra_shipping',
      component: () => import('pages/scan/zebra_shipping.vue')
    },
    {
      path: 'zebra_picking',
      name: 'zebra_picking',
      component: () => import('pages/scan/zebra_picking.vue')
    },
    {
      path: 'zebra_uptobin',
      name: 'zebra_uptobin',
      component: () => import('pages/scan/zebra_uptobin.vue')
    },
    {
      path: 'zebra_sorting',
      name: 'zebra_sorting',
      component: () => import('pages/scan/zebra_sorting.vue')
    },
    {
      path: 'zebra_cyclecount',
      name: 'zebra_cyclecount',
      component: () => import('pages/scan/zebra_cyclecount.vue')
    },
    {
      path: 'zebra_cyclecount',
      name: 'zebra_cyclecount',
      component: () => import('pages/scan/zebra_cyclecount.vue')
    },
    {
      path: 'zebra_locationquery',
      name: 'zebra_locationquery',
      component: () => import('pages/scan/zebra_locationquery.vue')
    },
    // urova
    {
      path: 'urovo_goodslist',
      name: 'urovo_goodslist',
      component: () => import('pages/scan/urovo_goodslist.vue')
    },
    {
      path: 'urovo_stocklist',
      name: 'urovo_stocklist',
      component: () => import('pages/scan/urovo_stocklist.vue')
    },
    {
      path: 'urovo_movetobin',
      name: 'urovo_movetobin',
      component: () => import('pages/scan/urovo_movetobin.vue')
    },
    {
      path: 'urovo_shipping',
      name: 'urovo_shipping',
      component: () => import('pages/scan/urovo_shipping.vue')
    },
    {
      path: 'urovo_picking',
      name: 'urovo_picking',
      component: () => import('pages/scan/urovo_picking.vue')
    },
    {
      path: 'urovo_uptobin',
      name: 'urovo_uptobin',
      component: () => import('pages/scan/urovo_uptobin.vue')
    },
    {
      path: 'urovo_sorting',
      name: 'urovo_sorting',
      component: () => import('pages/scan/urovo_sorting.vue')
    },
    {
      path: 'urovo_cyclecount',
      name: 'urovo_cyclecount',
      component: () => import('pages/scan/urovo_cyclecount.vue')
    },
    {
      path: 'urovo_locationquery',
      name: 'urovo_locationquery',
      component: () => import('pages/scan/urovo_locationquery.vue')
    },
    {
      path: 'uploadcenter',
      name: 'uploadcenter',
      component: () => import('pages/uploadcenter/upload.vue'),
      children: [{
          path: 'initializeupload',
          name: 'initializeupload',
          component: () => import('pages/uploadcenter/initializeupload.vue')
        },
        {
          path: 'addupload',
          name: 'addupload',
          component: () => import('pages/uploadcenter/addupload.vue')
        }
      ]
    }
  ]
}]

routes.push({
  path: '/',
  component: () => import('layouts/MainLayout.vue'),
  children: []
})

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
