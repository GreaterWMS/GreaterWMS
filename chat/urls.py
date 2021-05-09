from django.urls import path
from . import views

urlpatterns = [
path(r'', views.ChatViewSet.as_view({"get": "list"}), name="chat"),
path(r'read/', views.ReadAPI.as_view({"get": "list"}), name='read')
]
