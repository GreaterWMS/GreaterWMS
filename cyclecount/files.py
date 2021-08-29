from rest_framework_csv.renderers import CSVStreamingRenderer

def file_headers():
    return [
        'creater',
        'create_time'
    ]

def cn_data_header():
    return dict([
        ('creater', u'创建人'),
        ('create_time', u'创建时间')
    ])

def en_data_header():
    return dict([
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
    ])


class FileRenderCN(CSVStreamingRenderer):
    header = file_headers()
    labels = cn_data_header()

class FileRenderEN(CSVStreamingRenderer):
    header = file_headers()
    labels = en_data_header()
