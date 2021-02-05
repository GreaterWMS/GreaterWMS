from rest_framework import serializers
from .models import TransportationFeeListModel
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

class PaymentGetSerializer(serializers.ModelSerializer):
    send_city = serializers.CharField(read_only=True, required=False)
    receiver_city = serializers.CharField(read_only=True, required=False)
    weight_fee = serializers.FloatField(read_only=True, required=False)
    volume_fee = serializers.FloatField(read_only=True, required=False)
    transportation_supplier = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = TransportationFeeListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', ]

class PaymentPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[openid_validate])
    send_city = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    receiver_city = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    weight_fee = serializers.FloatField(read_only=False, required=True, validators=[data_validate])
    volume_fee = serializers.FloatField(read_only=False, required=True, validators=[data_validate])
    transportation_supplier = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    class Meta:
        model = TransportationFeeListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class PaymentUpdateSerializer(serializers.ModelSerializer):
    send_city = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    receiver_city = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    weight_fee = serializers.FloatField(read_only=False, required=True, validators=[data_validate])
    volume_fee = serializers.FloatField(read_only=False, required=True, validators=[data_validate])
    transportation_supplier = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    class Meta:
        model = TransportationFeeListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class PaymentPartialUpdateSerializer(serializers.ModelSerializer):
    send_city = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    receiver_city = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    weight_fee = serializers.FloatField(read_only=False, required=False, validators=[data_validate])
    volume_fee = serializers.FloatField(read_only=False, required=False, validators=[data_validate])
    transportation_supplier = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    class Meta:
        model = TransportationFeeListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]
