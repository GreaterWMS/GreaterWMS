from django.db import models

class ShippingModel(models.Model):
    appid = models.CharField(max_length=50)
    goods_code = models.CharField(max_length=50)
    shipping_time = models.DateField(auto_now_add=False)
    shipping_qty = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
