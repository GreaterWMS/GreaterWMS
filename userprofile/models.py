from django.db import models

class Users(models.Model):
    user_id = models.IntegerField(default=0, verbose_name="用户id")
    name = models.CharField(max_length=80, verbose_name='登入名')
    vip = models.IntegerField(default=1, verbose_name='vip等级')
    openid = models.CharField(max_length=100, verbose_name='openid')
    appid = models.CharField(max_length=100, verbose_name='appid')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    developer = models.BooleanField(default=True, verbose_name='开发者标识')
    t_code = models.CharField(max_length=100, verbose_name='后台ID')
    ip = models.CharField(max_length=100, verbose_name='注册ip')
    vip_time = models.DateTimeField(auto_now_add=True)
    link_to = models.BooleanField(default=False, verbose_name='是否发起链接')
    link_to_id = models.IntegerField(default=0, verbose_name='链接发起者')
    avatar = models.CharField(max_length=100, default='/static/img/user.jpg', verbose_name='头像')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
