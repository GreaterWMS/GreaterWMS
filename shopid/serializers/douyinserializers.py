from rest_framework import serializers
from shopid.models.douyinmodels import ListModel

class DouYinGetSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(read_only=True, required=False)
    shop_mode = serializers.CharField(read_only=True, required=False)
    shop_appid = serializers.CharField(read_only=True, required=False)
    shop_app_secret = serializers.CharField(read_only=True, required=False)
    shop_id = serializers.CharField(read_only=True, required=False)
    sandbox = serializers.IntegerField(read_only=True, required=False)
    proxy = serializers.IntegerField(read_only=True, required=False)
    proxy_ip = serializers.JSONField(read_only=True, required=False)
    t_code = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['openid', 'appid', ]
        read_only_fields = ['id']

class DouYinfileRenderSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(read_only=True, required=False)
    shop_mode = serializers.CharField(read_only=True, required=False)
    shop_appid = serializers.CharField(read_only=True, required=False)
    shop_app_secret = serializers.CharField(read_only=True, required=False)
    shop_id = serializers.CharField(read_only=True, required=False)
    sandbox = serializers.IntegerField(read_only=True, required=False)
    proxy = serializers.IntegerField(read_only=True, required=False)
    proxy_ip = serializers.JSONField(read_only=True, required=False)
    t_code = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['openid', 'appid', ]
        read_only_fields = ['id']
