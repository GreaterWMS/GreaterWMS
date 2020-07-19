from django.db import models

class GoodsModel(models.Model):
    appid = models.CharField(max_length=50)
    goods_code = models.CharField(max_length=50)
    on_hand_stock = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
