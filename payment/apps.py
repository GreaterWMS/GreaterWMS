from django.apps import AppConfig
from django.db.models.signals import post_migrate

class PaymentConfig(AppConfig):
    name = 'payment'

#     def ready(self):
#         post_migrate.connect(do_init_data, sender=self)
#
# def do_init_data(sender, **kwargs):
#     init_category()
#
# def init_category():
#     """
#         :return:None
#     """
#     try:
#         from .models import TransportationFeeListModel as transporationfee
#         if transporationfee.objects.filter(openid__iexact='init_data').exists():
#             pass
#         else:
#             init_data = [
#                 transporationfee(openid='init_data', send_city='上海市', receiver_city='杭州市',
#                                  weight_fee=0.4, volume_fee=30, transportation_supplier='WanKe Logistic',
#                                  min_payment=250, creater='GreaterWMS'),
#                 transporationfee(openid='init_data', send_city='上海市', receiver_city='北京市',
#                                  weight_fee=0.8, volume_fee=220, transportation_supplier='WanKe Logistic',
#                                  min_payment=250, creater='GreaterWMS'),
#             ]
#             transporationfee.objects.bulk_create(init_data, batch_size=100)
#     except:
#         pass
#
# def init_datas():
#     init_category()
