from rest_framework_csv.renderers import CSVStreamingRenderer


def file_headers():
    return [
        'customer_id',
        'customer_name',
        'customer_group',
        'customer_contact',
        'customer_bank_account',
        'customer_password',
        'customer_refrigeration_fee',
        'customer_loading_fee',
        'customer_film_laminating_fee',
        'create_time'
    ]

def cn_data_header():
    return dict([
        ('customer_id', u'客户id'),
        ('customer_name', u'客户名称'),
        ('customer_group', u'客户组'),
        ('customer_contact', u'联系电话'),
        ('customer_bank_account', u'银行账号'),
        ('customer_password', u'密码'),
        ('customer_refrigeration_fee', u'冷藏费'),
        ('customer_loading_fee', u'装卸费'),
        ('customer_film_laminating_fee', u'围膜费'),
        ('create_time', u'创建时间')
    ])

def en_data_header():
    return dict([
        ('customer_id', u'ID'),
        ('customer_name', u'Name'),
        ('customer_group', u'Group'),
        ('customer_contact', u'Contact'),
        ('customer_bank_account', u'Bank Account'),
        ('customer_password', u'Password'),
        ('customer_refrigeration_fee', u'Refrigeration Fee'),
        ('customer_loading_fee', u'Loading Fee'),
        ('customer_film_laminating_fee', u'Film-Laminating Fee'),
        ('create_time', u'Create Time')
    ])


class FileRenderCN(CSVStreamingRenderer):
    header = file_headers()
    labels = cn_data_header()

class FileRenderEN(CSVStreamingRenderer):
    header = file_headers()
    labels = en_data_header()
