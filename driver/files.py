from rest_framework_csv.renderers import CSVStreamingRenderer

class FileRenderCN(CSVStreamingRenderer):
    header = [
        'driver_name',
        'license_plate',
        'contact',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('driver_name', u'司机姓名'),
        ('license_plate', u'车牌号'),
        ('contact', u'联系方式'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

class FileRenderEN(CSVStreamingRenderer):
    header = [
        'driver_name',
        'license_plate',
        'contact',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('driver_name', u'Driver Name'),
        ('license_plate', u'License Plate'),
        ('contact', u'Contact'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])
