from django.urls import path
from . import views

urlpatterns = [
path(r'', views.ListViewSet.as_view({"get": "list"}), name="scanner"),
]
