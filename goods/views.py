from rest_framework import viewsets
from .models import ListModel
from . import serializers
from .page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import Filter
from rest_framework.exceptions import APIException
from goodsunit.models import ListModel as goods_unit
from goodsclass.models import ListModel as goods_class
from goodsbrand.models import ListModel as goods_brand
from goodscolor.models import ListModel as goods_color
from goodsshape.models import ListModel as goods_shape
from goodsspecs.models import ListModel as goods_specs
from goodsorigin.models import ListModel as goods_origin
from supplier.models import ListModel as supplier
from scanner.models import ListModel as scanner
from utils.md5 import Md5
from .serializers import FileRenderSerializer
from django.http import StreamingHttpResponse
from .files import FileRenderCN, FileRenderEN
from rest_framework.settings import api_settings
from asn.models import AsnDetailModel

class SannerGoodsTagView(viewsets.ModelViewSet):

    """
    retrieve:
        Response a data retrieve（get）

    """

    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter
    lookup_field = 'bar_code'
    def get_project(self):
        try:
            bar_code = self.kwargs['bar_code']
            return bar_code
        except:
            return None

    def get_queryset(self):
        bar_code = self.get_project()
        if self.request.user:
            if bar_code is None:
                return ListModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return ListModel.objects.filter(openid=self.request.auth.openid, bar_code=bar_code, is_delete=False)
        else:
            return ListModel.objects.filter().none()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'destroy']:
            return serializers.GoodsGetSerializer
        elif self.action in ['create']:
            return serializers.GoodsPostSerializer
        elif self.action in ['update']:
            return serializers.GoodsUpdateSerializer
        elif self.action in ['partial_update']:
            return serializers.GoodsPartialUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def retrieve(self, request, *args, **kwargs):
        data=self.request.GET.get('asn_code')
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        good_detail=AsnDetailModel.objects.filter(asn_code=data,goods_code=serializer.data['goods_code']).first()
        if good_detail is None:
            raise APIException({"detail":"The product label does not exist"})
        else:
            context = {}
            context['goods_code'] = good_detail.goods_code
            context['goods_actual_qty'] = good_detail.goods_actual_qty
        return Response(context, status=200)

class APIViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）

        list:
            Response a data list（all）

        create:
            Create a data line（post）

        delete:
            Delete a data line（delete)

        partial_update:
            Partial_update a data（patch：partial_update）

        update:
            Update a data（put：update）
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
                return ListModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return ListModel.objects.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return ListModel.objects.filter().none()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'destroy']:
            return serializers.GoodsGetSerializer
        elif self.action in ['create']:
            return serializers.GoodsPostSerializer
        elif self.action in ['update']:
            return serializers.GoodsUpdateSerializer
        elif self.action in ['partial_update']:
            return serializers.GoodsPartialUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        data['openid'] = self.request.auth.openid
        data['unit_volume'] = round(
            (float(data['goods_w']) * float(data['goods_d']) * float(data['goods_h'])) / 1000000000, 4)
        if ListModel.objects.filter(openid=data['openid'], goods_code=data['goods_code'], is_delete=False).exists():
            raise APIException({"detail": "Data Exists"})
        else:
            if supplier.objects.filter(openid=data['openid'], supplier_name=data['goods_supplier'],
                                        is_delete=False).exists():
                if goods_unit.objects.filter(openid=data['openid'], goods_unit=data['goods_unit'],
                                           is_delete=False).exists():
                    if goods_class.objects.filter(openid=data['openid'], goods_class=data['goods_class'],
                                                 is_delete=False).exists():
                        if goods_brand.objects.filter(openid=data['openid'], goods_brand=data['goods_brand'],
                                                     is_delete=False).exists():
                            if goods_color.objects.filter(openid=data['openid'], goods_color=data['goods_color'],
                                                         is_delete=False).exists():
                                if goods_shape.objects.filter(openid=data['openid'], goods_shape=data['goods_shape'],
                                                             is_delete=False).exists():
                                    if goods_specs.objects.filter(openid=data['openid'],
                                                                 goods_specs=data['goods_specs'],
                                                                 is_delete=False).exists():
                                        if goods_origin.objects.filter(openid=data['openid'],
                                                                     goods_origin=data['goods_origin'],
                                                                     is_delete=False).exists():
                                            data['bar_code'] = Md5.md5(data['goods_code'])
                                            serializer = self.get_serializer(data=data)
                                            serializer.is_valid(raise_exception=True)
                                            serializer.save()
                                            scanner.objects.create(openid=self.request.auth.openid, mode="GOODS",
                                                                   code=data['goods_code'],
                                                                   bar_code=data['bar_code'])
                                            headers = self.get_success_headers(serializer.data)
                                            return Response(serializer.data, status=200, headers=headers)
                                        else:
                                            raise APIException(
                                                {"detail": "Goods Origin does not exists or it has been changed"})
                                    else:
                                        raise APIException(
                                            {"detail": "Goods Specs does not exists or it has been changed"})
                                else:
                                    raise APIException({"detail": "Goods Shape does not exists or it has been changed"})
                            else:
                                raise APIException({"detail": "Goods Color does not exists or it has been changed"})
                        else:
                            raise APIException({"detail": "Goods Brand does not exists or it has been changed"})
                    else:
                        raise APIException({"detail": "Goods Class does not exists or it has been changed"})
                else:
                    raise APIException({"detail": "Goods Unit does not exists or it has been changed"})
            else:
                raise APIException({"detail": "Supplier does not exists or it has been changed"})

    def update(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot update data which not yours"})
        else:
            data = self.request.data
            data['unit_volume'] = round(
                (float(data['goods_w']) * float(data['goods_d']) * float(data['goods_h'])) / 1000000000, 4)
            if supplier.objects.filter(openid=self.request.auth.openid, supplier_name=data['goods_supplier'],
                                        is_delete=False).exists():
                if goods_unit.objects.filter(openid=self.request.auth.openid, goods_unit=data['goods_unit'],
                                               is_delete=False).exists():
                    if goods_class.objects.filter(openid=self.request.auth.openid, goods_class=data['goods_class'],
                                                  is_delete=False).exists():
                        if goods_brand.objects.filter(openid=self.request.auth.openid, goods_brand=data['goods_brand'],
                                                      is_delete=False).exists():
                            if goods_color.objects.filter(openid=self.request.auth.openid, goods_color=data['goods_color'],
                                                            is_delete=False).exists():
                                if goods_shape.objects.filter(openid=self.request.auth.openid, goods_shape=data['goods_shape'],
                                                                is_delete=False).exists():
                                    if goods_specs.objects.filter(openid=self.request.auth.openid,
                                                                  goods_specs=data['goods_specs'],
                                                                  is_delete=False).exists():
                                        if goods_origin.objects.filter(openid=self.request.auth.openid,
                                                                       goods_origin=data['goods_origin'],
                                                                       is_delete=False).exists():
                                            scanner.objects.filter(openid=self.request.auth.openid,
                                                                   mode='GOODS',
                                                                   code=qs.goods_code).update(code=str(data['goods_code']))
                                            serializer = self.get_serializer(qs, data=data)
                                            serializer.is_valid(raise_exception=True)
                                            serializer.save()
                                            headers = self.get_success_headers(serializer.data)
                                            return Response(serializer.data, status=200, headers=headers)
                                        else:
                                            raise APIException(
                                                {"detail": "Goods Origin does not exists or it has been changed"})
                                    else:
                                        raise APIException(
                                            {"detail": "Goods Specs does not exists or it has been changed"})
                                else:
                                    raise APIException({"detail": "Goods Shape does not exists or it has been changed"})
                            else:
                                raise APIException({"detail": "Goods Color does not exists or it has been changed"})
                        else:
                            raise APIException({"detail": "Goods Brand does not exists or it has been changed"})
                    else:
                        raise APIException({"detail": "Goods Class does not exists or it has been changed"})
                else:
                    raise APIException({"detail": "Goods Unit does not exists or it has been changed"})
            else:
                raise APIException({"detail": "Supplier does not exists or it has been changed"})

    def partial_update(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot partial_update data which not yours"})
        else:
            data = self.request.data
            if supplier.objects.filter(openid=self.request.auth.openid, supplier_name=data['goods_supplier'],
                                        is_delete=False).exists():
                if goods_unit.objects.filter(openid=self.request.auth.openid, goods_unit=data['goods_unit'],
                                               is_delete=False).exists():
                    if goods_class.objects.filter(openid=self.request.auth.openid, goods_class=data['goods_class'],
                                                  is_delete=False).exists():
                        if goods_brand.objects.filter(openid=self.request.auth.openid, goods_brand=data['goods_brand'],
                                                      is_delete=False).exists():
                            if goods_color.objects.filter(openid=self.request.auth.openid, goods_color=data['goods_color'],
                                                            is_delete=False).exists():
                                if goods_shape.objects.filter(openid=self.request.auth.openid, goods_shape=data['goods_shape'],
                                                                is_delete=False).exists():
                                    if goods_specs.objects.filter(openid=self.request.auth.openid,
                                                                  goods_specs=data['goods_specs'],
                                                                  is_delete=False).exists():
                                        if goods_origin.objects.filter(openid=self.request.auth.openid,
                                                                       goods_origin=data['goods_origin'],
                                                                       is_delete=False).exists():
                                            scanner.objects.filter(openid=self.request.auth.openid,
                                                                   mode='GOODS',
                                                                   code=qs.goods_code).update(
                                                code=str(data['goods_code']))
                                            serializer = self.get_serializer(qs, data=data, partial=True)
                                            serializer.is_valid(raise_exception=True)
                                            serializer.save()
                                            headers = self.get_success_headers(serializer.data)
                                            return Response(serializer.data, status=200, headers=headers)
                                        else:
                                            raise APIException(
                                                {"detail": "Goods Origin does not exists or it has been changed"})
                                    else:
                                        raise APIException(
                                            {"detail": "Goods Specs does not exists or it has been changed"})
                                else:
                                    raise APIException({"detail": "Goods Shape does not exists or it has been changed"})
                            else:
                                raise APIException({"detail": "Goods Color does not exists or it has been changed"})
                        else:
                            raise APIException({"detail": "Goods Brand does not exists or it has been changed"})
                    else:
                        raise APIException({"detail": "Goods Class does not exists or it has been changed"})
                else:
                    raise APIException({"detail": "Goods Unit does not exists or it has been changed"})
            else:
                raise APIException({"detail": "Supplier does not exists or it has been changed"})

    def destroy(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot delete data which not yours"})
        else:
            qs.is_delete = True
            qs.save()
            serializer = self.get_serializer(qs, many=False)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

class FileDownloadView(viewsets.ModelViewSet):
    renderer_classes = (FileRenderCN, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
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
                return ListModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return ListModel.objects.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return ListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.FileRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def get_lang(self, data):
        lang = self.request.META.get('HTTP_LANGUAGE')
        if lang:
            if lang == 'zh-hans':
                return FileRenderCN().render(data)
            else:
                return FileRenderEN().render(data)
        else:
            return FileRenderEN().render(data)

    def list(self, request, *args, **kwargs):
        from datetime import datetime
        dt = datetime.now()
        data = (
            FileRenderSerializer(instance).data
            for instance in self.filter_queryset(self.get_queryset())
        )
        renderer = self.get_lang(data)
        response = StreamingHttpResponse(
            renderer,
            content_type="text/csv"
        )
        response['Content-Disposition'] = "attachment; filename='goodslist_{}.csv'".format(str(dt.strftime('%Y%m%d%H%M%S%f')))
        return response
