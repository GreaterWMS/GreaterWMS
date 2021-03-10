from rest_framework_csv.renderers import CSVStreamingRenderer

class FileRenderCN(CSVStreamingRenderer):
    header = [
        'bin_name',
        'bin_size',
        'bin_property',
        'empty_label',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('bin_name', u'库位名称'),
        ('bin_size', u'库位尺寸'),
        ('bin_property', u'库位属性'),
        ('empty_label', u'空库位标识'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

class FileRenderEN(CSVStreamingRenderer):
    header = [
        'bin_name',
        'bin_size',
        'bin_property',
        'empty_label',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('bin_name', u'Bin Name'),
        ('bin_size', u'Bin Size'),
        ('bin_property', u'Bin Property'),
        ('empty_label', u'Empty Label'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])
