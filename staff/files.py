from rest_framework_csv.renderers import CSVStreamingRenderer

class FileRenderCN(CSVStreamingRenderer):
    header = [
        'staff_name',
        'staff_type',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('staff_name', u'员工用户名'),
        ('staff_type', u'员工类型'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

class FileRenderEN(CSVStreamingRenderer):
    header = [
        'staff_name',
        'staff_type',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('staff_name', u'Staff Name'),
        ('staff_type', u'Staff Type'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time'),
    ])
