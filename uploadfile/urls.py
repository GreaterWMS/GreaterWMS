from django.urls import path
from . import views

urlpatterns = [
path(r'goodslistfile/', views.GoodlistfileViewSet.as_view({"post": "create"}), name="goodslistfile"),
path(r'suppplierfile/', views.SupplierfileViewSet.as_view({"post": "create"}), name="suppplierfile"),
path(r'customerfile/', views.GoodlistfileViewSet.as_view({"post": "create"}), name="customerfile"),
]
