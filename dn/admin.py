from django.contrib import admin
from .models import DnListModel, DnDetailModel, PickingListModel

admin.site.register(DnListModel)
admin.site.register(DnDetailModel)
admin.site.register(PickingListModel)
