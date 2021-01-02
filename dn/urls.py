"""singosgu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
path(r'list/', views.DnListViewSet.as_view({"get": "list", "post": "create"}), name="dnlist"),
re_path(r'^list/(?P<pk>\d+)/$', views.DnListViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}), name="dnlist_1"),
path(r'detail/', views.DnDetailViewSet.as_view({"get": "list", "post": "create", 'put': 'update'}), name="dndetail"),
re_path(r'^detail/(?P<pk>\d+)/$', views.DnDetailViewSet.as_view({
    'get': 'retrieve',
}), name="dndetail_1"),
re_path(r'^viewprint/(?P<pk>\d+)/$', views.DnViewPrintViewSet.as_view({
    'get': 'retrieve',
}), name="dnviewprint_1"),
re_path(r'^neworder/(?P<pk>\d+)/$', views.DnNewOrderViewSet.as_view({
    'post': 'create',
}), name="preloadid_1"),
path(r'orderrelease/', views.DnOrderReleaseViewSet.as_view({"post": "create"}), name="orderrelease"),
re_path(r'^orderrelease/(?P<pk>\d+)/$', views.DnOrderReleaseViewSet.as_view({
    'put': 'update',
}), name="orderrelease_1"),
re_path(r'^sorted/(?P<pk>\d+)/$', views.DnSortedViewSet.as_view({
    'post': 'create',
}), name="sorted_1"),
re_path(r'^movetobin/(?P<pk>\d+)/$', views.MoveToBinViewSet.as_view({
    'post': 'create',
}), name="movetobin_1"),
]
