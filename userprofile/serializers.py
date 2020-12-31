from rest_framework import serializers
from .models import Users
import re

def data_validate(data):
    script_obj = re.findall(r'script', str(data), re.IGNORECASE)
    select_obj = re.findall(r'select', str(data), re.IGNORECASE)
    if data == '1':
        raise serializers.ValidationError('Bad Data can‘not be store')
    if script_obj:
        raise serializers.ValidationError('Bad Data can‘not be store')
    elif select_obj:
        raise serializers.ValidationError('Bad Data can‘not be store')
    else:
    #独立效验器
    #raise serializers ValidationError('填写实际的地址')  #有错就抛出异常
    #没错就返回数据
        return data


class GetSerializer(serializers.ModelSerializer):
    api_name = serializers.CharField(read_only=True, validators=[data_validate])
    api_describe = serializers.CharField(read_only=True, validators=[data_validate])
    api_manager = serializers.CharField(read_only=True, validators=[data_validate])
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Users
        fields = '__all__'
        #exclude = ['id']    #排出id字段
        #扩展address: extra_kwargs={}#局部替换某些字段的设定，或者新增设为
        # extra_kwargs={
        #     "address":{
        #         "min_length":5,#给地址增加  最小长度限制
        #         "default":"默认测试地址"   #增加默认值
        #     }
        # }

class PostSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=80)
    openid = serializers.CharField(max_length=100)
    appid = serializers.CharField(max_length=100)
    ip = serializers.CharField(max_length=100)
    link_to = serializers.BooleanField(default=False)
    link_to_id = serializers.IntegerField(default=0)
    avatar = serializers.CharField(max_length=100, default='/static/img/user.jpg')
    api_name = serializers.CharField(max_length=255, min_length=1, required=True, validators=[data_validate])
    api_describe = serializers.CharField(max_length=255, min_length=1, required=True, validators=[data_validate])
    api_manager = serializers.CharField(max_length=255, min_length=1, required=True, validators=[data_validate])
    class Meta:
        model = Users
        #fields = '__all__'
        exclude = ['id']
        read_only_fields = ('create_time', 'update_time')  # 指定字段为read_only,
        #扩展address: extra_kwargs={}#局部替换某些字段的设定，或者新增设为
        # extra_kwargs={
        #     "address":{
        #         "min_length":5,#给地址增加  最小长度限制
        #         "default":"默认测试地址"   #增加默认值
        #     }
        # }


class UpdateSerializer(serializers.ModelSerializer):
    api_name = serializers.CharField(max_length=255, min_length=1, required=True, validators=[data_validate])
    api_describe = serializers.CharField(max_length=255, min_length=1, required=True, validators=[data_validate])
    api_manager = serializers.CharField(max_length=255, min_length=1, required=True, validators=[data_validate])
    class Meta:
        model = Users
        #fields = '__all__'
        exclude = ['id']  # 排出id字段
        read_only_fields = ('create_time', 'update_time')  # 指定字段为read_only,
        #扩展address: extra_kwargs={}#局部替换某些字段的设定，或者新增设为
        # extra_kwargs={
        #     "address":{
        #         "min_length":5,#给地址增加  最小长度限制
        #         "default":"默认测试地址"   #增加默认值
        #     }
        # }

class PartialUpdateSerializer(serializers.ModelSerializer):
    api_name = serializers.CharField(max_length=255, min_length=1, required=False, validators=[data_validate])
    api_describe = serializers.CharField(max_length=255, min_length=1, required=False, validators=[data_validate])
    api_manager = serializers.CharField(max_length=255, min_length=1, required=False, validators=[data_validate])
    class Meta:
        model = Users
        #fields = '__all__'
        exclude = ['id', 'create_time', 'update_time']  # 排出id字段
        read_only_fields = ('create_time', 'update_time')  # 指定字段为read_only,
        #扩展address: extra_kwargs={}#局部替换某些字段的设定，或者新增设为
        # extra_kwargs={
        #     "address":{
        #         "min_length":5,#给地址增加  最小长度限制
        #         "default":"默认测试地址"   #增加默认值
        #     }
        # }
