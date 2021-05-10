from django.urls import path
from . import views

urlpatterns = [
path(r'goodslistfile/', views.GoodlistfileViewSet.as_view({"post": "create"}), name="goodslistfile")
]
