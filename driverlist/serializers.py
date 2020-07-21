from rest_framework import serializers

class ListSerializers(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    plate_license = serializers.CharField(read_only=True)
    mobile = serializers.IntegerField(read_only=True)
    identity_card = serializers.CharField(read_only=True)
    driver_license = serializers.CharField(read_only=True)
    vehicle_license = serializers.CharField(read_only=True)
    create_name = serializers.CharField(read_only=True)
    t_code = serializers.CharField(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    last_update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
