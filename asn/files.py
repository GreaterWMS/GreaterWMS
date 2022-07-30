from rest_framework_csv.renderers import CSVStreamingRenderer

def list_file_headers():
    return [
        'asn_code',
        'asn_status',
        'total_weight',
        'total_volume',
        'total_cost',
        'supplier',
        'creater',
        'create_time',
        'update_time'
    ]

def list_cn_data_header():
    return dict([
        ('asn_code', u'ASN单号'),
        ('asn_status', u'ASN状态'),
        ('total_weight', u'总重量'),
        ('total_volume', u'总体积'),
        ('total_cost', u'总成本'),
        ('supplier', u'供应商'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

def list_en_data_header():
    return dict([
        ('asn_code', u'ASN Code'),
        ('asn_status', u'ASN Status'),
        ('total_weight', u'Total Weight'),
        ('total_volume', u'Total Volume'),
        ('total_cost', u'Total Cost'),
        ('supplier', u'Supplier'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])

def detail_file_headers():
    return [
        'asn_code',
        'asn_status',
        'supplier',
        'goods_code',
        'goods_desc',
        'goods_qty',
        'goods_actual_qty',
        'sorted_qty',
        'goods_shortage_qty',
        'goods_more_qty',
        'goods_damage_qty',
        'goods_weight',
        'goods_volume',
        'goods_cost',
        'creater',
        'create_time',
        'update_time'
    ]

def detail_cn_data_header():
    return dict([
        ('asn_code', u'ASN单号'),
        ('asn_status', u'ASN状态'),
        ('supplier', u'供应商'),
        ('goods_code', u'商品编码'),
        ('goods_desc', u'商品描述'),
        ('goods_qty', u'订单数量'),
        ('goods_actual_qty', u'实际到货数量'),
        ('sorted_qty', u'已分拣数量'),
        ('goods_shortage_qty', u'少到货数量'),
        ('goods_more_qty', u'多到货数量'),
        ('goods_damage_qty', u'破损数量'),
        ('goods_weight', u'商品重量'),
        ('goods_volume', u'商品体积'),
        ('goods_cost', u'商品成本'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

def detail_en_data_header():
    return dict([
        ('asn_code', u'ASN Code'),
        ('asn_status', u'ASN Status'),
        ('supplier', u'Supplier'),
        ('goods_code', u'Goods Code'),
        ('goods_desc', u'Goods Description'),
        ('goods_qty', u'Goods Qty'),
        ('goods_actual_qty', u'Goods Actual Qty'),
        ('sorted_qty', u'Sorted Qty'),
        ('goods_shortage_qty', u'Goods Shortage Qty'),
        ('goods_more_qty', u'Goods More Qty'),
        ('goods_damage_qty', u'Goods Damage Qty'),
        ('goods_weight', u'Goods Weight'),
        ('goods_volume', u'Goods Volume'),
        ('goods_cost', u'Goods Cost'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])

class FileListRenderCN(CSVStreamingRenderer):
    header = list_file_headers()
    labels = list_cn_data_header()

class FileListRenderEN(CSVStreamingRenderer):
    header = list_file_headers()
    labels = list_en_data_header()

class FileDetailRenderCN(CSVStreamingRenderer):
    header = detail_file_headers()
    labels = detail_cn_data_header()

class FileDetailRenderEN(CSVStreamingRenderer):
    header = detail_file_headers()
    labels = detail_en_data_header()
