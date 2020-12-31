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
path(r'list/', views.StockListViewSet.as_view({"get": "list"}), name="list"),
path(r'bin/', views.StockBinViewSet.as_view({"get": "list"}), name="bin"),
re_path(r'^bin/(?P<pk>\d+)/$', views.StockBinViewSet.as_view({
    'get': 'retrieve',
    'post': 'create'
}), name="bin_1"),
]
