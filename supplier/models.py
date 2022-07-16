from django.db import models

class ListModel(models.Model):
    supplier_name = models.CharField(max_length=255, verbose_name="Supplier Name")
    supplier_city = models.CharField(max_length=255, verbose_name="Supplier City")
    supplier_address = models.CharField(max_length=255, verbose_name="Supplier Address")
    supplier_contact = models.CharField(max_length=255, verbose_name="Supplier Contact")
    supplier_manager = models.CharField(max_length=255, verbose_name="Supplier Manager")
    supplier_level = models.BigIntegerField(default=1, verbose_name="Supplier Level")
    creater = models.CharField(max_length=255, verbose_name="Who Created")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Supplier'
        verbose_name_plural = "Supplier"
        ordering = ['supplier_name']

    def __int__(self):
        return self.pk
