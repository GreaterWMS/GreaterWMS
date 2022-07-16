from django.db import models

class ListModel(models.Model):
    capital_name = models.CharField(max_length=255, verbose_name="Capital Name")
    capital_qty = models.BigIntegerField(default=0, verbose_name="Capital Qty")
    capital_cost = models.FloatField(default=0, verbose_name="Capital Cost")
    creater = models.CharField(max_length=255, verbose_name="Who Created")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'capital'
        verbose_name = 'Capital'
        verbose_name_plural = "Capital"
        ordering = ['-id']

    def __int__(self):
        return self.pk
