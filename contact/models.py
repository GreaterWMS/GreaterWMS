from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    comments = models.CharField(max_length=400, verbose_name='备注')
    openid = models.CharField(max_length=400, verbose_name='用户标识')
    ip = models.CharField(max_length=80, verbose_name='ip')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<contact: %s for %s for %s>' % (self.name, self.mobile, self.comments)
