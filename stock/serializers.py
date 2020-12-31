from rest_framework import serializers
from .models import StockListModel, StockBinModel
from userprofile.serializers import Users
from rest_framework.exceptions import APIException
import re

def data_validate(data):
    script_obj = re.findall(r'script', str(data), re.IGNORECASE)
    select_obj = re.findall(r'select', str(data), re.IGNORECASE)
    if script_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    elif select_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    else:
        return data

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
    hold_stock = serializers.IntegerField(read_only=True, required=False)
    damage_stock = serializers.IntegerField(read_only=True, required=False)
    asn_stock = serializers.IntegerField(read_only=True, required=False)
    dn_stock = serializers.IntegerField(read_only=True, required=False)
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
    pick_qty = serializers.IntegerField(read_only=True, required=False)
    picked_qty = serializers.IntegerField(read_only=True, required=False)
    bin_size = serializers.CharField(read_only=True, required=False)
    bin_property = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = StockBinModel
        exclude = ['openid', ]
        read_only_fields = ['id', 'openid', 'create_time', 'update_time', ]

class StockBinPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[openid_validate])
    bin_name = serializers.CharField(read_only=True, required=False, validators=[data_validate])
    move_to_bin = serializers.CharField(read_only=True, required=False, validators=[data_validate])
    move_qty = serializers.CharField(read_only=True, required=False, validators=[data_validate])

    class Meta:
        model = StockBinModel
        exclude = []
        read_only_fields = ['id', 'openid', 'create_time', 'update_time', ]
