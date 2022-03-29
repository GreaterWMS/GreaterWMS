from rest_framework_csv.renderers import CSVStreamingRenderer

def file_headers():
    return [
        'shop_name',
        'shop_mode',
        'shop_appid',
        'shop_app_secret',
        'shop_id',
        'sandbox',
        'proxy',
        'proxy_ip',
        'create_time',
        'update_time'
    ]

def cn_data_header():
    return dict([
        ('shop_name', u'店铺名称'),
        ('shop_mode', u'所属平台'),
        ('shop_appid', u'Appid'),
        ('shop_app_secret', u'App Secret'),
        ('shop_id', u'店铺ID'),
        ('sandbox', u'沙箱环境'),
        ('proxy', u'代理IP'),
        ('proxy_ip', u'代理IP地址'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间')
    ])

class DouYinfileRenderCN(CSVStreamingRenderer):
    header = file_headers()
    labels = cn_data_header()
