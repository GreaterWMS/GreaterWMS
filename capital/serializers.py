from rest_framework import serializers
from .models import ListModel
from utils import datasolve

class CapitalGetSerializer(serializers.ModelSerializer):
    capital_name = serializers.CharField(read_only=True, required=False)
    capital_qty = serializers.IntegerField(read_only=True, required=False)
    capital_cost = serializers.FloatField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'openid', ]

class CapitalPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    capital_name = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    capital_qty = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.data_validate])
    capital_cost = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class CapitalUpdateSerializer(serializers.ModelSerializer):
    capital_name = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    capital_qty = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.data_validate])
    capital_cost = serializers.FloatField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class CapitalPartialUpdateSerializer(serializers.ModelSerializer):
    capital_name = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    capital_qty = serializers.IntegerField(read_only=False, required=False, validators=[datasolve.data_validate])
    capital_cost = serializers.FloatField(read_only=False, required=False, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class FileRenderSerializer(serializers.ModelSerializer):
    capital_name = serializers.CharField(read_only=False, required=False)
    capital_qty = serializers.IntegerField(read_only=False, required=False)
    capital_cost = serializers.FloatField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        ref_name = 'CapitalFileRenderSerializer'
        exclude = ['openid', 'is_delete', ]
