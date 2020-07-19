from rest_framework import serializers

class ListSerializers(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    province = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    district = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    manager = serializers.CharField(read_only=True)
    mobile = serializers.CharField(read_only=True)
    customer_lv = serializers.IntegerField(read_only=True)
    t_code = serializers.CharField(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    last_update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
