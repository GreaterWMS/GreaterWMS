from rest_framework import serializers
from goods.models import ListModel as goodslist
from utils import datasolve

class GoodslistSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    supplier_name = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    supplier_city = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    supplier_address = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_contact = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_manager = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier_level = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = goodslist
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]
