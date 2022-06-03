from rest_framework import viewsets
from shopid.models.douyinmodels import ListModel
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from shopid.filter.douyinfilter import Filter
from rest_framework.exceptions import APIException
from shopid.serializers.douyinserializers import DouYinfileRenderSerializer

class DouYinSandBoxAPI(viewsets.ModelViewSet):
    """
        create:
            沙箱环境，Int类型，1为沙箱环境，0为正式环境
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
        if 'sandbox' not in data:
            raise APIException({'detail': '请sandbox调整成开启还是关闭，开始是1，关闭是0'})
        if 'sandbox' in data:
            if int(data['sandbox']) != 0 or int(data['sandbox']) != 1:
                raise APIException({'detail': '沙箱环境只接受1，或者0'})
        qs = ListModel.objects.filter(t_code=data['t_code'])
        if qs.exists():
            qs.update(sandbox=int(data['sandbox']))
            data['result'] = 'success'
            return Response(data, status=200)
        else:
            raise APIException({"detail": "店铺不存在"})