from rest_framework import serializers
from .models import StockListModel, StockBinModel
from userprofile.serializers import Users
from rest_framework.exceptions import APIException

def openid_validate(data):
    if Users.objects.filter(openid=data).exists():
        return data
    else:
        raise APIException({'detail': 'User does not exists'})

def appid_validate(data):
    if Users.objects.filter(appid=data).exists():
        return data
    else:
        raise APIException({'detail': 'User does not exists'})

class StockListGetSerializer(serializers.ModelSerializer):
    api_name = serializers.CharField(read_only=True, required=False)
    goods_code = serializers.CharField(read_only=True, required=False)
    goods_desc = serializers.CharField(read_only=True, required=False)
    goods_qty = serializers.IntegerField(read_only=True, required=False)
    onhand_stock = serializers.IntegerField(read_only=True, required=False)
    can_order_stock = serializers.IntegerField(read_only=True, required=False)
    inspect_stock = serializers.IntegerField(read_only=True, required=False)
    cross_dock_stock = serializers.IntegerField(read_only=True, required=False)
    hold_stock = serializers.IntegerField(read_only=True, required=False)
    damage_stock = serializers.IntegerField(read_only=True, required=False)
    asn_stock = serializers.IntegerField(read_only=True, required=False)
    pre_load_stock = serializers.IntegerField(read_only=True, required=False)
    pre_sort_stock = serializers.IntegerField(read_only=True, required=False)
    sorted_stock = serializers.IntegerField(read_only=True, required=False)
    pick_stock = serializers.IntegerField(read_only=True, required=False)
    picked_stock = serializers.IntegerField(read_only=True, required=False)
    back_order_stock = serializers.IntegerField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = StockListModel
        exclude = ['openid', ]
        read_only_fields = ['id', 'openid', 'create_time', 'update_time', ]

class StockBinGetSerializer(serializers.ModelSerializer):
    bin_name = serializers.CharField(read_only=True, required=False)
    goods_code = serializers.CharField(read_only=True, required=False)
    goods_desc = serializers.CharField(read_only=True, required=False)
    goods_qty = serializers.IntegerField(read_only=True, required=False)
    bin_size = serializers.CharField(read_only=True, required=False)
    bin_property = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = StockBinModel
        exclude = ['openid', ]
        read_only_fields = ['id', 'openid', 'create_time', 'update_time', ]
