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

class CustomerGetSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(read_only=True, required=False)
    customer_city = serializers.CharField(read_only=True, required=False)
    customer_address = serializers.CharField(read_only=True, required=False)
    customer_contact = serializers.IntegerField(read_only=True, required=False)
    customer_manager = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'openid', 'create_time', 'update_time', ]

class CustomerPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[openid_validate])
    customer_name = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    customer_city = serializers.CharField(read_only=False,  required=True, validators=[data_validate])
    customer_address = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    customer_contact = serializers.IntegerField(read_only=False, required=True, validators=[data_validate])
    customer_manager = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class CustomerUpdateSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    customer_city = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    customer_address = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    customer_contact = serializers.IntegerField(read_only=False, required=True, validators=[data_validate])
    customer_manager = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class CustomerPartialUpdateSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    customer_city = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    customer_address = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    customer_contact = serializers.IntegerField(read_only=False, required=False, validators=[data_validate])
    customer_manager = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class FileRenderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    customer_city = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    customer_address = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    customer_contact = serializers.IntegerField(read_only=False, required=False, validators=[data_validate])
    customer_manager = serializers.CharField(read_only=False, required=False, validators=[data_validate])
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', 'creater', ]
