from rest_framework import serializers
from goodslist import models

class UserCheckRule(object):
    def __call__(self, value):
        data = value.split("\"")
        if models.GoodsUnit.objects.filter(transaction_code=data[0], is_delete=0).exists():
            unit_token = models.GoodsUnit.objects.get(transaction_code=data[0], is_delete=0).user_allocation
            if data[1] != unit_token:
                message = "%s 这不是你的数据，你无权修改" % data[0]
                raise serializers.ValidationError(message)
        elif models.GoodsClass.objects.filter(transaction_code=data[0], is_delete=0).exists():
            unit_token = models.GoodsClass.objects.get(transaction_code=data[0], is_delete=0).user_allocation
            if data[1] != unit_token:
                message = "%s 这不是你的数据，你无权修改" % data[0]
                raise serializers.ValidationError(message)
        else:
            message = "%s 你所要找的数据不存在" % data[0]
            raise serializers.ValidationError(message)

class UserCheckSerializers(serializers.Serializer):
    usercheck = serializers.CharField(validators=[UserCheckRule(), ])
