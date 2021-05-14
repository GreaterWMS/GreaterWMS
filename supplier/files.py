from rest_framework_csv.renderers import CSVStreamingRenderer

def file_headers():
    return [
        'supplier_name',
        'supplier_city',
        'supplier_address',
        'supplier_contact',
        'supplier_manager',
        'supplier_level',
        'creater',
        'create_time',
        'update_time'
    ]

def cn_data_header():
    return dict([
        ('supplier_name', u'供应商名称'),
        ('supplier_city', u'供应商城市'),
        ('supplier_address', u'详细地址'),
        ('supplier_contact', u'联系电话'),
        ('supplier_manager', u'负责人'),
        ('supplier_level', u'供应商等级'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间'),
    ])

def en_data_header():
    return dict([
        ('supplier_name', u'Supplier Name'),
        ('supplier_city', u'Supplier City'),
        ('supplier_address', u'Supplier Address'),
        ('supplier_contact', u'Supplier Contact'),
        ('supplier_manager', u'Supplier Manager'),
        ('supplier_level', u'Supplier Level'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time'),
    ])

class FileRenderCN(CSVStreamingRenderer):
    header = file_headers()
    labels = cn_data_header()

class FileRenderEN(CSVStreamingRenderer):
    header = file_headers()
    labels = en_data_header()
