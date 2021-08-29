from rest_framework import serializers
from .models import CyclecountModeDayModel
from utils import datasolve

class CyclecountGetSerializer(serializers.ModelSerializer):
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d')
    class Meta:
        model = CyclecountModeDayModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', ]

class CyclecountPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = CyclecountModeDayModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class CyclecountUpdateSerializer(serializers.ModelSerializer):
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = CyclecountModeDayModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class CyclecountPartialUpdateSerializer(serializers.ModelSerializer):
    creater = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    class Meta:
        model = CyclecountModeDayModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class FileRenderSerializer(serializers.ModelSerializer):
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = CyclecountModeDayModel
        ref_name = 'CyclecountFileRenderSerializer'
        exclude = ['openid', 'is_delete', ]
