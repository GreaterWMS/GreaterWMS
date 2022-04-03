from rest_framework_csv.renderers import CSVStreamingRenderer

def file_headers():
    return [
        'goods_code',
        'goods_desc',
        'goods_supplier',
        'goods_weight',
        'goods_w',
        'goods_d',
        'goods_h',
        'unit_volume',
        'goods_unit',
        'goods_class',
        'goods_brand',
        'goods_color',
        'goods_shape',
        'goods_specs',
        'goods_origin',
        'goods_cost',
        'goods_price',
        'creater',
        'create_time',
        'update_time'
    ]

def cn_data_header():
    return dict([
        ('goods_code', u'商品编码'),
        ('goods_desc', u'商品描述'),
        ('goods_supplier', u'商品供应商'),
        ('goods_weight', u'商品单位重量'),
        ('goods_w', u'商品单位长度'),
        ('goods_d', u'商品单位宽度'),
        ('goods_h', u'商品单位高度'),
        ('unit_volume', u'最小单位体积'),
        ('goods_unit', u'商品单位'),
        ('goods_class', u'商品类别'),
        ('goods_brand', u'商品品牌'),
        ('goods_color', u'商品颜色'),
        ('goods_shape', u'商品形状'),
        ('goods_specs', u'商品规格'),
        ('goods_origin', u'商品产地'),
        ('goods_cost', u'商品成本'),
        ('goods_price', u'商品价格'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

def en_data_header():
    return dict([
        ('goods_code', u'Goods Code'),
        ('goods_desc', u'Goods Description'),
        ('goods_supplier', u'Goods Supplier'),
        ('goods_weight', u'Goods Weight'),
        ('goods_w', u'Goods Wide'),
        ('goods_d', u'Goods Depth'),
        ('goods_h', u'Goods Height'),
        ('unit_volume', u'Unit Volume'),
        ('goods_unit', u'Goods Unit'),
        ('goods_class', u'Goods Class'),
        ('goods_brand', u'Goods Brand'),
        ('goods_color', u'Goods Color'),
        ('goods_shape', u'Goods Shape'),
        ('goods_specs', u'Goods Specs'),
        ('goods_origin', u'Goods Origin'),
        ('goods_cost', u'Goods Cost'),
        ('goods_price', u'Goods Price'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])

class FileRenderCN(CSVStreamingRenderer):
    header = file_headers()
    labels = cn_data_header()

class FileRenderEN(CSVStreamingRenderer):
    header = file_headers()
    labels = en_data_header()
