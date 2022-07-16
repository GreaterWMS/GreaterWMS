from django.db import models

class ListModel(models.Model):
    goods_class = models.CharField(max_length=255, verbose_name="Goods Class")
    creater = models.CharField(max_length=255, verbose_name="Who created")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'goodsclass'
        verbose_name = 'Goods Class'
        verbose_name_plural = "Goods Class"
        ordering = ['goods_class']

    def __int__(self):
        return self.pk
