from django.urls import path
from . import views

urlpatterns = [
path(r'goodslistfile/', views.GoodlistfileViewSet.as_view(), name="goodslistfile"),
path(r'supplierfile/', views.SupplierfileViewSet.as_view(), name="suppplierfile"),
path(r'customerfile/', views.CustomerfileViewSet.as_view(), name="customerfile"),
path(r'capitalfile/', views.CapitalfileViewSet.as_view(), name="capitalfile"),
path(r'freightfile/', views.FreightfileViewSet.as_view(), name="freightfile")
]
