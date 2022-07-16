from django.contrib import admin
from .models import AsnListModel, AsnDetailModel

admin.site.register(AsnListModel)
admin.site.register(AsnDetailModel)
