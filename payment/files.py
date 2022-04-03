from rest_framework_csv.renderers import CSVStreamingRenderer

def file_headers():
    return [
        'send_city',
        'receiver_city',
        'weight_fee',
        'volume_fee',
        'min_payment',
        'transportation_supplier',
        'creater',
        'create_time',
        'update_time'
    ]

def cn_data_header():
    return dict([
        ('send_city', u'始发城市'),
        ('receiver_city', u'到货城市'),
        ('weight_fee', u'单公斤运费'),
        ('volume_fee', u'每立方米运费'),
        ('min_payment', u'最小运费'),
        ('transportation_supplier', u'承运商'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

def en_data_header():
    return dict([
        ('send_city', u'Send City'),
        ('receiver_city', u'Receiver City'),
        ('weight_fee', u'Weight Fee'),
        ('volume_fee', u'Volume Fee'),
        ('min_payment', u'Min Payment'),
        ('transportation_supplier', u'Transportation Supplier'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time')
    ])

class FreightfileRenderCN(CSVStreamingRenderer):
    header = file_headers()
    labels = cn_data_header()

class FreightfileRenderEN(CSVStreamingRenderer):
    header = file_headers()
    labels = en_data_header()
