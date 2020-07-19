from django.db import models

class BaseInfoModel(models.Model):
    appid = models.CharField(max_length=50)
    goods_code = models.CharField(max_length=50)
    sup_product_day = models.IntegerField(default=0)
    sup_intransit = models.IntegerField(default=0)
    loading_inspect = models.IntegerField(default=0)
    total_leadtime = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
