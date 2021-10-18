from django.db import models

class CyclecountModeDayModel(models.Model):
    openid = models.CharField(max_length=255, verbose_name="Openid")
    cyclecount_status = models.IntegerField(default=0, verbose_name="Cycle Count Status")
    bin_name = models.CharField(max_length=255, verbose_name="Bin Name")
    goods_code = models.CharField(max_length=255, verbose_name="Goods Code")
    goods_qty = models.BigIntegerField(default=0, verbose_name="On Hand Stock")
    physical_inventory = models.BigIntegerField(default=0, verbose_name="Goods Code")
    difference = models.BigIntegerField(default=0, verbose_name="Goods Code")
    creater = models.CharField(max_length=255, verbose_name="Who Create")
    create_time = models.DateField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'cyclecountday'
        verbose_name = 'data id'
        verbose_name_plural = "data id"
        ordering = ['openid']

    def __str__(self):
        return self.pk
