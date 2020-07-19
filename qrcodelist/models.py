from django.db import models

class QrCodeList(models.Model):
    text = models.CharField(max_length=100, verbose_name='二维码信息')
    text_img = models.CharField(max_length=100, verbose_name='二维码链接')
    create_time = models.DateTimeField(auto_now_add=True)
