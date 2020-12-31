from django.apps import AppConfig
from django.db.models.signals import post_migrate

class GoodsunitConfig(AppConfig):
    name = 'goodsunit'

    def ready(self):
        post_migrate.connect(do_init_data, sender=self)

def do_init_data(sender, **kwargs):
    init_category()

def init_category():
    """
        :return:None
    """
    try:
        from .models import ListModel as ls
        if ls.objects.filter(openid__iexact='init_data').exists():
            pass
        else:
            init_data = [
                ls(openid='init_data', goods_unit='G', creater='GreaterWMS'),
                ls(openid='init_data', goods_unit='KG', creater='GreaterWMS'),
                ls(openid='init_data', goods_unit='Box', creater='GreaterWMS'),
                ls(openid='init_data', goods_unit='Package', creater='GreaterWMS'),
                ls(openid='init_data', goods_unit='Peice', creater='GreaterWMS'),
                ls(openid='init_data', goods_unit='Pallet', creater='GreaterWMS'),
            ]
            ls.objects.bulk_create(init_data, batch_size=100)
    except:
        pass
