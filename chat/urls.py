from django.urls import path
from . import views

urlpatterns = [
path(r'', views.APIViewSet.as_view({"get": "list"}), name="chat"),
path(r'read/', views.ReadAPI.as_view({"get": "list"}), name='read')
]
