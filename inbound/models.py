from django.db import models

class ListModel(models.Model):
    api_name = models.CharField(max_length=32, verbose_name="接口名称")
    api_describe = models.TextField(max_length=255, verbose_name="接口描述")
    api_manager = models.CharField(max_length=11, verbose_name="接口负责人")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'inbound'
        verbose_name = 'data id'
        verbose_name_plural = "data id"
        ordering = ['-id']

    def __str__(self):
        return self.pk
