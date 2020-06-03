
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: 'inbound',
        name: 'inbound',
        component: () => import('pages/Index.vue')
      },
      {
        path: '',
        name: 'index',
        component: () => import('pages/Index.vue')
      },
      {
        path: 'simorder',
        name: 'simorder',
        component: () => import('pages/simorder.vue')
      },
      {
        path: 'stockanalyst',
        name: 'stockanalyst',
        component: () => import('pages/stockanalyst.vue')
      },
      {
        path: 'staff',
        name: 'staff',
        component: () => import('pages/staff.vue')
      },
      {
        path: 'shipping',
        name: 'shipping',
        component: () => import('pages/shipping.vue')
      },
      {
        path: 'goods',
        name: 'goods',
        component: () => import('pages/goods.vue')
      },
      {
        path: 'basicinfo',
        name: 'basicinfo',
        component: () => import('pages/basicinfo.vue')
      },
      {
        path: 'hscode',
        name: 'hscode',
        component: () => import('pages/Index.vue')
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
