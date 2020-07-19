from django.db import models

class Throttle(models.Model):
    openid = models.CharField(max_length=100, verbose_name='匹配名')
    appid = models.CharField(max_length=100, verbose_name='匹配用户码')
    transaction_code =  models.CharField(max_length=100, verbose_name='事务代码')
    mode = models.CharField(max_length=100, verbose_name='事务类型')
    ip_address = models.CharField(max_length=100, verbose_name='ip地址')
    throttle_create_time = models.DateTimeField(auto_now_add=True)
