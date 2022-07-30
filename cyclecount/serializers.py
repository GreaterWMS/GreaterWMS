from rest_framework import serializers
from .models import CyclecountModeDayModel
from utils import datasolve
from .models import QTYRecorder
class CyclecountGetSerializer(serializers.ModelSerializer):
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = CyclecountModeDayModel
        exclude = ['openid']
        read_only_fields = ['id', ]

class CyclecountPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = CyclecountModeDayModel
        exclude = []
        read_only_fields = ['id', 'create_time', 'update_time', ]

class CyclecountUpdateSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = CyclecountModeDayModel
        exclude = []
        read_only_fields = ['id', 'create_time', 'update_time', ]

class FileRenderSerializer(serializers.ModelSerializer):
    creater = serializers.CharField(read_only=False, required=False)
    physical_inventory = serializers.SerializerMethodField()
    difference = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = CyclecountModeDayModel
        ref_name = 'CyclecountFileRenderSerializer'
        exclude = ['openid']

    def get_physical_inventory(self, obj):
        return ''

    def get_difference(self, obj):
        return ''

class FileRenderAllSerializer(serializers.ModelSerializer):
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = CyclecountModeDayModel
        ref_name = 'CyclecountFileRenderAllSerializer'
        exclude = ['openid']


class QTYRecorderSerializer(serializers.ModelSerializer):
    mode_code = serializers.CharField(read_only=True, required=False)
    bin_name = serializers.CharField(read_only=True, required=False)
    goods_code = serializers.CharField(read_only=True, required=False)
    goods_desc = serializers.CharField(read_only=True, required=False)
    goods_qty = serializers.IntegerField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = QTYRecorder
        ref_name = 'QTYRecorderSerializer'
        exclude = ['openid']