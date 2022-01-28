from django.urls import path, re_path
from . import views

urlpatterns = [
path(r'list/', views.AsnListViewSet.as_view({"get": "list", "post": "create"}), name="asnlist"),
re_path(r'^list/(?P<pk>\d+)/$', views.AsnListViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}), name="asnlist_1"),
path(r'detail/', views.AsnDetailViewSet.as_view({"get": "list", "post": "create", 'put': 'update'}), name="asndetail"),
re_path(r'^detail/(?P<pk>\d+)/$', views.AsnDetailViewSet.as_view({
    'get': 'retrieve',
}), name="asndetail_1"),
re_path(r'^viewprint/(?P<pk>\d+)/$', views.AsnViewPrintViewSet.as_view({
    'get': 'retrieve',
}), name="asnviewprint_1"),
re_path(r'^preload/(?P<pk>\d+)/$', views.AsnPreLoadViewSet.as_view({
    'post': 'create',
}), name="preload_1"),
re_path(r'^presort/(?P<pk>\d+)/$', views.AsnPreSortViewSet.as_view({
    'post': 'create',
}), name="presort_1"),
path(r'sorted/', views.AsnSortedViewSet.as_view({"put": "update"}), name="sorted"),
re_path(r'^sorted/(?P<pk>\d+)/$', views.AsnSortedViewSet.as_view({
    'post': 'create'
}), name="sorted_1"),
path(r'movetobin/', views.MoveToBinViewSet.as_view({'put': 'update'}), name="movetobin"),
re_path(r'^movetobin/(?P<pk>\d+)/$', views.MoveToBinViewSet.as_view({
    'post': 'create',
}), name="movetobin_1"),
path(r'filelist/', views.FileListDownloadView.as_view({"get": "list"}), name="asnfilelistdownload"),
path(r'filedetail/', views.FileDetailDownloadView.as_view({"get": "list"}), name="asnfiledetaildownload"),
]
