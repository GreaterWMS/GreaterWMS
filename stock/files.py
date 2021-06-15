from rest_framework_csv.renderers import CSVStreamingRenderer

def file_headers_bin():
    return [
        'bin_name',
        'goods_code',
        'goods_desc',
        'goods_qty',
        'pick_qty',
        'picked_qty',
        'bin_size',
        'bin_property',
        'create_time',
        'update_time'
    ]

def cn_data_header_bin():
    return dict([
        ('bin_name', u'库位名称'),
        ('goods_code', u'商品编码'),
        ('goods_desc', u'商品描述'),
        ('goods_qty', u'商品数量'),
        ('pick_qty', u'等待拣货数量'),
        ('picked_qty', u'已拣货数量'),
        ('bin_size', u'库位尺寸'),
        ('bin_property', u'库位属性'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

def en_data_header_bin():
    return dict([
        ('bin_name', u'Bin Name'),
        ('goods_code', u'Goods Code'),
        ('goods_desc', u'Goods Description'),
        ('goods_qty', u'Goods Qty'),
        ('pick_qty', u'Pick Stock'),
        ('picked_qty', u'Picked Stock'),
        ('bin_size', u'Bin Size'),
        ('bin_property', u'Bin Property'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])

def file_headers_list():
    return [
        'goods_code',
        'goods_desc',
        'goods_qty',
        'onhand_stock',
        'can_order_stock',
        'ordered_stock',
        'inspect_stock',
        'hold_stock',
        'damage_stock',
        'asn_stock',
        'dn_stock',
        'pre_load_stock',
        'pre_sort_stock',
        'sorted_stock',
        'pick_stock',
        'picked_stock',
        'back_order_stock',
        'create_time',
        'update_time'
    ]

def cn_data_header_list():
    return dict([
        ('goods_code', u'商品编码'),
        ('goods_desc', u'商品描述'),
        ('goods_qty', u'商品数量'),
        ('onhand_stock', u'现有库存'),
        ('can_order_stock', u'可被下单数量'),
        ('ordered_stock', u'已被下单数量'),
        ('inspect_stock', u'质检库存'),
        ('hold_stock', u'锁定库存'),
        ('damage_stock', u'破损库存'),
        ('asn_stock', u'到货通知书数量'),
        ('dn_stock', u'发货单数量'),
        ('pre_load_stock', u'等待卸货数量'),
        ('pre_sort_stock', u'等待分拣数量'),
        ('sorted_stock', u'已分拣数量'),
        ('pick_stock', u'等待拣货数量'),
        ('picked_stock', u'已拣货数量'),
        ('back_order_stock', u'欠货数量'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

def en_data_header_list():
    return dict([
        ('goods_code', u'Goods Code'),
        ('goods_desc', u'Goods Description'),
        ('goods_qty', u'Goods Qty'),
        ('onhand_stock', u'Onhand Stock'),
        ('can_order_stock', u'Can Order Stock'),
        ('ordered_stock', u'Ordered Stock'),
        ('inspect_stock', u'Inspect Stock'),
        ('hold_stock', u'Hold Stock'),
        ('damage_stock', u'Damage Stock'),
        ('asn_stock', u'ASN Stock'),
        ('dn_stock', u'DN Stock'),
        ('pre_load_stock', u'Pre Load Stock'),
        ('pre_sort_stock', u'Pre Sort Stock'),
        ('sorted_stock', u'Sorted Stock'),
        ('pick_stock', u'Pick Stock'),
        ('picked_stock', u'Picked Stock'),
        ('back_order_stock', u'Back Order Stock'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])

class FileBinListRenderCN(CSVStreamingRenderer):
    header = file_headers_bin()
    labels = cn_data_header_bin()

class FileBinListRenderEN(CSVStreamingRenderer):
    header = file_headers_bin()
    labels = en_data_header_bin()

class FileListRenderCN(CSVStreamingRenderer):
    header = file_headers_list()
    labels = cn_data_header_list()

class FileListRenderEN(CSVStreamingRenderer):
    header = file_headers_list()
    labels = en_data_header_list()
