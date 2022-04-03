from django.urls import path, re_path
from . import views

urlpatterns = [
path(r'', views.APIViewSet.as_view({"get": "list", "post": "create"}), name="staff"),
path(r'type/', views.TypeAPIViewSet.as_view({"get": "list"}), name="stafftype"),
path(r'file/', views.FileDownloadView.as_view({"get": "list"}), name="stafffiledownload"),
re_path(r'^(?P<pk>\d+)/$', views.APIViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}), name="staff_1")
]
