from rest_framework import viewsets
from .models import StockListModel, StockBinModel
from . import serializers
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import StockListFilter, StockBinFilter
from rest_framework.exceptions import APIException

class StockListViewSet(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）
    """
    queryset = StockListModel.objects.all()
    serializer_class = serializers.StockListGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = StockListFilter

    def get_queryset(self):
        if self.request.user:
            return self.queryset.filter(openid=self.request.auth.openid)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.StockListGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

class StockBinViewSet(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）
    """
    queryset = StockBinModel.objects.all()
    serializer_class = serializers.StockBinGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = StockBinFilter

    def get_queryset(self):
        if self.request.user:
            return self.queryset.filter(openid=self.request.auth.openid)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.StockBinGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)
