from rest_framework import serializers
from .models import DnListModel, DnDetailModel, PickingListModel
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

def dn_data_validate(data):
    script_obj = re.findall(r'script', str(data), re.IGNORECASE)
    select_obj = re.findall(r'select', str(data), re.IGNORECASE)
    if script_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    elif select_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    else:
        dn_last_code = re.findall(r'\d+', str(data), re.IGNORECASE)
        if str(dn_last_code[0]) == '00000001':
            data = 'DN' + '00000001'
        else:
            data = 'DN' + str(int(dn_last_code[0]) + 1).zfill(8)
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
class DNListGetSerializer(serializers.ModelSerializer):
    dn_code = serializers.CharField(read_only=True, required=False)
    dn_status = serializers.IntegerField(read_only=True, required=False)
    customer = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = DnListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', ]

class DNListPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[openid_validate])
    dn_code = serializers.CharField(read_only=False,  required=True, validators=[dn_data_validate])
    customer = serializers.CharField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    class Meta:
        model = DnListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class DNListPartialUpdateSerializer(serializers.ModelSerializer):
    dn_code = serializers.CharField(read_only=False,  required=True, validators=[dn_data_validate])

    class Meta:
        model = DnListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class DNListUpdateSerializer(serializers.ModelSerializer):
    dn_code = serializers.CharField(read_only=False,  required=True, validators=[dn_data_validate])

    class Meta:
        model = DnListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class DNDetailGetSerializer(serializers.ModelSerializer):
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
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    back_order_label = serializers.BooleanField(read_only=True, required=False)
    class Meta:
        model = DnDetailModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'openid']

class DNDetailPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[openid_validate])
    dn_code = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    customer = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_code = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    goods_qty = serializers.IntegerField(read_only=False, required=True, validators=[data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    class Meta:
        model = DnDetailModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class DNDetailUpdateSerializer(serializers.ModelSerializer):
    dn_code = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    customer = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    goods_code = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    goods_qty = serializers.IntegerField(read_only=False, required=True, validators=[data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    class Meta:
        model = DnDetailModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class DNDetailPartialUpdateSerializer(serializers.ModelSerializer):
    dn_code = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    customer = serializers.CharField(read_only=False,  required=False, validators=[data_validate])
    goods_code = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    goods_qty = serializers.IntegerField(read_only=False, required=False, validators=[data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    class Meta:
        model = DnDetailModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class DNPickingListGetSerializer(serializers.ModelSerializer):
    dn_code = serializers.CharField(read_only=True, required=False)
    bin_name = serializers.CharField(read_only=True, required=False)
    goods_code = serializers.CharField(read_only=True, required=False)
    pick_qty = serializers.IntegerField(read_only=True, required=False)
    picked_qty = serializers.IntegerField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = PickingListModel
        exclude = ['openid', ]
        read_only_fields = ['id', ]

class DNPickingCheckGetSerializer(serializers.ModelSerializer):
    dn_code = serializers.CharField(read_only=True, required=False)
    bin_name = serializers.CharField(read_only=True, required=False)
    goods_code = serializers.CharField(read_only=True, required=False)
    pick_qty = serializers.IntegerField(read_only=True, required=False)
    picked_qty = serializers.IntegerField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = PickingListModel
        exclude = ['openid', ]
        read_only_fields = ['id', ]

class FileListRenderSerializer(serializers.ModelSerializer):
    dn_code = serializers.CharField(read_only=False, required=False)
    dn_status = serializers.IntegerField(read_only=False, required=False)
    total_weight = serializers.FloatField(read_only=False, required=False)
    total_volume = serializers.FloatField(read_only=False, required=False)
    customer = serializers.CharField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    back_order_label = serializers.BooleanField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = DnListModel
        ref_name = 'DNFileListRenderSerializer'
        exclude = ['openid', 'is_delete', ]

class FileDetailRenderSerializer(serializers.ModelSerializer):
    dn_code = serializers.CharField(read_only=False, required=False)
    dn_status = serializers.IntegerField(read_only=False, required=False)
    customer = serializers.CharField(read_only=False, required=False)
    goods_code = serializers.CharField(read_only=False, required=False)
    goods_qty = serializers.IntegerField(read_only=False, required=False)
    pick_qty = serializers.IntegerField(read_only=False, required=False)
    picked_qty = serializers.IntegerField(read_only=False, required=False)
    intransit_qty = serializers.IntegerField(read_only=False, required=False)
    delivery_actual_qty = serializers.IntegerField(read_only=False, required=False)
    delivery_shortage_qty = serializers.IntegerField(read_only=False, required=False)
    delivery_more_qty = serializers.IntegerField(read_only=False, required=False)
    delivery_damage_qty = serializers.IntegerField(read_only=False, required=False)
    goods_weight = serializers.FloatField(read_only=False, required=False)
    goods_volume = serializers.FloatField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    back_order_label = serializers.BooleanField(read_only=False, required=False)

    class Meta:
        model = DnDetailModel
        ref_name = 'DNFileDetailRenderSerializer'
        exclude = ['openid', 'is_delete', ]
