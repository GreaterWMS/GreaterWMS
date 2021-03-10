from rest_framework_csv.renderers import CSVStreamingRenderer

class FileListRenderCN(CSVStreamingRenderer):
    header = [
        'asn_code',
        'asn_status',
        'total_weight',
        'total_volume',
        'supplier',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('asn_code', u'ASN单号'),
        ('asn_status', u'ASN状态'),
        ('total_weight', u'总重量'),
        ('total_volume', u'总体积'),
        ('supplier', u'供应商'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间'),
    ])

class FileListRenderEN(CSVStreamingRenderer):
    header = [
        'asn_code',
        'asn_status',
        'total_weight',
        'total_volume',
        'supplier',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('asn_code', u'ASN Code'),
        ('asn_status', u'ASN Status'),
        ('total_weight', u'Total Weight'),
        ('total_volume', u'Total Volume'),
        ('supplier', u'Supplier'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time'),
    ])

class FileDetailRenderCN(CSVStreamingRenderer):
    header = [
        'asn_code',
        'asn_status',
        'supplier',
        'goods_code',
        'goods_qty',
        'goods_actual_qty',
        'sorted_qty',
        'goods_shortage_qty',
        'goods_more_qty',
        'goods_damage_qty',
        'goods_weight',
        'goods_volume',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('asn_code', u'ASN单号'),
        ('asn_status', u'ASN状态'),
        ('supplier', u'供应商'),
        ('goods_code', u'商品编码'),
        ('goods_qty', u'订单数量'),
        ('goods_actual_qty', u'实际到货数量'),
        ('sorted_qty', u'已分拣数量'),
        ('goods_shortage_qty', u'少到货数量'),
        ('goods_more_qty', u'多到货数量'),
        ('goods_damage_qty', u'破损数量'),
        ('goods_weight', u'商品重量'),
        ('goods_volume', u'商品体积'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

class FileDetailRenderEN(CSVStreamingRenderer):
    header = [
        'asn_code',
        'asn_status',
        'supplier',
        'goods_code',
        'goods_qty',
        'goods_actual_qty',
        'sorted_qty',
        'goods_shortage_qty',
        'goods_more_qty',
        'goods_damage_qty',
        'goods_weight',
        'goods_volume',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('asn_code', u'ASN Code'),
        ('asn_status', u'ASN Status'),
        ('supplier', u'Supplier'),
        ('goods_code', u'Goods Code'),
        ('goods_qty', u'Goods Qty'),
        ('goods_actual_qty', u'Goods Actual Qty'),
        ('sorted_qty', u'Sorted Qty'),
        ('goods_shortage_qty', u'Goods Shortage Qty'),
        ('goods_more_qty', u'Goods More Qty'),
        ('goods_damage_qty', u'Goods Damage Qty'),
        ('goods_weight', u'Goods Weight'),
        ('goods_volume', u'Goods Volume'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])
