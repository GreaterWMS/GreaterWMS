from django.urls import path, re_path
from . import views

urlpatterns = [
path(r'', views.CyclecountModeDayViewSet.as_view({"get": "list", "post": "create", "put": "update", "patch": "partial_update"}), name="cyclecount"),
]
