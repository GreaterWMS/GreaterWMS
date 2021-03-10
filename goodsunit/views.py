from rest_framework import viewsets
from .models import ListModel
from . import serializers
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import Filter
from rest_framework.exceptions import APIException

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
    serializer_class = serializers.GoodsunitGetSerializer
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
            return serializers.GoodsunitGetSerializer
        elif self.action == 'retrieve':
            return serializers.GoodsunitGetSerializer
        elif self.action == 'create':
            return serializers.GoodsunitPostSerializer
        elif self.action == 'update':
            return serializers.GoodsunitUpdateSerializer
        elif self.action == 'partial_update':
            return serializers.GoodsunitPartialUpdateSerializer
        elif self.action == 'destroy':
            return serializers.GoodsunitGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['openid'] = request.auth.openid
        if self.queryset.filter(openid=data['openid'], goods_unit=data['goods_unit'], is_delete=False).exists():
            raise APIException({"detail": "Data exists"})
        else:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

    def update(self, request, pk):
        qs = self.get_object()
        if qs.openid != 'init_data':
            if qs.openid != request.auth.openid:
                raise APIException({"detail": "Cannot update data which not yours"})
            else:
                data = request.data
                serializer = self.get_serializer(qs, data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=200, headers=headers)
        else:
            data = request.data
            serializer = self.get_serializer(qs, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

    def partial_update(self, request, pk):
        qs = self.get_object()
        if qs.openid != 'init_data':
            if qs.openid != request.auth.openid:
                raise APIException({"detail": "Cannot partial_update data which not yours"})
            else:
                data = request.data
                serializer = self.get_serializer(qs, data=data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=200, headers=headers)
        else:
            data = request.data
            serializer = self.get_serializer(qs, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

    def destroy(self, request, pk):
        qs = self.get_object()
        if qs.openid != 'init_data':
            if qs.openid != request.auth.openid:
                raise APIException({"detail": "Cannot delete data which not yours"})
            else:
                qs.is_delete = True
                qs.save()
                serializer = self.get_serializer(qs, many=False)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=200, headers=headers)
        else:
            qs.is_delete = True
            qs.save()
            serializer = self.get_serializer(qs, many=False)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)
