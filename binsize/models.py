from django.db import models

class ListModel(models.Model):
    bin_size = models.CharField(max_length=255, verbose_name="Bin Name")
    bin_size_w = models.FloatField(default=0, verbose_name="Bin Width")
    bin_size_d = models.FloatField(default=0, verbose_name="Bin Depth")
    bin_size_h = models.FloatField(default=0, verbose_name="Bin Height")
    creater = models.CharField(max_length=255, verbose_name="Who created")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'binsize'
        verbose_name = 'Bin Size'
        verbose_name_plural = "Bin Size"
        ordering = ['-id']

    def __int__(self):
        return self.pk
