from django.db import models

class AsnListModel(models.Model):
    asn_code = models.CharField(max_length=255, verbose_name="ASN Code")
    asn_status = models.BigIntegerField(default=1, verbose_name="ASN Status")
    total_weight = models.FloatField(default=0, verbose_name="Total Weight")
    total_volume = models.FloatField(default=0, verbose_name="Total Volume")
    total_cost = models.FloatField(default=0, verbose_name="Total Cost")
    supplier = models.CharField(max_length=255, verbose_name="ASN Supplier")
    creater = models.CharField(max_length=255, verbose_name="Who Created")
    bar_code = models.CharField(max_length=255, verbose_name="Bar Code")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    transportation_fee = models.JSONField(default=dict, verbose_name="Transportation Fee")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'asnlist'
        verbose_name = 'ASN List'
        verbose_name_plural = "ASN List"
        ordering = ['-id']

    def __int__(self):
        return self.pk

class AsnDetailModel(models.Model):
    asn_code = models.CharField(max_length=255, verbose_name="ASN Code")
    asn_status = models.BigIntegerField(default=1, verbose_name="ASN Status")
    supplier = models.CharField(max_length=255, verbose_name="ASN Supplier")
    goods_code = models.CharField(max_length=255, verbose_name="Goods Code")
    goods_desc = models.CharField(max_length=255, verbose_name="Goods Description")
    goods_qty = models.BigIntegerField(default=0, verbose_name="Goods QTY")
    goods_actual_qty = models.BigIntegerField(default=0, verbose_name="Goods Actual QTY")
    sorted_qty = models.BigIntegerField(default=0, verbose_name="Sorted QTY")
    goods_shortage_qty = models.BigIntegerField(default=0, verbose_name="Goods Shortage QTY")
    goods_more_qty = models.BigIntegerField(default=0, verbose_name="Goods More QTY")
    goods_damage_qty = models.BigIntegerField(default=0, verbose_name="Goods damage QTY")
    goods_weight = models.FloatField(default=0, verbose_name="Goods Weight")
    goods_volume = models.FloatField(default=0, verbose_name="Goods Volume")
    goods_cost = models.FloatField(default=0, verbose_name="Goods Cost")
    creater = models.CharField(max_length=255, verbose_name="Who Created")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'asndetail'
        verbose_name = 'ASN Detail'
        verbose_name_plural = "ASN Detail"
        ordering = ['-id']

    def __int__(self):
        return self.pk

