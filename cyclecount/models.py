from django.db import models

class ListModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='库位名称')
    goods_code = models.CharField(max_length=50, verbose_name='商品编号')
    goods_name = models.CharField(max_length=50, verbose_name='商品描述')
    goods_qty = models.BigIntegerField(default=0, verbose_name='盘点数量')
    staff = models.CharField(max_length=50, verbose_name='盘点用户名')
    cycle_count_balance = models.BigIntegerField(default=0, verbose_name='盘点差异')
    inbound_time = models.DateTimeField(auto_now_add=False)
    appid = models.CharField(max_length=50, verbose_name='用户匹配码')
    t_code = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
