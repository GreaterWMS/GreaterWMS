from django.db import models

class TransportationFeeListModel(models.Model):
    send_city = models.CharField(max_length=255, verbose_name="Send City")
    receiver_city = models.CharField(max_length=255, verbose_name="Receiver City")
    weight_fee = models.FloatField(default=0, verbose_name="Weight Fee")
    volume_fee = models.FloatField(default=0, verbose_name="Volume Fee")
    min_payment = models.FloatField(default=0, verbose_name="Min Payment")
    transportation_supplier = models.CharField(max_length=255, verbose_name="Transportation Supplier")
    creater = models.CharField(max_length=255, verbose_name="Who Created")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'transportationfee'
        verbose_name = 'Transportation Fee'
        verbose_name_plural = "Transportation Fee"
        ordering = ['-id']

    def __int__(self):
        return self.pk
