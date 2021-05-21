from rest_framework_csv.renderers import CSVStreamingRenderer

def file_headers():
    return [
        'capital_name',
        'capital_qty',
        'capital_cost',
        'creater',
        'create_time',
        'update_time'
    ]
def cn_data_header():
    return dict([
        ('capital_name', u'资产名称'),
        ('capital_qty', u'资产数量'),
        ('capital_cost', u'资产成本'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

def en_data_header():
    return dict([
        ('capital_name', u'Capital Name'),
        ('capital_qty', u'Capital Qty'),
        ('capital_cost', u'Capital Cost'),
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
