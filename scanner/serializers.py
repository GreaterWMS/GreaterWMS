from rest_framework import serializers
from .models import ListModel
from utils import datasolve
from dn.models import DnDetailModel
import time
from stock.models import StockBinModel


class ListGetSerializer(serializers.ModelSerializer):
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    request_time = serializers.SerializerMethodField()

    class Meta:
        model = ListModel
        exclude = ['openid']
        read_only_fields = ['id', ]

    def get_request_time(self, obj):
        return time.time()


class SannerDnDetailPickingListGetSerializer(serializers.ModelSerializer):
    dn_code = serializers.CharField(read_only=True, required=False)
    dn_status = serializers.IntegerField(read_only=True, required=False)
    customer = serializers.CharField(read_only=True, required=False)
    goods_code = serializers.CharField(read_only=True, required=False)
    goods_qty = serializers.IntegerField(read_only=True, required=False)
    pick_qty = serializers.IntegerField(read_only=True, required=False)
    picked_qty = serializers.IntegerField(read_only=True, required=False)
    intransit_qty = serializers.IntegerField(read_only=True, required=False)
    delivery_actual_qty = serializers.IntegerField(read_only=True, required=False)
    delivery_shortage_qty = serializers.IntegerField(read_only=True, required=False)
    delivery_more_qty = serializers.IntegerField(read_only=True, required=False)
    delivery_damage_qty = serializers.IntegerField(read_only=True, required=False)
    goods_weight = serializers.FloatField(read_only=True, required=False)
    goods_volume = serializers.FloatField(read_only=True, required=False)
    goods_cost = serializers.FloatField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    back_order_label = serializers.BooleanField(read_only=True, required=False)

    class Meta:
        model = DnDetailModel
        fields=['dn_code','dn_status','customer','goods_code','goods_qty','goods_qty','pick_qty','picked_qty','intransit_qty','delivery_actual_qty','delivery_shortage_qty','delivery_more_qty','delivery_damage_qty','goods_weight','goods_volume','goods_cost','creater','create_time','update_time','back_order_label']
        read_only_fields = ['id', 'openid']



