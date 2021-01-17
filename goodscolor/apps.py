from django.apps import AppConfig
from django.db.models.signals import post_migrate

class GoodscolorConfig(AppConfig):
    name = 'goodscolor'

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
                ls(openid='init_data', goods_color='Red', creater='GreaterWMS'),
                ls(openid='init_data', goods_color='Orange', creater='GreaterWMS'),
                ls(openid='init_data', goods_color='Yellow', creater='GreaterWMS'),
                ls(openid='init_data', goods_color='Green', creater='GreaterWMS'),
                ls(openid='init_data', goods_color='Blue', creater='GreaterWMS'),
                ls(openid='init_data', goods_color='Indigo', creater='GreaterWMS'),
                ls(openid='init_data', goods_color='Purple', creater='GreaterWMS'),
            ]
            ls.objects.bulk_create(init_data, batch_size=100)
    except:
        pass
