from rest_framework_csv.renderers import CSVStreamingRenderer

def file_headers():
    return [
        "cyclecount_status",
        "bin_name",
        "goods_code",
        "goods_desc",
        "goods_qty",
        "physical_inventory",
        "difference",
        "creater",
        "create_time",
        "update_time"
    ]

def cn_data_header():
    return dict([
        ('cyclecount_status', u'盘点状态'),
        ('bin_name', u'库位名称'),
        ('goods_code', u'商品编码'),
        ('goods_desc', u'商品描述'),
        ('goods_qty', u'现有数量'),
        ('physical_inventory', u'盘点数量'),
        ('difference', u'盘点差异'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'盘点时间')
    ])

def en_data_header():
    return dict([
        ('cyclecount_status', u'Count Status'),
        ('bin_nam', u'Bin Name'),
        ('goods_code', u'Goods Code'),
        ('goods_desc', u'Goods Description'),
        ('goods_qty', u'On-Hand Stock'),
        ('physical_inventory', u'Count QTY'),
        ('difference', u'Count Difference'),
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
