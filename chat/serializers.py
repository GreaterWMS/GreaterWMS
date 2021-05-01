from rest_framework import serializers
from .models import ListModel

class ChatGetSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(read_only=True, required=False)
    receiver = serializers.CharField(read_only=True, required=False)
    read = serializers.BooleanField(read_only=True, required=False)
    detail = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', ]
