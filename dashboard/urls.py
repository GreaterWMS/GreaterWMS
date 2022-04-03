from django.urls import path, re_path
from . import views

urlpatterns = [
path(r'receipts/', views.ReceiptsViewSet.as_view({"get": "list"}), name="receipts"),
path(r'sales/', views.SalesViewSet.as_view({"get": "list"}), name="sales")
]
