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

class ChatGetSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(read_only=True, required=False)
    receiver = serializers.CharField(read_only=True, required=False)
    read = serializers.BooleanField(read_only=True, required=False)
    detail = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', ]
