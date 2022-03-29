from django.urls import path, re_path
from .views.doudian.doudian import DouYinInitAPI, DouYinfileDownloadView
from .views.doudian.sandbox import DouYinSandBoxAPI
from .views.doudian.proxy import DouYinProxyAPI

urlpatterns = [
path(r'douyin/', DouYinInitAPI.as_view({"get": "list", "post": "create"}), name="douyin_init"),
re_path(r'^douyin/(?P<pk>\d+)/$', DouYinInitAPI.as_view({
    'delete': 'destroy'
}), name="douyin_init_1"),
path(r'douyin/sandbox/', DouYinSandBoxAPI.as_view({"post": "create"}), name="douyin_sandbox"),
path(r'douyin/proxy/', DouYinProxyAPI.as_view({"post": "create"}), name="douyin_proxy"),
path(r'douyin/file/', DouYinfileDownloadView.as_view({"get": "list"}), name="DouYinfileDownload"),
]
