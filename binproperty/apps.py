from django.apps import AppConfig
from django.db.models.signals import post_migrate

class BinpropertyConfig(AppConfig):
    name = 'binproperty'

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
            if ls.objects.filter(openid__iexact='init_data').count() != 4:
                ls.objects.filter(openid__iexact='init_data').delete()
                init_data = [
                    ls(id=1, openid='init_data', bin_property='Damage', creater='GreaterWMS'),
                    ls(id=2, openid='init_data', bin_property='Inspection', creater='GreaterWMS'),
                    ls(id=3, openid='init_data', bin_property='Normal', creater='GreaterWMS'),
                    ls(id=4, openid='init_data', bin_property='Holding', creater='GreaterWMS')
                ]
                ls.objects.bulk_create(init_data, batch_size=100)
        else:
            init_data = [
                ls(id=1, openid='init_data', bin_property='Damage', creater='GreaterWMS'),
                ls(id=2, openid='init_data', bin_property='Inspection', creater='GreaterWMS'),
                ls(id=3, openid='init_data', bin_property='Normal', creater='GreaterWMS'),
                ls(id=4, openid='init_data', bin_property='Holding', creater='GreaterWMS')
            ]
            ls.objects.bulk_create(init_data, batch_size=100)
    except:
        pass
