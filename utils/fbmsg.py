class FBMsg(object):
    def ret():
        ret = {"code": "200", "msg": "Success Create", "data": None}
        return ret
    def err_contact_name():
        err_contact_name = {"code": "1001", "msg": "称谓不能为空", "data": None}
        return err_contact_name
    def err_contact_mobile():
        err_contact_mobile = {"code": "1002", "msg": "联系电话不能为空", "data": None}
        return err_contact_mobile
    def err_contact_comments():
        err_contact_comments = {"code": "1003", "msg": "备注不能为空", "data": None}
        return err_contact_comments
    def err_order_same():
        err_order_same = {"code": "1004", "msg": "订单已存在", "data": None}
        return err_order_same
    def err_order_no():
        err_order_no = {"code": "1005", "msg": "无效订单", "data": None}
        return err_order_no
    def err_order_fail():
        err_order_fail = {"code": "1006", "msg": "订单支付失败", "data": None}
        return err_order_fail
    def err_ret():
        err_ret = {"code": "1011", "msg": "User Name Or Password Error", "data": None}
        return err_ret
    def err_data():
        err_data = {"code": "1012", "msg": "数据不可用", "data": None}
        return err_data
    def err_tc():
        err_tc = {"code": "1013", "msg": "transaction_code错误", "data": None}
        return err_tc
    def err_tc_empty():
        err_tc_empty = {"code": "1014", "msg": "数据不存在", "data": None}
        return err_tc_empty
    def err_delete():
        err_delete = {"code": "1015", "msg": "该条数据已经删除", "data": None}
        return err_delete
    def err_code1():
        err_code1 = {"code": "1016", "msg": "数据已存在", "data": None}
        return err_code1
    def err_status():
        err_status = {"code": "1017", "msg": "状态已经存在，无需修改", "data": None}
        return err_status
    def err_user_name():
        err_user_name = {"code": "1018", "msg": "用户名不可以为空", "data": None}
        return err_user_name
    def err_auth():
        err_auth = {'code': "1021", 'msg': '用户不存在'}
        return err_auth
    def err_user_same():
        err_user_same = {'code': "1022", 'msg': 'User Is Exists'}
        return err_user_same
    def error_referer():
        error_referer = {'code': "1023", 'msg': '错误的token'}
        return error_referer
    def err_password1_empty():
        err_password1_empty = {'code': "1024", 'msg': 'Password Can Not Be Empty'}
        return err_password1_empty
    def err_password2_empty():
        err_password2_empty = {'code': "1025", 'msg': 'Please Confirm The Password'}
        return err_password2_empty
    def err_password_not_same():
        err_password_not_same = {'code': "1026", 'msg': 'Password Is Not Same One'}
        return err_password_not_same
    def err_psw():
        err_psw = {"code": "1027", "msg": "用户密码错误"}
        return err_psw
    def err_dev():
        err_dev = {"code": "1028", "msg": "非开发者openid，无法使用此功能"}
        return err_dev
    def err_register_more():
        err_register_more = {"code": "1029", "msg": "1个ip只能注册2个账号"}
        return err_register_more
    def err_openid():
        err_openid = {"code": "1030", "msg": "没有openid"}
        return err_openid
    def err_more_user():
        err_more_user = {"code": "1041", "msg": "一个账号只能建立5个用户"}
        return err_more_user
    def err_req_day():
        err_req_day = {"code": "1042", "msg": "发货记录至少需要"}
        return err_req_day
    def err_req_shipping_list():
        err_req_shipping_list = {"code": "1043", "msg": "请上传发货记录"}
        return err_req_shipping_list
    def err_req_stock_list():
        err_req_stock_list = {"code": "1044", "msg": "请上传现有库存"}
        return err_req_stock_list
    def err_req_baseinfo_list():
        err_req_baseinfo_list = {"code": "1045", "msg": "请上传基础信息"}
        return err_req_baseinfo_list
    def err_goods_code():
        err_goods_code = {"code": "1046", "msg": "该商品编号不存在"}
        return err_goods_code
    def err_authid():
        err_authid = {"code": "1033", "msg": "没有authid"}
        return err_authid
    def ret_auth():
        ret_auth = {"code": "1032", "msg": "验证通过"}
        return ret_auth
    def err_bad():
        err_bad = {"code": "1031", "msg": "提交了非法数据，多次提交直接封号"}
        return err_bad
    def err_auth_open():
        err_auth_open = {"err_auth_open": "1034", "msg": "非本授权码下账号"}
        return err_auth_open
    def err_goods_code():
        err_goods_code = {"code": "1051", "msg": "商品编码不存在", "data": None}
        return err_goods_code
    def err_po_num_empty():
        err_po_num_empty = {"code": "1060", "msg": "订单号不可以为空", "data": None}
        return err_po_num_empty
    def err_po_num():
        err_po_num = {"code": "1061", "msg": "订单已经存在", "data": None}
        return err_po_num
    def err_po_qty_type():
        err_po_qty_type = {"code": "1062", "msg": "数量必须是数字", "data": None}
        return err_po_qty_type
    def err_po_qty():
        err_po_qty = {"code": "1063", "msg": "数量必须大于0", "data": None}
        return err_po_qty
    def err_same_po_num():
        err_same_po_num = {"code": "1063", "msg": "订单编码不一致", "data": None}
        return err_same_po_num
    def err_lot_num():
        err_lot_num = {"code": "1064", "msg": "缺少lot_num，格式为:YYYY-MM-DD", "data": None}
        return err_lot_num
    def err_lot_num_empty():
        err_lot_num_empty = {"code": "1065", "msg": "lot_num不能为空，格式为:YYYY-MM-DD", "data": None}
        return err_lot_num_empty
    def err_lot_num_format():
        err_lot_num_format = {"code": "1066", "msg": "lot_num格式不正确，格式为:YYYY-MM-DD", "data": None}
        return err_lot_num_format
    def err_po_supplier():
        err_po_supplier = {"code": "1067", "msg": "字段supplier不能为空", "data": None}
        return err_po_supplier
    def err_po_supplier_empty():
        err_po_supplier_empty = {"code": "1068", "msg": "供应商不存在", "data": None}
        return err_po_supplier_empty
    def err_po_goods_code():
        err_po_goods_code = {"code": "1069", "msg": "商品编码不能为空", "data": None}
        return err_po_goods_code
    def err_po_status_empty():
        err_po_status_empty = {"code": "1070", "msg": "订单状态不能为空", "data": None}
        return err_po_status_empty
    def err_po_status_less():
        err_po_status_less = {"code": "1071", "msg": "订单状态不可逆", "data": None}
        return err_po_status_less
    def err_po_status_same():
        err_po_status_same = {"code": "1072", "msg": "订单状态不可以相同", "data": None}
        return err_po_status_same
    def err_po_status_more():
        err_po_status_more = {"code": "1073", "msg": "订单状态不可以直接跨级更改", "data": None}
        return err_po_status_more
    def err_po_status_big():
        err_po_status_big = {"code": "1074", "msg": "此接口只支持9以内的状态变化", "data": None}
        return err_po_status_big
    def err_po_status_delete():
        err_po_status_delete = {"code": "1075", "msg": "只有订单状态为1的订单可以删除", "data": None}
        return err_po_status_delete
    def err_po_status_patch():
        err_po_status_patch = {"code": "1076", "msg": "只有订单状态为1的订单可以修改", "data": None}
        return err_po_status_patch
    def err_po_actual_delivery_stock_patch():
        err_po_actual_delivery_stock_patch = {"code": "1077", "msg": "实际到货数量不可以为空", "data": None}
        return err_po_actual_delivery_stock_patch
    def err_po_actual_delivery_stock_more():
        err_po_actual_delivery_stock_more = {"code": "1078", "msg": "实际到货数量不可以大于订单数量", "data": None}
        return err_po_actual_delivery_stock_more
    def err_po_actual_delivery_stock_zero():
        err_po_actual_delivery_stock_zero = {"code": "1079", "msg": "实际到货数量不可以小于0", "data": None}
        return err_po_actual_delivery_stock_zero
    def err_po_actual_delivery_stock_moreall():
        err_po_actual_delivery_stock_moreall = {"code": "1080", "msg": "到货数量不可以大于订单数量", "data": None}
        return err_po_actual_delivery_stock_moreall
    def err_po_actual_delivery_stock_again():
        err_po_actual_delivery_stock_again = {"code": "1081", "msg": "不要重复修改相同的数量", "data": None}
        return err_po_actual_delivery_stock_again
    def err_sort_stock_bin_name():
        err_sort_stock_bin_name = {"code": "1082", "msg": "上架库位名称不能为空", "data": None}
        return err_sort_stock_bin_name
    def err_sort_stock_bin_name_error():
        err_sort_stock_bin_name_error = {"code": "1083", "msg": "上架库位不存在", "data": None}
        return err_sort_stock_bin_name_error
    def err_sort_stock_qty():
        err_sort_stock_qty = {"code": "1084", "msg": "需要有上架数量", "data": None}
        return err_sort_stock_qty
    def err_sort_stock_qty_empty():
        err_sort_stock_qty_empty = {"code": "1085", "msg": "上架数量不能为空", "data": None}
        return err_sort_stock_qty_empty
    def err_sort_stock_qty_zero():
        err_sort_stock_qty_zero = {"code": "1086", "msg": "上架数量必须大于0", "data": None}
        return err_sort_stock_qty_zero
    def err_sort_stock_qty_more():
        err_sort_stock_qty_more = {"code": "1087", "msg": "上架数量不可以超过待上架库存", "data": None}
        return err_sort_stock_qty_more
    def err_sort_stock_bin_type():
        err_sort_stock_bin_type = {"code": "1088", "msg": "上架库位属性与实际库位属性不符", "data": None}
        return err_sort_stock_bin_type
    def wms_ret():
        wms_ret = {"code": "200", "msg": "操作成功", "data": None}
        return wms_ret
    def wms_same():
        wms_same = {"code": "100001", "msg": "数据已存在", "data": None}
        return wms_same
    def wms_err():
        wms_err = {"code": "100002", "msg": "数据不存在", "data": None}
        return wms_err
    def wms_errfile():
        wms_errfile = {"code": "100003", "msg": "下载文件请求参数错误", "data": None}
        return wms_errfile
    def wms_time():
        wms_time = {"results":{"code": "100004", "msg": "起始时间必须大于等于结束日期,默认结束日期为今天", "data": None}}
        return wms_time
    def wms_vip_get():
        wms_vip_get = {"results":{"code": "100005", "msg": "您的会员等级不够，请升级会员来提权", "data": None}}
        return wms_vip_get
    def wms_vip():
        wms_vip = {"code": "100005", "msg": "普通会员每天只能进行3次主动沟通", "data": None}
        return wms_vip
    def wms_dev():
        wms_dev = {"code": "100006", "msg": "不可以对管理员账号进行操作", "data": None}
        return wms_dev
    def wms_user_owner():
        wms_user_owner = {"code": "100007", "msg": "不可以删除自己", "data": None}
        return wms_user_owner
    def wms_warehouse_more():
        wms_warehouse_more = {"code": "100008", "msg": "只能创建一个仓库", "data": None}
        return wms_warehouse_more
    def wms_company_more():
        wms_company_more = {"code": "100008", "msg": "只能创建一个公司信息", "data": None}
        return wms_company_more
    def wms_binproperty():
        wms_binproperty = {"code": "100009", "msg": "库位属性不存在", "data": None}
        return wms_binproperty
    def wms_binsize():
        wms_binsize = {"code": "100010", "msg": "库位尺寸不存在", "data": None}
        return wms_binsize
    def wms_no_user():
        wms_no_user = {"results": {"code": "100011", "msg": "用户名不存在", "data": None}}
        return wms_no_user
    def wms_po_status_1():
        wms_po_status_1 = {"code": "100012", "msg": "只有入库单状态为1的订单才可以删除", "data": None}
        return wms_po_status_1
    def wms_po_empty():
        wms_po_empty = {"code": "100013", "msg": "入库单号码不存在", "data": None}
        return wms_po_empty
    def wms_po_status_predelivery():
        wms_po_status_predelivery = {"code": "100014", "msg": "入库单已经到货", "data": None}
        return wms_po_status_predelivery
    def wms_po_status_predelivery_detail():
        wms_po_status_predelivery_detail = {"code": "100015", "msg": "入库单没有任何订单明细", "data": None}
        return wms_po_status_predelivery_detail
    def wms_po_status_preload_detail():
        wms_po_status_preload_detail = {"code": "100016", "msg": "入库单没有任何订单明细", "data": None}
        return wms_po_status_preload_detail
    def wms_po_qty_up_more():
        wms_po_qty_up_more = {"code": "100017", "msg": "实际到货上架数量不可大于实际到货数量", "data": None}
        return wms_po_qty_up_more
    def wms_po_qty_dup_more():
        wms_po_qty_dup_more = {"code": "100018", "msg": "破损上架数量不可大于到货破损数量", "data": None}
        return wms_po_qty_dup_more
    def wms_po_qty_all_up_more():
        wms_po_qty_all_up_more = {"code": "100019", "msg": "上架数量不可大于待上架数量", "data": None}
        return wms_po_qty_all_up_more
    def wms_so_picked_more():
        wms_so_picked_more = {"code": "100020", "msg": "实际拣货数量不可以大于需要拣货数量", "data": None}
        return wms_so_picked_more
    def wms_dongtai():
        wms_dongtai = {"code": "200", "msg": "动态发布成功", "data": None}
        return wms_dongtai
    def wms_capcha():
        wms_capcha = {"code": "100080", "msg": "刷新过快，请稍后再刷新验证码", "data": None}
        return wms_capcha
    def wms_capcha_l():
        wms_capcha_l = {"code": "100081", "msg": "验证码超时", "data": None}
        return wms_capcha_l
    def wms_capcha_n():
        wms_capcha_n = {"code": "100082", "msg": "验证码不存在", "data": None}
        return wms_capcha_n
