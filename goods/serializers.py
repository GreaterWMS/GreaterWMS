from rest_framework import serializers
from .models import ListModel
from userprofile.models import Users
import re
from rest_framework.exceptions import APIException

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

class GoodsGetSerializer(serializers.ModelSerializer):
    goods_code = serializers.CharField(read_only=True, required=False)
    goods_desc = serializers.CharField(read_only=True, required=False)
    goods_supplier = serializers.CharField(read_only=True, required=False)
    goods_weight = serializers.FloatField(read_only=True, required=False)
    goods_w = serializers.FloatField(read_only=True, required=False)
    goods_d = serializers.FloatField(read_only=True, required=False)
    goods_h = serializers.FloatField(read_only=True, required=False)
    unit_volume = serializers.FloatField(read_only=True, required=False)
    goods_unit = serializers.CharField(read_only=True, required=False)
    goods_class = serializers.CharField(read_only=True, required=False)
    goods_brand = serializers.CharField(read_only=True, required=False)
    goods_color = serializers.CharField(read_only=True, required=False)
    goods_shape = serializers.CharField(read_only=True, required=False)
    goods_specs = serializers.CharField(read_only=True, required=False)
    goods_origin = serializers.CharField(read_only=True, required=False)
    goods_cost = serializers.FloatField(read_only=True, required=False)
    goods_price = serializers.FloatField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]

class GoodsPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[openid_validate])
    goods_code = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_desc = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_supplier = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_weight = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    goods_w = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    goods_d = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    goods_h = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    unit_volume = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    goods_unit = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_class = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_brand = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_color = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_shape = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_specs = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_origin = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_cost = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    goods_price = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    creater = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class GoodsUpdateSerializer(serializers.ModelSerializer):
    goods_code = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_desc = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_supplier = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_weight = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    goods_w = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    goods_d = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    goods_h = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    unit_volume = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    goods_unit = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_class = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_brand = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_color = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_shape = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_specs = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_origin = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_cost = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    goods_price = serializers.FloatField(read_only=False,  required=True, validators=[data_validate])
    creater = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class GoodsPartialUpdateSerializer(serializers.ModelSerializer):
    goods_code = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_desc = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_supplier = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_weight = serializers.FloatField(read_only=False,  required=False, validators=[data_validate])
    goods_w = serializers.FloatField(read_only=False,  required=False, validators=[data_validate])
    goods_d = serializers.FloatField(read_only=False,  required=False, validators=[data_validate])
    goods_h = serializers.FloatField(read_only=False,  required=False, validators=[data_validate])
    unit_volume = serializers.FloatField(read_only=False,  required=False, validators=[data_validate])
    goods_unit = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_class = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_brand = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_color = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_shape = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_specs = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_origin = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_cost = serializers.FloatField(read_only=False,  required=False, validators=[data_validate])
    goods_price = serializers.FloatField(read_only=False,  required=False, validators=[data_validate])
    creater = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class FileRenderSerializer(serializers.ModelSerializer):
    goods_code = serializers.CharField(read_only=False, required=False)
    goods_desc = serializers.CharField(read_only=False, required=False)
    goods_supplier = serializers.CharField(read_only=False, required=False)
    goods_weight = serializers.FloatField(read_only=False, required=False)
    goods_w = serializers.FloatField(read_only=False, required=False)
    goods_d = serializers.FloatField(read_only=False, required=False)
    goods_h = serializers.FloatField(read_only=False, required=False)
    unit_volume = serializers.FloatField(read_only=False, required=False)
    goods_unit = serializers.CharField(read_only=False, required=False)
    goods_class = serializers.CharField(read_only=False, required=False)
    goods_brand = serializers.CharField(read_only=False, required=False)
    goods_color = serializers.CharField(read_only=False, required=False)
    goods_shape = serializers.CharField(read_only=False, required=False)
    goods_specs = serializers.CharField(read_only=False, required=False)
    goods_origin = serializers.CharField(read_only=False, required=False)
    goods_cost = serializers.FloatField(read_only=False, required=False)
    goods_price = serializers.FloatField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        ref_name = 'GOODSFileRenderSerializer'
        exclude = ['openid', 'is_delete', ]
