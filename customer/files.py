from rest_framework_csv.renderers import CSVStreamingRenderer

def file_headers():
    return [
        'customer_name',
        'customer_city',
        'customer_address',
        'customer_contact',
        'customer_manager',
        'customer_level',
        'creater',
        'create_time',
        'update_time'
    ]

def cn_data_header():
    return dict([
        ('customer_name', u'客户名称'),
        ('customer_city', u'客户城市'),
        ('customer_address', u'详细地址'),
        ('customer_contact', u'联系电话'),
        ('customer_manager', u'负责人'),
        ('customer_level', u'客户等级'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间'),
    ])

def en_data_header():
    return dict([
        ('customer_name', u'Customer Name'),
        ('customer_city', u'Customer City'),
        ('customer_address', u'Customer Address'),
        ('customer_contact', u'Customer Contact'),
        ('customer_manager', u'Customer Manager'),
        ('customer_level', u'Customer Level'),
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
