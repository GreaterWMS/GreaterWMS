from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
path(r'', views.APIViewSet.as_view({"get": "list"}), name="chat"),
path(r'read/', views.ReadAPI.as_view({"get": "list"}), name='read')
]
