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

class FileRenderSerializer(serializers.ModelSerializer):
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = CyclecountModeDayModel
        ref_name = 'CyclecountFileRenderSerializer'
        exclude = ['openid']


class QTYRecorderSerializer(serializers.ModelSerializer):
    # openid = serializers.CharField(read_only=True,required=False)
    mode_code = serializers.CharField(read_only=True,required=False)
    bin_name = serializers.CharField(read_only=True,required=False)
    goods_code = serializers.CharField(read_only=True,required=False)
    goods_qty = serializers.CharField(read_only=True,required=False)
    creater = serializers.CharField(read_only=True,required=False)
    crete_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = QTYRecorder
        exclude = ['openid']