from rest_framework import serializers

class ListSerializers(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    so_status = serializers.IntegerField(read_only=True)
    customer = serializers.CharField(read_only=True)
    create_name = serializers.CharField(read_only=True)
    t_code = serializers.CharField(read_only=True)
    is_delete = serializers.IntegerField(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    last_update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

class GoodsListSerializers(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    goods_name = serializers.CharField(read_only=True)

class CustomerListSerializers(serializers.Serializer):
    name = serializers.CharField(read_only=True)
