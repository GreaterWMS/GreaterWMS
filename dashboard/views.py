from rest_framework import viewsets
from asn.models import AsnDetailModel
from asn import serializers
from utils.page import MyPageNumberPagination
from utils.datasolve import sumOfList
from utils.fbmsg import FBMsg
from utils.md5 import Md5
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from asn.filter import AsnDetailFilter
from rest_framework.exceptions import APIException
from django.shortcuts import render
from dateutil.relativedelta import relativedelta
from django.db.models.functions import TruncMonth,TruncYear,ExtractDay,ExtractMonth
from django.db.models import Count
from django.db import connection
from django.db.models import Q
from django.db.models import Sum
import re
from django.utils import timezone

class ReceiptsViewSet(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）
    """
    pagination_class = []
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = AsnDetailFilter

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
                return AsnDetailModel.objects.filter(openid=self.request.auth.openid, asn_status__gte=4,
                                                     create_time__gte=timezone.now().date() - timezone.timedelta(days=14),
                                                     is_delete=False)
            else:
                return AsnDetailModel.objects.filter(openid=self.request.auth.openid, asn_status__gte=4,
                                                     create_time__gte=timezone.now().date() - timezone.timedelta(days=14),
                                                     id=id, is_delete=False)
        else:
            return AsnDetailModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.ASNDetailGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def notice_lang(self):
        lang = self.request.META.get('HTTP_LANGUAGE')
        if lang == 'zh-hans':
            return {
                "receipts": "总收货量",
                "qty": "收货数量排名",
                "cost": "收货额排名"
            }
        if lang == 'zh-hant':
            return {
                "receipts": "縂收貨數",
                "qty": "收貨數量排名",
                "cost": "收貨額排名"
            }
        if lang == 'en-us':
            return {
                "receipts": "Total Receipts",
                "qty": "Receiving Quantity Ranking",
                "cost": "Receiving Amount Ranking"
            }
        if lang == 'ja':
            return {
                "receipts": "総受入量",
                "qty": "受入数量ランキング",
                "cost": "受入額ランキング"
            }

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        data_list = []
        print(self.notice_lang())
        receipt_res = qs.annotate(month=ExtractMonth('create_time'), day=ExtractDay('create_time')) \
            .values('month', 'day').order_by('month', 'day').annotate(number=Sum('goods_cost'))
        qty_res = qs.values('goods_code').order_by('goods_code').annotate(number=Sum('goods_qty'))
        rank_res = qs.values('goods_code').order_by('goods_code').annotate(number=Sum('goods_cost'))
        receipt_res_dict = {
            "product": self.notice_lang()['receipts']
        }
        qty_res_dict = {
            "product": self.notice_lang()['qty']
        }
        rank_res_dict = {
            "product": self.notice_lang()['cost']
        }
        for i in receipt_res:
            receipt_res_dict.update({"%s-%s" % (i['month'], i['day']): i['number']})
        for i in qty_res:
            qty_res_dict.update({i['goods_code']: i['number']})
        for i in rank_res:
            rank_res_dict.update({i['goods_code']: i['number']})
        data_list.append(receipt_res_dict)
        data_list.append(qty_res_dict)
        data_list.append(rank_res_dict)
        print(data_list)
        return Response(data_list)
