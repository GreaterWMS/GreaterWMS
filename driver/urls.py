from django.urls import path, re_path
from . import views

urlpatterns = [
path(r'', views.APIViewSet.as_view({"get": "list", "post": "create"}), name="driver"),
path(r'file/', views.FileDownloadView.as_view({"get": "list"}), name="driverfiledownload"),
re_path(r'^(?P<pk>\d+)/$', views.APIViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}), name="driver_1"),
path(r'dispatchlist/', views.DispatchListViewSet.as_view({"get": "list"}), name="dispatchlist"),
re_path(r'^dispatchlist/(?P<pk>\d+)/$', views.DispatchListViewSet.as_view({
    'get': 'retrieve',
}), name="dispatchlist_1")
]
