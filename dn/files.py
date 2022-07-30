from rest_framework_csv.renderers import CSVStreamingRenderer

def list_file_headers():
    return [
        'dn_code',
        'dn_status',
        'total_weight',
        'total_volume',
        'customer',
        'creater',
        'back_order_label',
        'create_time',
        'update_time'
    ]
def list_cn_data_header():
    return dict([
        ('dn_code', u'发货单单号'),
        ('dn_status', u'发货单状态'),
        ('total_weight', u'总重量'),
        ('total_volume', u'总体积'),
        ('customer', u'客户'),
        ('creater', u'创建人'),
        ('back_order_label', u'欠货订单标识'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

def list_en_data_header():
    return dict([
        ('dn_code', u'DN Code'),
        ('dn_status', u'DN Status'),
        ('total_weight', u'Total Weight'),
        ('total_volume', u'Total Volume'),
        ('customer', u'Customer'),
        ('creater', u'Creater'),
        ('back_order_label', u'Back Order Label'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])

def detail_file_headers():
    return [
        'dn_code',
        'dn_status',
        'goods_code',
        'goods_desc',
        'goods_qty',
        'pick_qty',
        'picked_qty',
        'intransit_qty',
        'delivery_actual_qty',
        'delivery_shortage_qty',
        'delivery_more_qty',
        'delivery_damage_qty',
        'goods_weight',
        'goods_volume',
        'customer',
        'creater',
        'back_order_label',
        'create_time',
        'update_time'
    ]
def detail_cn_data_header():
    return dict([
        ('dn_code', u'发货单单号'),
        ('dn_status', u'发货单状态'),
        ('goods_code', u'发货单货物名称'),
        ('goods_desc', u'发货单货物描述'),
        ('goods_qty', u'发货单数量'),
        ('pick_qty', u'需要拣货数量'),
        ('picked_qty', u'已拣货数量'),
        ('intransit_qty', u'在途库存'),
        ('delivery_actual_qty', u'实际到货'),
        ('delivery_shortage_qty', u'到货短少'),
        ('delivery_more_qty', u'多到货'),
        ('delivery_damage_qty', u'到货破损'),
        ('goods_weight', u'商品重量'),
        ('goods_volume', u'商品体积'),
        ('customer', u'客户'),
        ('creater', u'创建人'),
        ('back_order_label', u'欠货订单标识'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

def detail_en_data_header():
    return dict([
        ('dn_code', u'DN Code'),
        ('dn_status', u'DN Status'),
        ('goods_code', u'Goods Code'),
        ('goods_desc', u'Goods Description'),
        ('goods_qty', u'Goods Qty'),
        ('pick_qty', u'Pick Qty'),
        ('picked_qty', u'Picked Qty'),
        ('intransit_qty', u'Intransit Qty'),
        ('delivery_actual_qty', u'Delivery Actual Qty'),
        ('delivery_shortage_qty', u'Delivery Shortage Qty'),
        ('delivery_more_qty', u'Delivery More Qty'),
        ('delivery_damage_qty', u'Delivery Damage Qty'),
        ('goods_weight', u'Goods Weight'),
        ('goods_volume', u'Goods Volume'),
        ('customer', u'Customer'),
        ('creater', u'Creater'),
        ('back_order_label', u'Back Order Label'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])

class FileListRenderCN(CSVStreamingRenderer):
    header = list_file_headers()
    labels = list_cn_data_header()

class FileListRenderEN(CSVStreamingRenderer):
    header = list_file_headers()
    labels = list_cn_data_header()

class FileDetailRenderCN(CSVStreamingRenderer):
    header = detail_file_headers()
    labels = detail_cn_data_header()

class FileDetailRenderEN(CSVStreamingRenderer):
    header = detail_file_headers()
    labels = detail_en_data_header()
