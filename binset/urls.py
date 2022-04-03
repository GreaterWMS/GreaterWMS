from django.urls import path, re_path
from . import views

urlpatterns = [
path(r'', views.APIViewSet.as_view({"get": "list", "post": "create"}), name="binset"),
path(r'file/', views.FileDownloadView.as_view({"get": "list"}), name="binsetfiledownload"),
re_path(r'^(?P<pk>\d+)/$', views.APIViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}), name="binset_1"),
path(r'scannerbintag/<str:bar_code>/',views.ScannerBinsetTagView.as_view({"get":"retrieve"}))
]
