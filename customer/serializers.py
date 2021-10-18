from rest_framework import serializers
from .models import ListModel
from utils import datasolve

class CustomerGetSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(read_only=True, required=False)
    customer_city = serializers.CharField(read_only=True, required=False)
    customer_address = serializers.CharField(read_only=True, required=False)
    customer_contact = serializers.CharField(read_only=True, required=False)
    customer_manager = serializers.CharField(read_only=True, required=False)
    customer_level = serializers.IntegerField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', ]

class CustomerPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    customer_name = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    customer_city = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    customer_address = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    customer_contact = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    customer_manager = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    customer_level = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class CustomerUpdateSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    customer_city = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    customer_address = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    customer_contact = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    customer_manager = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    customer_level = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class CustomerPartialUpdateSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    customer_city = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    customer_address = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    customer_contact = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    customer_manager = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    customer_level = serializers.IntegerField(read_only=False, required=False, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class FileRenderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(read_only=False, required=False)
    customer_city = serializers.CharField(read_only=False, required=False)
    customer_address = serializers.CharField(read_only=False, required=False)
    customer_contact = serializers.CharField(read_only=False, required=False)
    customer_manager = serializers.CharField(read_only=False, required=False)
    customer_level = serializers.IntegerField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        ref_name = 'CustomereFileRenderSerializer'
        exclude = ['openid', 'is_delete', ]
