from rest_framework import serializers

class StockAnalystSerializers(serializers.Serializer):
    goods_code = serializers.CharField(read_only=True)
    shipping_qty = serializers.IntegerField(read_only=True)
    shipping_time = serializers.DateField(read_only=True, format='%Y-%m-%d')
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
