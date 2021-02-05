
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'index',
        component: () => import('pages/Index.vue')
      },
      {
        path: 'dashboard',
        name: 'dashboard',
        component: () => import('pages/dashboard/dashboard.vue'),
        children: [
          {
            path: 'sales',
            name: 'sales',
            component: () => import('pages/dashboard/sales.vue')
          }
        ]
      },
      {
        path: 'inbound',
        name: 'inbound',
        component: () => import('pages/inbound/inbound.vue'),
        children: [
          {
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
        children: [
          {
            path: 'dn',
            name: 'dn',
            component: () => import('pages/outbound/dn.vue')
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
            path: 'shippedstock',
            name: 'shippedstock',
            component: () => import('pages/outbound/shippedstock.vue')
          },
          {
            path: 'backorder',
            name: 'backorder',
            component: () => import('pages/outbound/backorder.vue')
          }
        ]
      },
      {
        path: 'stock',
        name: 'stock',
        component: () => import('pages/stock/stock.vue'),
        children: [
          {
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
          }
        ]
      },
      {
        path: 'goods',
        name: 'goods',
        component: () => import('pages/goods/goods.vue'),
        children: [
          {
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
        children: [
          {
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
        children: [
          {
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
        children: [
          {
            path: 'capitallist',
            name: 'capitallist',
            component: () => import('pages/finance/capitallist.vue')
          }
        ]
      },
      {
        path: 'staff',
        name: 'staff',
        component: () => import('pages/staff/staff.vue'),
        children: [
          {
            path: 'stafflist',
            name: 'stafflist',
            component: () => import('pages/staff/stafflist.vue')
          },
          {
            path: 'staffauth',
            name: 'staffauth',
            component: () => import('pages/staff/staffauth.vue')
          }
        ]
      },
      {
        path: 'driver',
        name: 'driver',
        component: () => import('pages/driverlist/driver.vue'),
        children: [
          {
            path: 'driverlist',
            name: 'driverlist',
            component: () => import('pages/driverlist/driverlist.vue')
          }
        ]
      }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
