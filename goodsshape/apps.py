from django.apps import AppConfig
from django.db.models.signals import post_migrate

class GoodsshapeConfig(AppConfig):
    name = 'goodsshape'

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
                ls(openid='init_data', goods_shape='Square', creater='GreaterWMS'),
                ls(openid='init_data', goods_shape='Rectangle', creater='GreaterWMS'),
                ls(openid='init_data', goods_shape='Cone', creater='GreaterWMS'),
                ls(openid='init_data', goods_shape='Cylinder', creater='GreaterWMS'),
                ls(openid='init_data', goods_shape='Irregular', creater='GreaterWMS'),
            ]
            ls.objects.bulk_create(init_data, batch_size=100)
    except:
        pass
