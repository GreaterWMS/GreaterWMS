from rest_framework import serializers

class ListSerializers(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    bin_size = serializers.CharField(read_only=True)
    bin_property = serializers.CharField(read_only=True)
    bin_empty = serializers.IntegerField(read_only=True)
    create_name = serializers.CharField(read_only=True)
    t_code = serializers.CharField(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    last_update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
