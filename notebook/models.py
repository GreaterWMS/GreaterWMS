from django.db import models

class NoteBook(models.Model):
    openid = models.CharField(max_length=80, verbose_name="openid")
    icon = models.CharField(max_length=80, verbose_name="图标名称")
    icon_color = models.CharField(max_length=80, verbose_name="图标颜色")
    title = models.CharField(max_length=80, verbose_name='标题')
    desc = models.CharField(max_length=2000, verbose_name='内容')
    progress = models.IntegerField(default=0, verbose_name='进度')
    note_day = models.DateField(verbose_name='备忘录日期')
    is_delete = models.IntegerField(default=0, verbose_name='删除标记')
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
