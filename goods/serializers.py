from rest_framework import serializers
from .models import ListModel
from utils import datasolve
from rest_framework.exceptions import ValidationError

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
    bar_code = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id']


class GoodsPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    goods_code = serializers.CharField(read_only=False, required=True, min_length=1,
                                       validators=[datasolve.data_validate])
    goods_desc = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_supplier = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_weight = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_w = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_d = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_h = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    unit_volume = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_unit = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_class = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_brand = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_color = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_shape = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_specs = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_origin = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_cost = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_price = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    bar_code = serializers.CharField(read_only=False, required=True)

    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]





class GoodsUpdateSerializer(serializers.ModelSerializer):
    goods_code = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate],
                                       min_length=1)
    goods_desc = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_supplier = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_weight = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_w = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_d = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_h = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    unit_volume = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_unit = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_class = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_brand = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_color = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_shape = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_specs = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_origin = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_cost = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_price = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    bar_code = serializers.CharField(read_only=False, required=False)

    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class GoodsPartialUpdateSerializer(serializers.ModelSerializer):
    goods_code = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate],
                                       min_length=1)
    goods_desc = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_supplier = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_weight = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_w = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_d = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_h = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    unit_volume = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_unit = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_class = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_brand = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_color = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_shape = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_specs = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_origin = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_cost = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_price = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    bar_code = serializers.CharField(read_only=False, required=False)


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
