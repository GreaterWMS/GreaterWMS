from django.db import models

class ListModel(models.Model):
    appid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    customer_lv = models.IntegerField(default=3)
    t_code = models.CharField(max_length=50)
    is_delete = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
