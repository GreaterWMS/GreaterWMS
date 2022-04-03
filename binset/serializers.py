from rest_framework import serializers
from .models import ListModel
from utils import datasolve

class ScannerBinsetTagGetSerializer(serializers.ModelSerializer):
    bin_name = serializers.CharField(read_only=True, required=False)
    bin_size = serializers.CharField(read_only=True, required=False)
    bin_property = serializers.CharField(read_only=True, required=False)
    empty_label = serializers.BooleanField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    bar_code = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', ]


class BinsetGetSerializer(serializers.ModelSerializer):
    bin_name = serializers.CharField(read_only=True, required=False)
    bin_size = serializers.CharField(read_only=True, required=False)
    bin_property = serializers.CharField(read_only=True, required=False)
    empty_label = serializers.BooleanField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    bar_code = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', ]

class BinsetPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    bin_name = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    bin_size = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    bin_property = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    bar_code = serializers.CharField(read_only=False, required=True)
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class BinsetUpdateSerializer(serializers.ModelSerializer):
    bin_name = serializers.CharField(read_only=True, required=False)
    bin_size = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    bin_property = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    bar_code = serializers.CharField(read_only=False, required=False)
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

class FileRenderSerializer(serializers.ModelSerializer):
    bin_name = serializers.CharField(read_only=False, required=False)
    bin_size = serializers.CharField(read_only=False, required=False)
    bin_property = serializers.CharField(read_only=False, required=False)
    empty_label = serializers.BooleanField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        ref_name = 'BinSetFileRenderSerializer'
        exclude = ['openid', 'is_delete', ]
