from django.http import StreamingHttpResponse
from rest_framework import viewsets
from rest_framework.settings import api_settings
from .models import TransportationFeeListModel
from . import serializers
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import TransportationFeeListFilter
from rest_framework.exceptions import APIException
from .files import FreightfileRenderCN, FreightfileRenderEN

class TransportationFeeListViewSet(viewsets.ModelViewSet):
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
    queryset = TransportationFeeListModel.objects.all()
    serializer_class = serializers.FreightGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = TransportationFeeListFilter

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
            return serializers.FreightGetSerializer
        elif self.action == 'retrieve':
            return serializers.FreightGetSerializer
        elif self.action == 'create':
            return serializers.FreightPostSerializer
        elif self.action == 'update':
            return serializers.FreightUpdateSerializer
        elif self.action == 'partial_update':
            return serializers.FreightPartialUpdateSerializer
        elif self.action == 'destroy':
            return serializers.FreightGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        data['openid'] = self.request.auth.openid
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=200, headers=headers)

    def update(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot Update Data Which Not Yours"})
        else:
            data = self.request.data
            serializer = self.get_serializer(qs, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

    def partial_update(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot Partial Update Data Which Not Yours"})
        else:
            data = self.request.data
            serializer = self.get_serializer(qs, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

    def destroy(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot Delete Data Which Not Yours"})
        else:
            qs.is_delete = True
            qs.save()
            serializer = self.get_serializer(qs, many=False)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

class FreightfileDownloadView(viewsets.ModelViewSet):
    queryset = TransportationFeeListModel.objects.all()
    serializer_class = serializers.FreightfileRenderSerializer
    renderer_classes = (FreightfileRenderCN, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = TransportationFeeListFilter

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
            return serializers.FreightfileRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def list(self, request, *args, **kwargs):
        from datetime import datetime
        dt = datetime.now()
        data = (
            serializers.FreightfileRenderSerializer(instance).data
            for instance in self.filter_queryset(self.get_queryset())
        )
        if self.request.GET.get('lang', '') == 'zh-hans':
            renderer = FreightfileRenderCN().render(data)
        else:
            renderer = FreightfileRenderEN().render(data)
        response = StreamingHttpResponse(
            renderer,
            content_type="text/csv"
        )
        response['Content-Disposition'] = "attachment; filename='freight_{}.csv'".format(str(dt.strftime('%Y%m%d%H%M%S%f')))
        return response
