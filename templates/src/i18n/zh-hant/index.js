// This is just an example,
// so you can safely delete all default props below

export default {
  failed: 'Action failed',
  success: 'Action was successful',
  index: {
    webtitle: 'GreaterWMS--開源倉庫管理系統',
    home: '首頁',
    title: 'GreaterWMS',
    title_tip: 'GreaterWMS首頁',
    hide_menu: '收起選單',
    api: 'API檔案',
    translate: '更改語言',
    unread: '未讀消息',
    login: '登入',
    register: '注册',
    login_tip: '輸入你的OPENID和用戶名',
    register_tip: '注册成為管理員',
    logout: '退出登入',
    user_login: '用戶登入',
    admin_login: '管理員登入',
    user_center: '用戶中心',
    change_user: '更改用戶',
    view_my_openid: '查看我的OPENID',
    your_openid: '你的OPENID',
    contact_list: '最近聯繫人',
    chat_more: '更多歷史消息',
    chat_no_more: '沒有更多消息',
    chat_send: '發送',
    previous: '上一頁',
    next: '下一頁',
    admin_name: '管理員',
    password: '密碼',
    confirm_password: '確認密碼',
    staff_name: '用戶名',
    cancel: '取消',
    close: '關閉',
    submit: '提交',
    download: '下載',
    updatetitle: '升級就緒',
    updatedesc: '版本已經升級準備就緒',
    update: '馬上更新'
  },
  menuItem: {
    dashboard: '報表中心',
    inbound: '收貨管理',
    outbound: '發貨管理',
    stock: '庫存管理',
    finance: '財務中心',
    goods: '商品管理',
    baseinfo: '基本設置',
    warehouse: '倉庫設置',
    staff: '用戶管理',
    driver: '司機管理',
    customerdn: '客戶訂單',
    supplierasn: '供應商訂單'
  },
  contact: '立即溝通',
  sendmessage: '給他發一條消息',
  send: '發送',
  nomoremessage: '沒有更多消息',
  loadmore: '加載更多',
  new: '新增',
  newtip: '新增一條數據',
  refresh: '刷新',
  refreshtip: '刷新所有數據',
  edit: '編輯這條數據',
  confirmedit: '確認編輯數據',
  canceledit: '取消編輯數據',
  delete: '刪除這條數據',
  deletetip: '此操作不可逆。 ',
  confirmdelete: '確認刪除數據',
  canceldelete: '取消刪除數據',
  download: '下載',
  downloadtip: '下載所有數據',
  frombin: '從庫位',
  movetobin: '移庫',
  uptobin: '上架',
  cyclecount: '動態盤點',
  cyclecountrecorder: '盤點記錄',
  search: '關鍵字搜索',
  creater: '創建人',
  createtime: '創建時間',
  updatetime: '更新時間',
  action: '操作',
  previous: '上一頁',
  next: '下一頁',
  no_data: '沒有更多數據',
  submit: '確認',
  cancel: '取消',
  estimate: '預估運費',
  downloadasnlist: '下載列表',
  downloadasndetail: '下載明細',
  downloadasnlisttip: '下載到貨通知書列表',
  downloadasndetailtip: '下載到貨通知書明細',
  printthisasn: '查看到貨通知書',
  confirmdelivery: '確認ASN已經到貨 ',
  finishloading: '確認卸貨完成 ',
  confirmsorted: '確認分揀完成 ',
  downloaddnlist: '下載列表',
  downloaddndetail: '下載明細',
  downloaddnlisttip: '下載發貨單列表',
  downloaddndetailtip: '下載發貨單明細',
  release: '匹配訂單',
  releaseallorder: '全部生成揀貨單',
  releaseorder: '生成揀貨單',
  print: '打印揀貨單',
  printthisdn: '查看和打印發貨單',
  confirmorder: '確認訂單',
  confirmpicked: '確認揀貨完成',
  dispatch: '發貨',
  deletebackorder: '刪除欠貨訂單',
  baseinfo: {
    company_info: '公司信息',
    supplier: '供應商',
    customer: '客戶',
    view_company: {
      company_name: '公司名稱',
      company_city: '所在城市',
      company_address: '地址',
      company_contact: '聯繫方式',
      company_manager: '負責人'
    },
    view_supplier: {
      supplier_name: '供應商名稱',
      supplier_city: '所在城市',
      supplier_address: '地址',
      supplier_contact: '聯繫方式',
      supplier_manager: '負責人',
      supplier_level: '供應商等級'
    },
    view_customer: {
      customer_name: '客戶名稱',
      customer_city: '所在城市',
      customer_address: '地址',
      customer_contact: '聯繫方式',
      customer_manager: '負責人',
      customer_level: '客戶等級'
    }
  },
  finance: {
    capital: '固定資產',
    freight: '運輸費用',
    view_capital: {
      capital_name: '固定資產名稱',
      capital_qty: '數量',
      capital_cost: '金額'
    },
    view_freight: {
      transportation_supplier: '承運商',
      send_city: '始發地',
      receiver_city: '目的地',
      weight_fee: '重量運費',
      volume_fee: '體積運費',
      min_payment: '最小費用'
    }
  },
  driver: {
    driver: '司機管理',
    dispatchlist: '提貨記錄',
    view_driver: {
      driver_name: '司機姓名',
      license_plate: '車牌號',
      contact: '聯繫方式'
    },
    view_dispatch: {
      driver_name: '司機姓名',
      dn_code: '發貨單號',
      contact: '聯繫方式'
    }
  },
  goods: {
    goods_list: '商品列表',
    unit: '商品單位',
    class: '商品類別',
    color: '商品顏色',
    brand: '商品品牌',
    shape: '商品形狀',
    specs: '商品規格',
    origin: '商品產地',
    view_goodslist: {
      goods_code: '商品編碼',
      goods_desc: '商品描述',
      goods_supplier: '供應商',
      goods_weight: '商品重量(單位:克)',
      goods_w: '商品長度(單位:毫米)',
      goods_d: '商品寬度(單位:毫米)',
      goods_h: '商品高度(單位:毫米)',
      unit_volume: '最小單位體積',
      goods_unit: '商品單位',
      goods_class: '商品類別',
      goods_brand: '商品品牌',
      goods_color: '商品顏色',
      goods_shape: '商品形狀',
      goods_specs: '商品規格',
      goods_origin: '商品產地',
      goods_cost: '商品成本',
      goods_price: '商品價格'
    },
    view_unit: {
      goods_unit: '商品單位'
    },
    view_class: {
      goods_class: '商品類別'
    },
    view_color: {
      goods_color: '商品顏色'
    },
    view_brand: {
      goods_brand: '商品品牌'
    },
    view_shape: {
      goods_shape: '商品形狀'
    },
    view_specs: {
      goods_specs: '商品規格'
    },
    view_origin: {
      goods_origin: '商品產地'
    }
  },
  inbound: {
    asn: '到貨通知書',
    predeliverystock: '待到貨',
    preloadstock: '待卸貨',
    presortstock: '待分揀',
    sortstock: '已分揀',
    shortage: '來貨短少',
    more: '多到貨',
    asnfinish: '收貨明細',
    asndone: '收貨完成',
    view_asn: {
      asn_code: '到貨通知書單號',
      asn_status: '到貨通知書狀態',
      goods_qty: '到貨通知書數量',
      goods_actual_qty: '實際到貨數量',
      goods_shortage_qty: '到貨短少數量',
      goods_more_qty: '多到貨數量',
      goods_damage_qty: '到貨破損數量',
      presortstock: '帶分揀數量',
      sorted_qty: '已入庫數量',
      total_weight: '總重量(單位:千克)',
      total_volume: '總體積(單位:立方米)'
    }
  },
  outbound: {
    dn: '發貨單',
    freshorder: '預發貨單',
    neworder: '新發貨單',
    backorder: '欠貨訂單',
    pickstock: '待揀貨',
    pickedstock: '已揀貨',
    pickinglist: '揀貨單',
    shippedstock: '已發貨',
    received: '已簽收',
    pod: '簽收回單',
    view_dn: {
      dn_code: '發貨單號',
      dn_status: '發貨單狀態',
      goods_qty: '訂單數量',
      intransit_qty: '已發貨數量',
      delivery_actual_qty: '實際到貨數量',
      delivery_shortage_qty: '到貨短少',
      delivery_more_qty: '多到貨',
      delivery_damage_qty: '到貨破損',
      total_weight: '總重量(單位:千克)',
      total_volume: '總體積(單位:立方米)',
      customer: '客戶'
    }
  },
  staff: {
    staff: '員工列表',
    check_code: '驗證碼',
    view_staff: {
      staff_name: '員工名稱',
      staff_type: '員工類型'
    }
  },
  stock: {
    stocklist: '庫存列表',
    stockbinlist: '庫位列表',
    emptybin: '空庫位',
    occupiedbin: '有貨庫位',
    view_stocklist: {
      goods_code: '商品編碼',
      goods_desc: '商品描述',
      goods_qty: '總數量',
      onhand_stock: '現有數量',
      can_order_stock: '可被下單數量',
      ordered_stock: '已被下單數量',
      inspect_stock: '質檢數量',
      hold_stock: '鎖貨數量',
      damage_stock: '破損數量',
      asn_stock: '到貨通知書數量',
      dn_stock: '發貨單數量',
      pre_load_stock: '待卸貨數量',
      pre_sort_stock: '待分揀數量',
      sorted_stock: '已分揀數量',
      pick_stock: '待揀貨數量',
      picked_stock: '已揀貨數量',
      back_order_stock: '欠貨數量',
      on_hand_inventory: '現有庫存',
      history_inventory: '當時庫存',
      physical_inventory: '盤點數量',
      difference: '差異',
      cyclecount: '動態盤點',
      recyclecount: '复盤',
      downloadcyclecount: '盤點表',
      cyclecountresult: '確認結果',
      cyclecounttip: '生成動態盤點表',
      recyclecounttip: '生成複盤盤點表',
      downloadcyclecounttip: '下載盤點表',
      cyclecountresulttip: '確認盤點結果',
      daychoice: '日期選擇',
      daychoicetip: '選擇對應日期的盤點表'
    }
  },
  warehouse: {
    warehouse: '倉庫設置',
    binset: '庫位設置',
    binsize: '庫位尺寸',
    property: '庫位屬性',
    view_warehouse: {
      warehouse_name: '倉庫名稱',
      warehouse_city: '所在城市',
      warehouse_address: '地址',
      warehouse_contact: '聯繫方式',
      warehouse_manager: '負責人'
    },
    view_binset: {
      bin_name: '庫位名稱',
      bin_size: '庫位尺寸',
      bin_property: '庫位屬性',
      empty_label: '空庫位標識'
    },
    view_binsize: {
      bin_size: '庫位尺寸',
      bin_size_w: '庫位長度(單位:毫米)',
      bin_size_d: '庫位寬度(單位:毫米)',
      bin_size_h: '庫位高度(單位:毫米)'
    },
    view_property: {
      bin_property: '庫位屬性'
    }
  },
  scan: {
    scan: '掃描',
    scan_asn: 'ASN查詢',
    scan_dn: 'DN查詢',
    scan_sorting: '分揀',
    scan_uptobin: '上架',
    scan_picking: '揀貨',
    scan_shipping: '發貨',
    view_binmove: {
      goods_code: '產品名稱',
      onhand_stock: '現有庫存',
      qty: '移庫數量'
    }
  },
  notice: {
    unknow_error: '未知錯誤',
    network_error: '網絡異常',
    400: '錯誤請求(400)',
    401: '未取得授權(401)',
    403: '拒絕訪問(403)',
    404: '資源不存在(404)',
    405: '該功能被禁用(405)',
    408: '請求超時(408)',
    409: '數據衝突(409)',
    410: '數據已刪除(410)',
    500: '服務器錯誤(500)',
    501: '服務未實現(501)',
    502: '網絡錯誤(502)',
    503: '服務不可用(503)',
    504: '網絡超時(504)',
    505: 'HTTP版本不受支持(505)'
  }
}
