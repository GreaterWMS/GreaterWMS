from rest_framework import serializers
from .models import ListModel
from utils import datasolve

class CustomerGetSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(read_only=True, required=False)
    customer_name = serializers.CharField(read_only=True, required=False)
    customer_group = serializers.CharField(read_only=True, required=False)
    customer_contact = serializers.CharField(read_only=True, required=False)
    customer_bank_account = serializers.CharField(read_only=True, required=False)
    customer_password = serializers.CharField(read_only=True, required=False)
    customer_refrigeration_fee = serializers.IntegerField(read_only=True, required=False)
    customer_loading_fee = serializers.IntegerField(read_only=True, required=False)
    customer_film_laminating_fee = serializers.IntegerField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', ]

class CustomerPostSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_name = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_group = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_contact = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_password = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_refrigeration_fee = serializers.IntegerField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_loading_fee = serializers.IntegerField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_film_laminating_fee = serializers.IntegerField(read_only=True, required=False,validators=[datasolve.openid_validate])
    class Meta:
        model = ListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', ]

class CustomerUpdateSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_name = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_group = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_contact = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_bank_account = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_password = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_refrigeration_fee = serializers.IntegerField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_loading_fee = serializers.IntegerField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_film_laminating_fee = serializers.IntegerField(read_only=True, required=False,validators=[datasolve.openid_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time',  ]

class CustomerPartialUpdateSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_name = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_group = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_contact = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_bank_account = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_password = serializers.CharField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_refrigeration_fee = serializers.IntegerField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_loading_fee = serializers.IntegerField(read_only=True, required=False,validators=[datasolve.openid_validate])
    customer_film_laminating_fee = serializers.IntegerField(read_only=True, required=False,validators=[datasolve.openid_validate])
    class Meta:
        model = ListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time',  ]

class FileRenderSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(read_only=True, required=False)
    customer_name = serializers.CharField(read_only=True, required=False)
    customer_group = serializers.CharField(read_only=True, required=False)
    customer_contact = serializers.CharField(read_only=True, required=False)
    customer_bank_account = serializers.CharField(read_only=True, required=False)
    customer_password = serializers.CharField(read_only=True, required=False)
    customer_refrigeration_fee = serializers.IntegerField(read_only=True, required=False)
    customer_loading_fee = serializers.IntegerField(read_only=True, required=False)
    customer_film_laminating_fee = serializers.IntegerField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = ListModel
        ref_name = 'CustomerFileRenderSerializer'
        exclude = ['openid', 'is_delete', ]
