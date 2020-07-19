from rest_framework import serializers

class ListSerializers(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    po_status = serializers.IntegerField(read_only=True)
    goods_code = serializers.CharField(read_only=True)
    goods_name = serializers.CharField(read_only=True)
    po_qty = serializers.IntegerField(read_only=True)
    arrive_qty = serializers.IntegerField(read_only=True)
    actual_qty = serializers.IntegerField(read_only=True)
    actual_up_qty = serializers.IntegerField(read_only=True)
    shortage_qty = serializers.IntegerField(read_only=True)
    more_qty = serializers.IntegerField(read_only=True)
    damage_qty = serializers.IntegerField(read_only=True)
    damage_up_qty = serializers.IntegerField(read_only=True)
    up_qty = serializers.IntegerField(read_only=True)
    supplier = serializers.CharField(read_only=True)
    create_name = serializers.CharField(read_only=True)
    t_code = serializers.CharField(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    last_update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

class BinListSerializers(serializers.Serializer):
    name = serializers.CharField(read_only=True)
