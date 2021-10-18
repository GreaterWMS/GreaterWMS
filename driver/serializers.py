from rest_framework import serializers
from .models import ListModel, DispatchListModel
from utils import datasolve

class DriverGetSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(read_only=True, required=False)
    license_plate = serializers.CharField(read_only=True, required=False)
    contact = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', ]

class DriverPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    driver_name = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    contact = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    license_plate = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class DriverUpdateSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    license_plate = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    contact = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class DriverPartialUpdateSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    license_plate = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    contact = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class DispatchListGetSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(read_only=True, required=False)
    dn_code = serializers.CharField(read_only=True, required=False)
    contact = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = DispatchListModel
        exclude = ['openid', ]
        read_only_fields = ['id', ]

class FileRenderSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(read_only=False, required=False)
    license_palate = serializers.IntegerField(read_only=False, required=False)
    contact = serializers.CharField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        ref_name = 'DriverFileRenderSerializer'
        exclude = ['openid', 'is_delete', ]

