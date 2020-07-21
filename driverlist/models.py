from django.db import models

class ListModel(models.Model):
    appid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    plate_license = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    identity_card = models.CharField(max_length=50)
    driver_license = models.CharField(max_length=50)
    vehicle_license = models.CharField(max_length=50)
    create_name = models.CharField(max_length=50)
    t_code = models.CharField(max_length=50)
    is_delete = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
