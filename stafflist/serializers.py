from rest_framework import serializers

class ListSerializers(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    nickname = serializers.CharField(read_only=True)
    create_name = serializers.CharField(read_only=True)
    developer = serializers.IntegerField(read_only=True)
    auth_name = serializers.CharField(read_only=True)
    transaction_code = serializers.CharField(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    last_update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
