from django.db import models

class ListModel(models.Model):
    sender = models.CharField(max_length=100, verbose_name='Sender')
    receiver = models.CharField(max_length=100, verbose_name='Receiver')
    read = models.BooleanField(default=False, verbose_name="Readed")
    detail = models.CharField(max_length=100, verbose_name='Chat text')
    is_delete = models.BooleanField(default=False, verbose_name='Delete label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create time')
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Update time')

    class Meta:
        db_table = 'chat'
        verbose_name = 'Chat'
        verbose_name_plural = "Chat"
        ordering = ['-id']

    def __int__(self):
        return self.pk
