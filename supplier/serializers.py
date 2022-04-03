from rest_framework import serializers
from .models import ListModel
from utils import datasolve

class SupplierGetSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(read_only=True, required=False)
    supplier_city = serializers.CharField(read_only=True, required=False)
    supplier_address = serializers.CharField(read_only=True, required=False)
    supplier_contact = serializers.CharField(read_only=True, required=False)
    supplier_manager = serializers.CharField(read_only=True, required=False)
    supplier_level = serializers.IntegerField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'openid', 'create_time', 'update_time', ]

class SupplierPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    supplier_name = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    supplier_city = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    supplier_address = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_contact = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_manager = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_level = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class SupplierUpdateSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_city = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_address = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_contact = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_manager = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_level = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class SupplierPartialUpdateSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    supplier_city = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    supplier_address = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    supplier_contact = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    supplier_manager = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    supplier_level = serializers.IntegerField(read_only=False, required=False, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class FileRenderSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(read_only=False, required=False)
    supplier_city = serializers.CharField(read_only=False, required=False)
    supplier_address = serializers.CharField(read_only=False, required=False)
    supplier_contact = serializers.CharField(read_only=False, required=False)
    supplier_manager = serializers.CharField(read_only=False, required=False)
    supplier_level = serializers.IntegerField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        ref_name = 'SupplierFileRenderSerializer'
        exclude = ['openid', 'is_delete', ]
