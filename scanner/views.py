from dateutil.relativedelta import relativedelta
from django.http import StreamingHttpResponse
from django.utils import timezone
from .models import ListModel
from rest_framework import viewsets
from . import serializers
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filter import Filter
from rest_framework.generics import RetrieveAPIView,GenericAPIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from stock.models import StockBinModel
from dn.models import DnDetailModel
from dn.filter import DnDetailFilter

class SannerDnDetailPickingListView(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = DnDetailFilter


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
                return DnDetailModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return DnDetailModel.objects.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return DnDetailModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'destroy']:
            return serializers.SannerDnDetailPickingListGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

class ListViewSet(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）
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
                return ListModel.objects.filter(openid=self.request.auth.openid)
            else:
                return ListModel.objects.filter(openid=self.request.auth.openid, id=id)
        else:
            return ListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.ListGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)



class SannerView(viewsets.ModelViewSet):
    """
        Retrieve:
            Response a data retrieve
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
            if id is None:
                return ListModel.objects.filter(openid=self.request.auth.openid)
            else:
                return ListModel.objects.filter(openid=self.request.auth.openid, bar_code=bar_code)
        else:
            return ListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return serializers.ListGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)