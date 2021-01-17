from rest_framework_csv.renderers import CSVStreamingRenderer

class FileRenderCN(CSVStreamingRenderer):
    header = [
        'capital_name',
        'capital_qty',
        'capital_cost',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('capital_name', u'资产名称'),
        ('capital_qty', u'资产数量'),
        ('capital_cost', u'资产成本'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

class FileRenderEN(CSVStreamingRenderer):
    header = [
        'capital_name',
        'capital_qty',
        'capital_cost',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('capital_name', u'Capital Name'),
        ('capital_qty', u'Capital Qty'),
        ('capital_cost', u'Capital Cost'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])
