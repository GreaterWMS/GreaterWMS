from django.db import models

class ListModel(models.Model):
    customer_id = models.CharField(max_length=255, verbose_name="ID")
    customer_name = models.CharField(max_length=255, verbose_name="Name")
    customer_group = models.CharField(max_length=255, verbose_name="Group")
    customer_contact = models.CharField(max_length=255, verbose_name="Contact")
    customer_bank_account = models.CharField(max_length=255, verbose_name="Bank Account")
    customer_password = models.CharField(max_length=255, verbose_name="Password")
    customer_refrigeration_fee = models.BigIntegerField(default=0, verbose_name="Refrigeration Fee")
    customer_loading_fee = models.BigIntegerField(default=0, verbose_name="Loading Fee")
    customer_film_laminating_fee = models.BigIntegerField(default=0, verbose_name="Film-Laminating Fee")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name="Delete Label")
    create_time = models.DateTimeField(max_length=255, verbose_name="Create Time")

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = "Customer"
        ordering = ['customer_name']

    def __str__(self):
        return self.customer_name
