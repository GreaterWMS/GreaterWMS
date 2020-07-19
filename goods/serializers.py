from rest_framework import serializers

class ListSerializers(serializers.Serializer):
    goods_code = serializers.CharField(read_only=True)
    on_hand_stock = serializers.IntegerField(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
