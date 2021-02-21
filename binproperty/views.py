from rest_framework import viewsets
from .models import ListModel
from . import serializers
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import Filter
from rest_framework.exceptions import APIException
from django.db.models import Q


class APIViewSet(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）
    """
    queryset = ListModel.objects.all()
    serializer_class = serializers.BinpropertyGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BinpropertyGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)
