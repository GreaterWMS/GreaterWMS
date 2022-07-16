from django.db import models

class ListModel(models.Model):
    mode = models.CharField(max_length=255, verbose_name="Request Mode")
    code = models.CharField(max_length=255, verbose_name="Request Code")
    bar_code = models.CharField(max_length=255, verbose_name="Bar Code")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'scanner'
        verbose_name = 'Scanner'
        verbose_name_plural = "Scanner"
        ordering = ['-id']

    def __int__(self):
        return self.pk
