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
from django.db.models import Q
from .serializers import FileRenderSerializer
from django.http import StreamingHttpResponse
from .files import FileRenderCN, FileRenderEN
from rest_framework.settings import api_settings

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
    queryset = ListModel.objects.all()
    serializer_class = serializers.GoodsGetSerializer
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
                return self.queryset.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.GoodsGetSerializer
        elif self.action == 'retrieve':
            return serializers.GoodsGetSerializer
        elif self.action == 'create':
            return serializers.GoodsPostSerializer
        elif self.action == 'update':
            return serializers.GoodsUpdateSerializer
        elif self.action == 'partial_update':
            return serializers.GoodsPartialUpdateSerializer
        elif self.action == 'destroy':
            return serializers.GoodsGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['openid'] = self.request.auth.openid
        data['unit_volume'] = round(
            (float(data['goods_w']) * float(data['goods_d']) * float(data['goods_h'])) / 1000000000, 8)
        if self.queryset.filter(openid=data['openid'], goods_code=data['goods_code'], is_delete=False).exists():
            raise APIException({"detail": "Data exists"})
        else:
            if supplier.objects.filter(openid=data['openid'], supplier_name=data['goods_supplier'],
                                        is_delete=False).exists():
                if goods_unit.objects.filter(Q(openid=data['openid'], goods_unit=data['goods_unit'],
                                           is_delete=False) |
                                             Q(openid='init_data', goods_unit=data['goods_unit'],
                                           is_delete=False)).exists():
                    if goods_class.objects.filter(openid=data['openid'], goods_class=data['goods_class'],
                                                 is_delete=False).exists():
                        if goods_brand.objects.filter(openid=data['openid'], goods_brand=data['goods_brand'],
                                                     is_delete=False).exists():
                            if goods_color.objects.filter(Q(openid=data['openid'], goods_color=data['goods_color'],
                                                         is_delete=False) |
                                                          Q(openid='init_data', goods_color=data['goods_color'],
                                                         is_delete=False)).exists():
                                if goods_shape.objects.filter(Q(openid=data['openid'], goods_shape=data['goods_shape'],
                                                             is_delete=False) |
                                                              Q(openid='init_data', goods_shape=data['goods_shape'],
                                                             is_delete=False)).exists():
                                    if goods_specs.objects.filter(openid=data['openid'],
                                                                 goods_specs=data['goods_specs'],
                                                                 is_delete=False).exists():
                                        if goods_origin.objects.filter(openid=data['openid'],
                                                                     goods_origin=data['goods_origin'],
                                                                     is_delete=False).exists():
                                            serializer = self.get_serializer(data=data)
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

    def update(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot update data which not yours"})
        else:
            data = request.data
            data['unit_volume'] = round(
                (float(data['goods_w']) * float(data['goods_d']) * float(data['goods_h'])) / 1000000000, 8)
            if supplier.objects.filter(openid=self.request.auth.openid, supplier_name=data['goods_supplier'],
                                        is_delete=False).exists():
                if goods_unit.objects.filter(Q(openid=self.request.auth.openid, goods_unit=data['goods_unit'],
                                               is_delete=False) |
                                             Q(openid='init_data', goods_unit=data['goods_unit'],
                                               is_delete=False)).exists():
                    if goods_class.objects.filter(openid=self.request.auth.openid, goods_class=data['goods_class'],
                                                  is_delete=False).exists():
                        if goods_brand.objects.filter(openid=self.request.auth.openid, goods_brand=data['goods_brand'],
                                                      is_delete=False).exists():
                            if goods_color.objects.filter(Q(openid=self.request.auth.openid, goods_color=data['goods_color'],
                                                            is_delete=False) |
                                                          Q(openid='init_data', goods_color=data['goods_color'],
                                                            is_delete=False)).exists():
                                if goods_shape.objects.filter(Q(openid=self.request.auth.openid, goods_shape=data['goods_shape'],
                                                                is_delete=False) |
                                                              Q(openid='init_data', goods_shape=data['goods_shape'],
                                                                is_delete=False)).exists():
                                    if goods_specs.objects.filter(openid=self.request.auth.openid,
                                                                  goods_specs=data['goods_specs'],
                                                                  is_delete=False).exists():
                                        if goods_origin.objects.filter(openid=self.request.auth.openid,
                                                                       goods_origin=data['goods_origin'],
                                                                       is_delete=False).exists():
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
        if qs.openid != request.auth.openid:
            raise APIException({"detail": "Cannot partial_update data which not yours"})
        else:
            data = request.data
            if supplier.objects.filter(openid=self.request.auth.openid, supplier_name=data['goods_supplier'],
                                        is_delete=False).exists():
                if goods_unit.objects.filter(Q(openid=self.request.auth.openid, goods_unit=data['goods_unit'],
                                               is_delete=False) |
                                             Q(openid='init_data', goods_unit=data['goods_unit'],
                                               is_delete=False)).exists():
                    if goods_class.objects.filter(openid=self.request.auth.openid, goods_class=data['goods_class'],
                                                  is_delete=False).exists():
                        if goods_brand.objects.filter(openid=self.request.auth.openid, goods_brand=data['goods_brand'],
                                                      is_delete=False).exists():
                            if goods_color.objects.filter(Q(openid=self.request.auth.openid, goods_color=data['goods_color'],
                                                            is_delete=False) |
                                                          Q(openid='init_data', goods_color=data['goods_color'],
                                                            is_delete=False)).exists():
                                if goods_shape.objects.filter(Q(openid=self.request.auth.openid, goods_shape=data['goods_shape'],
                                                                is_delete=False) |
                                                              Q(openid='init_data', goods_shape=data['goods_shape'],
                                                                is_delete=False)).exists():
                                    if goods_specs.objects.filter(openid=self.request.auth.openid,
                                                                  goods_specs=data['goods_specs'],
                                                                  is_delete=False).exists():
                                        if goods_origin.objects.filter(openid=self.request.auth.openid,
                                                                       goods_origin=data['goods_origin'],
                                                                       is_delete=False).exists():
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
        if qs.openid != request.auth.openid:
            raise APIException({"detail": "Cannot delete data which not yours"})
        else:
            qs.is_delete = True
            qs.save()
            serializer = self.get_serializer(qs, many=False)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

class FileDownloadView(viewsets.ModelViewSet):
    queryset = ListModel.objects.all()
    serializer_class = serializers.FileRenderSerializer
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
                return self.queryset.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.FileRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def list(self, request, *args, **kwargs):
        from datetime import datetime
        dt = datetime.now()
        data = (
            FileRenderSerializer(instance).data
            for instance in self.get_queryset()
        )
        if self.request.GET.get('lang', '') == 'zh-hans':
            renderer = FileRenderCN().render(data)
        else:
            renderer = FileRenderEN().render(data)
        response = StreamingHttpResponse(
            renderer,
            content_type="text/csv"
        )
        response['Content-Disposition'] = "attachment; filename='goodslist_{}.csv'".format(str(dt.strftime('%Y%m%d%H%M%S%f')))
        return response
