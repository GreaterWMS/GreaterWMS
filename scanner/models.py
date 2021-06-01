from django.db import models

class ListModel(models.Model):
    mode = models.CharField(max_length=255, verbose_name="Request Mode")
    code = models.CharField(max_length=255, verbose_name="Request Code")
    bar_code = models.CharField(max_length=255, verbose_name="Bar Code")
    openid = models.CharField(max_length=255, verbose_name="Openid")

    class Meta:
        db_table = 'scanner'
        verbose_name = 'data id'
        verbose_name_plural = "data id"
        ordering = ['-id']

    def __str__(self):
        return self.pk
