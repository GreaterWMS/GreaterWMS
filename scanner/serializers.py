from rest_framework import serializers
from .models import ListModel
from utils import datasolve

class ListGetSerializer(serializers.ModelSerializer):
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ListModel
        exclude = ['openid']
        read_only_fields = ['id', ]
