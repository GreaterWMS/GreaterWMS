from rest_framework import serializers
from .models import ListModel
from utils import datasolve


class WarehouseGetSerializer(serializers.ModelSerializer):
    warehouse_name = serializers.CharField(read_only=True, required=False)
    warehouse_city = serializers.CharField(read_only=True, required=False)
    warehouse_address = serializers.CharField(read_only=True, required=False)
    warehouse_contact = serializers.CharField(read_only=True, required=False)
    warehouse_manager = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', ]


class WarehousePostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    warehouse_name = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate],
                                           max_length=45, min_length=1)
    warehouse_city = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    warehouse_address = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    warehouse_contact = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    warehouse_manager = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])

    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]


class WarehouseUpdateSerializer(serializers.ModelSerializer):
    warehouse_name = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate],
                                           max_length=45, min_length=1)
    warehouse_city = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    warehouse_address = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    warehouse_contact = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    warehouse_manager = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])

    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]


class WarehousePartialUpdateSerializer(serializers.ModelSerializer):
    warehouse_name = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate],
                                           max_length=45, min_length=1)
    warehouse_city = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    warehouse_address = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    warehouse_contact = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    warehouse_manager = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])

    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]
