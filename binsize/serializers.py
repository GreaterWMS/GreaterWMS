from rest_framework import serializers
from .models import ListModel
from utils import datasolve

class BinsizeGetSerializer(serializers.ModelSerializer):
    bin_size = serializers.CharField(read_only=True, required=False)
    bin_size_w = serializers.FloatField(read_only=True, required=False)
    bin_size_d = serializers.FloatField(read_only=True, required=False)
    bin_size_h = serializers.FloatField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', ]

class BinsizePostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    bin_size = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    bin_size_w = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    bin_size_d = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    bin_size_h = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class BinsizeUpdateSerializer(serializers.ModelSerializer):
    bin_size = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    bin_size_w = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    bin_size_d = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    bin_size_h = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class BinsizePartialUpdateSerializer(serializers.ModelSerializer):
    bin_size = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    bin_size_w = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    bin_size_d = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    bin_size_h = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class FileRenderSerializer(serializers.ModelSerializer):
    bin_size = serializers.CharField(read_only=False, required=False)
    bin_size_w = serializers.FloatField(read_only=False, required=False)
    bin_size_d = serializers.FloatField(read_only=False, required=False)
    bin_size_h = serializers.FloatField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        ref_name = 'BinSizeFileRenderSerializer'
        exclude = ['openid', 'is_delete', ]
