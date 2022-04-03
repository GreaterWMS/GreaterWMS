from rest_framework_csv.renderers import CSVStreamingRenderer

def file_headers():
    return [
        'staff_name',
        'staff_type',
        'create_time',
        'update_time'
    ]

def cn_data_header():
    return dict([
        ('staff_name', u'员工用户名'),
        ('staff_type', u'员工类型'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

def en_data_header():
    return dict([
        ('staff_name', u'Staff Name'),
        ('staff_type', u'Staff Type'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time'),
    ])

class FileRenderCN(CSVStreamingRenderer):
    header = file_headers()
    labels = cn_data_header()

class FileRenderEN(CSVStreamingRenderer):
    header = file_headers()
    labels = en_data_header()
