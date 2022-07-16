from django.db import models

class ListModel(models.Model):
    staff_name = models.CharField(max_length=255, verbose_name="Staff Name")
    staff_type = models.CharField(max_length=255, verbose_name="Staff Type")
    check_code = models.IntegerField(default=8888, verbose_name="Check Code")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")
    error_check_code_counter = models.IntegerField(default=0,verbose_name='check_code error counter')
    is_lock = models.BooleanField(default=False,verbose_name='Whether the lock')
    class Meta:
        db_table = 'staff'
        verbose_name = 'Staff'
        verbose_name_plural = "Staff"
        ordering = ['staff_name']

    def __int__(self):
        return self.pk

class TypeListModel(models.Model):
    staff_type = models.CharField(max_length=255, verbose_name="Staff Type")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    creater = models.CharField(max_length=255, verbose_name="Creater")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'stafftype'
        verbose_name = 'Staff Type'
        verbose_name_plural = "Staff Type"
        ordering = ['staff_type']

    def __int__(self):
        return self.pk
