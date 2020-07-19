from django.db import models

class ListModel(models.Model):
    appid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    goods_code = models.CharField(max_length=50)
    goods_name = models.CharField(max_length=50)
    goods_qty = models.BigIntegerField(default=0)
    can_order_stock = models.BigIntegerField(default=0)
    bin_property = models.CharField(max_length=50)
    bin_size = models.CharField(max_length=50)
    po_name = models.CharField(max_length=50, verbose_name='入库单号')
    t_code = models.CharField(max_length=50)
    is_delete = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
