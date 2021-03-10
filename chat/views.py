from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q
from rest_framework import viewsets
from .models import ListModel
from . import serializers
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filter import Filter

@method_decorator(csrf_exempt, name='dispatch')
class APIViewSet(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）
    """
    queryset = ListModel.objects.all()
    serializer_class = serializers.ChatGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_queryset(self):
        if self.request.user:
            sender = str(self.request.GET.get('sender', '')) + '-' + self.request.auth.openid
            receiver = str(self.request.GET.get('receiver', '')) + '-' + self.request.auth.openid
            if self.queryset.filter(sender=receiver, receiver=sender, read=False).exists():
                self.queryset.filter(sender=receiver, receiver=sender, read=False).update(read=True)
            return self.queryset.filter(Q(sender=sender, receiver=receiver) | Q(sender=receiver, receiver=sender))
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ChatGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

@method_decorator(csrf_exempt, name='dispatch')
class ReadAPI(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）
    """
    queryset = ListModel.objects.all()
    serializer_class = serializers.ChatGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_queryset(self):
        if self.request.user:
            sender = str(self.request.GET.get('sender', '')) + '-' + self.request.auth.openid
            return self.queryset.filter(receiver=sender, read=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ChatGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)
