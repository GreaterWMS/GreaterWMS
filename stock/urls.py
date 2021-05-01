from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
path(r'list/', views.StockListViewSet.as_view({"get": "list"}), name="list"),
path(r'bin/', views.StockBinViewSet.as_view({"get": "list"}), name="bin"),
re_path(r'^bin/(?P<pk>\d+)/$', views.StockBinViewSet.as_view({
    'get': 'retrieve',
    'post': 'create'
}), name="bin_1"),
path(r'filelist/', views.FileListDownloadView.as_view({"get": "list"}), name="stocklistfilelistdownload"),
path(r'filebinlist/', views.FileBinListDownloadView.as_view({"get": "list"}), name="binlistfiledetaildownload")
]
