from django.db import models

class Users(models.Model):
    user_id = models.IntegerField(default=0, verbose_name="Admin ID")
    name = models.CharField(max_length=80, verbose_name='Staff Name')
    vip = models.BigIntegerField(default=1, verbose_name='VIP Level')
    openid = models.CharField(max_length=100, verbose_name='OPENID')
    appid = models.CharField(max_length=100, verbose_name='APPID')
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    developer = models.BooleanField(default=True, verbose_name='Developer Label')
    t_code = models.CharField(max_length=100, verbose_name='Transaction Code')
    ip = models.CharField(max_length=100, verbose_name='Register IP')
    vip_time = models.DateTimeField(auto_now_add=True)
    link_to = models.BooleanField(default=False, verbose_name='Link To')
    link_to_id = models.BigIntegerField(default=0, verbose_name='Link To ID')
    avatar = models.CharField(max_length=100, default='/static/img/user.jpg', verbose_name='Staff Avatar')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Update Time')

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'User Profile'
        verbose_name_plural = "User Profile"
        ordering = ['-id']

    def __int__(self):
        return self.pk