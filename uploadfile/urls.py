from django.urls import path
from . import views

urlpatterns = [
path(r'goodslist/', views.GoodlistViewSet.as_view({"post": "create"}), name="goodslist")
]
