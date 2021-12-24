from django.urls import path
from . import views

urlpatterns = [
path(r'', views.ListViewSet.as_view({"get": "list"}), name="scanner"),
path(r'list/<str:bar_code>/', views.SannerView.as_view({"get": "retrieve"})),
path(r'sanerpicking/' , views.SannerDnDetailPickingListView.as_view({"get":"list"}),name="sanerpicking"),
]
