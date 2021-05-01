from django.urls import path, re_path
from . import views

urlpatterns = [
path(r'freight/', views.TransportationFeeListViewSet.as_view({"get": "list", "post": "create"}), name="transportationfee"),
re_path(r'^freight/(?P<pk>\d+)/$', views.TransportationFeeListViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}), name="transportationfee_1")
]
