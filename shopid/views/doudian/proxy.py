from rest_framework import viewsets
from shopid.models.douyinmodels import ListModel
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from shopid.filter.douyinfilter import Filter
from rest_framework.exceptions import APIException
from shopid.serializers.douyinserializers import DouYinfileRenderSerializer

class DouYinProxyAPI(viewsets.ModelViewSet):
    """
        create:
            是否开启代理IP，Int类型，1为开启代理，0为关闭代理
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_queryset(self):
        if self.request.user:
            return ListModel.objects.filter(openid=self.request.auth.openid)
        else:
            return ListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['create']:
            return DouYinfileRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        if 't_code' not in data:
            raise APIException({'detail': '请提交该店铺的唯一值'})
        if 'proxy' not in data:
            raise APIException({'detail': '代理开启还是关闭，开启是1，关闭是0'})
        if 'proxy' in data:
            qs = ListModel.objects.filter(t_code=data['t_code'])
            if int(data['proxy']) == 0:
                qs.update(proxy=0, proxy_ip={})
                data['result'] = 'success'
                return Response(data, status=200)
            elif int(data['proxy']) == 1:
                if 'proxy_ip' not in data:
                    raise APIException({'detail': '请输入代理ip，是个json格式{}'})
                else:
                    qs.update(proxy=1, proxy_ip=data['proxy_ip'])
                    data['result'] = 'success'
                    return Response(data, status=200)
            else:
                raise APIException({'detail': '请proxy调整成开启还是关闭，开启是1，关闭是0'})