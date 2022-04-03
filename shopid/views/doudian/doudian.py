from rest_framework import viewsets
from shopid.models.douyinmodels import ListModel
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from shopid.filter.douyinfilter import Filter
from rest_framework.exceptions import APIException
from utils.md5 import Md5
from shopid.files.douyinfiles import DouYinfileRenderCN
from rest_framework.settings import api_settings
from shopid.serializers.douyinserializers import DouYinfileRenderSerializer
from django.http import StreamingHttpResponse

class DouYinInitAPI(viewsets.ModelViewSet):
    """
        list:
            获得该企业的所有抖音店铺列表
        create:
            创建一个店铺
        delete:
            删除一个店铺
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return ListModel.objects.filter(shop_mode="douyin")
            else:
                return ListModel.objects.filter(shop_mode="douyin", id=id)
        else:
            return ListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list', 'create', 'destroy']:
            return DouYinfileRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        if 'shop_name' not in data:
            raise APIException({'detail': '请提交该店铺的店铺名称'})
        if 'shop_appid' not in data:
            raise APIException({'detail': '请提交该店铺的appid'})
        if 'shop_app_secret' not in data:
            raise APIException({'detail': '请提交该店铺的shop_app_secret'})
        if 'shop_id' not in data:
            raise APIException({'detail': '请提交该店铺的shop_id'})
        if ListModel.objects.filter(openid=self.request.auth.openid,
                                    appid=self.request.auth.appid,
                                    shop_name=data['shop_name'],
                                    shop_mode='douyin',
                                    shop_appid=data['shop_appid'],
                                    shop_app_secret=data['shop_app_secret'],
                                    shop_id=data['shop_id']).exists():
            raise APIException({"detail": "数据已经存在"})
        else:
            t_code = Md5.md5(data['shop_appid'])
            ListModel.objects.create(openid=self.request.auth.openid,
                                     appid=self.request.auth.appid,
                                     shop_name=data['shop_name'],
                                     shop_mode='douyin',
                                     shop_appid=str(data['shop_appid']),
                                     shop_app_secret=str(data['shop_app_secret']),
                                     shop_id=str(data['shop_id']),
                                     t_code=t_code)
            data['result'] = 'success'
            data['t_code'] = t_code
            return Response(data, status=200)

    def destroy(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "不可以删除别人的数据"})
        else:
            qs.delete()
            return Response({"result": "该商店已经删除"})

class DouYinfileDownloadView(viewsets.ModelViewSet):
    renderer_classes = (DouYinfileRenderCN, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return ListModel.objects.filter(openid=self.request.auth.openid)
            else:
                return ListModel.objects.filter(openid=self.request.auth.openid, id=id)
        else:
            return ListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return DouYinfileRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def get_lang(self, data):
        lang = self.request.META.get('HTTP_LANGUAGE')
        if lang:
            if lang == 'zh-hans':
                return DouYinfileRenderCN().render(data)
            else:
                return DouYinfileRenderCN().render(data)
        else:
            return DouYinfileRenderCN().render(data)

    def list(self, request, *args, **kwargs):
        from datetime import datetime
        dt = datetime.now()
        data = (
            DouYinfileRenderSerializer(instance).data
            for instance in self.filter_queryset(self.get_queryset())
        )
        renderer = self.get_lang(data)
        response = StreamingHttpResponse(
            renderer,
            content_type="text/csv"
        )
        response['Content-Disposition'] = "attachment; filename='freight_{}.csv'".format(str(dt.strftime('%Y%m%d%H%M%S%f')))
        return response