from django.db.models import Q
from rest_framework import viewsets
from .models import ListModel
from . import serializers
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filter import Filter

class ChatViewSet(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_queryset(self):
        if self.request.user:
            sender = str(self.request.GET.get('sender', '')) + '-' + self.request.auth.openid
            receiver = str(self.request.GET.get('receiver', '')) + '-' + self.request.auth.openid
            if ListModel.objects.filter(sender=receiver, receiver=sender, read=False).exists():
                ListModel.objects.filter(sender=receiver, receiver=sender, read=False).update(read=True)
            return ListModel.objects.filter(Q(sender=sender, receiver=receiver) | Q(sender=receiver, receiver=sender))
        else:
            return ListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.ChatGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

class ReadAPI(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_queryset(self):
        if self.request.user:
            sender = str(self.request.GET.get('sender', '')) + '-' + self.request.auth.openid
            return ListModel.objects.filter(receiver=sender, read=False)
        else:
            return ListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.ChatGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)
