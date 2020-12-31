from rest_framework import serializers
from .models import ListModel
from utils import datasolve

class BinsetGetSerializer(serializers.ModelSerializer):
    bin_name = serializers.CharField(read_only=True, required=False)
    bin_size = serializers.CharField(read_only=True, required=False)
    bin_property = serializers.CharField(read_only=True, required=False)
    empty_label = serializers.BooleanField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'openid', 'create_time', 'update_time', ]

class BinsetPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    bin_name = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    bin_size = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    bin_property = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class BinsetUpdateSerializer(serializers.ModelSerializer):
    bin_name = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    bin_size = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    bin_property = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class BinsetPartialUpdateSerializer(serializers.ModelSerializer):
    bin_name = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    bin_size = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    bin_property = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]
