from django.urls import path, re_path
from . import views

urlpatterns = [
path(r'', views.APIViewSet.as_view({"get": "list", "post": "create"}), name="goods"),
path(r'file/', views.FileDownloadView.as_view({"get": "list"}), name="goodslistfiledownload"),
re_path(r'^(?P<pk>\d+)/', views.APIViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}), name="goods_1"),
    path(r'goodstag/<str:bar_code>/',views.SannerGoodsTagView.as_view({"get":"retrieve"}))
]
