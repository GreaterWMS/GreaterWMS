from django.db import models

class QTYRecorder(models.Model):
    openid = models.CharField(max_length=255, verbose_name="Openid")
    mode_code = models.CharField(max_length=255, verbose_name="Transaction Mode")
    bin_name = models.CharField(max_length=255, verbose_name="Bin Name")
    goods_code = models.CharField(max_length=255, verbose_name="Goods Code")
    goods_desc = models.CharField(max_length=255, verbose_name="Goods Description")
    goods_qty = models.BigIntegerField(default=0, verbose_name="On Hand Stock")
    creater = models.CharField(max_length=255, verbose_name="Who Create")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'qtyrecorder'
        verbose_name = 'QTY Recorder'
        verbose_name_plural = "QTY Recorder"
        ordering = ['-id']

    def __int__(self):
        return self.pk

class CyclecountModeDayModel(models.Model):
    openid = models.CharField(max_length=255, verbose_name="Openid")
    cyclecount_status = models.IntegerField(default=0, verbose_name="Cycle Count Status")
    bin_name = models.CharField(max_length=255, verbose_name="Bin Name")
    goods_code = models.CharField(max_length=255, verbose_name="Goods Code")
    goods_qty = models.BigIntegerField(default=0, verbose_name="On Hand Stock")
    physical_inventory = models.BigIntegerField(default=0, verbose_name="Goods Code")
    difference = models.BigIntegerField(default=0, verbose_name="Goods Code")
    creater = models.CharField(max_length=255, verbose_name="Who Create")
    t_code = models.CharField(max_length=255, verbose_name="Transaction Code")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'cyclecountday'
        verbose_name = 'Cyclecount Day'
        verbose_name_plural = "Cyclecount Day"
        ordering = ['openid']

    def __int__(self):
        return self.pk
