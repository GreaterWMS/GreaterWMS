from django.db import models

class ListModel(models.Model):
    bin_name = models.CharField(max_length=255, verbose_name="Bin Name")
    bin_size = models.CharField(max_length=255, verbose_name="Bin Size")
    bin_property = models.CharField(max_length=11, verbose_name="Bin Property")
    empty_label = models.BooleanField(default=True, verbose_name="Empty Label")
    creater = models.CharField(max_length=255, verbose_name="Who Created")
    bar_code = models.CharField(max_length=255, verbose_name="Bar Code")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'binset'
        verbose_name = 'Bin Set'
        verbose_name_plural = "Bin Set"
        ordering = ['bin_name']

    def __int__(self):
        return self.pk
