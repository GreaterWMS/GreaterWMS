from rest_framework import serializers
from .models import AsnListModel, AsnDetailModel
from utils import datasolve

class ASNListGetSerializer(serializers.ModelSerializer):
    asn_code = serializers.CharField(read_only=True, required=False)
    asn_status = serializers.IntegerField(read_only=True, required=False)
    supplier = serializers.CharField(read_only=True, required=False)
    bar_code = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = AsnListModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'openid', ]

class ASNListPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    asn_code = serializers.CharField(read_only=False,  required=True, validators=[datasolve.asn_data_validate])
    supplier = serializers.CharField(read_only=False, required=False)
    bar_code = serializers.CharField(read_only=False, required=True)
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = AsnListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class ASNListPartialUpdateSerializer(serializers.ModelSerializer):
    asn_code = serializers.CharField(read_only=False,  required=True, validators=[datasolve.asn_data_validate])

    class Meta:
        model = AsnListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class ASNListUpdateSerializer(serializers.ModelSerializer):
    asn_code = serializers.CharField(read_only=False,  required=True, validators=[datasolve.asn_data_validate])

    class Meta:
        model = AsnListModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class ASNDetailGetSerializer(serializers.ModelSerializer):
    asn_code = serializers.CharField(read_only=True, required=False)
    supplier = serializers.CharField(read_only=True, required=False)
    goods_code = serializers.CharField(read_only=True, required=False)
    goods_desc = serializers.CharField(read_only=True, required=False)
    goods_qty = serializers.IntegerField(read_only=True, required=False)
    goods_actual_qty = serializers.IntegerField(read_only=True, required=False)
    sorted_qty = serializers.IntegerField(read_only=True, required=False)
    goods_shortage_qty = serializers.IntegerField(read_only=True, required=False)
    goods_more_qty = serializers.IntegerField(read_only=True, required=False)
    goods_damage_qty = serializers.IntegerField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = AsnDetailModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'openid']

class ASNDetailPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    asn_code = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    supplier = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    goods_code = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_desc = serializers.CharField(read_only=False, required=False)
    goods_qty = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.qty_0_data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = AsnDetailModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class ASNSortedPostSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(read_only=False, required=False, validators=[datasolve.openid_validate])
    asn_code = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    supplier = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    goods_code = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_desc = serializers.CharField(read_only=False, required=False)
    goods_qty = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.qty_data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = AsnDetailModel
        exclude = ['is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class ASNDetailUpdateSerializer(serializers.ModelSerializer):
    asn_code = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    supplier = serializers.CharField(read_only=False,  required=True, validators=[datasolve.data_validate])
    goods_code = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    goods_desc = serializers.CharField(read_only=False, required=False)
    goods_qty = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.qty_0_data_validate])
    creater = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    class Meta:
        model = AsnDetailModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class ASNDetailPartialUpdateSerializer(serializers.ModelSerializer):
    asn_code = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    supplier = serializers.CharField(read_only=False,  required=False, validators=[datasolve.data_validate])
    goods_code = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    goods_desc = serializers.CharField(read_only=False, required=False)
    goods_qty = serializers.IntegerField(read_only=False, required=False, validators=[datasolve.qty_0_data_validate])
    creater = serializers.CharField(read_only=False, required=False, validators=[datasolve.data_validate])
    class Meta:
        model = AsnDetailModel
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class MoveToBinSerializer(serializers.ModelSerializer):
    bin_name = serializers.CharField(read_only=False, required=True, validators=[datasolve.data_validate])
    qty = serializers.IntegerField(read_only=False, required=True, validators=[datasolve.qty_0_data_validate])
    class Meta:
        model = AsnDetailModel
        ref_name = 'AsnMoveToBin'
        exclude = ['openid', 'is_delete', ]
        read_only_fields = ['id', 'create_time', 'update_time', ]

class FileListRenderSerializer(serializers.ModelSerializer):
    asn_code = serializers.CharField(read_only=False, required=False)
    asn_status = serializers.IntegerField(read_only=False, required=False)
    total_weight = serializers.FloatField(read_only=False, required=False)
    total_volume = serializers.FloatField(read_only=False, required=False)
    total_cost = serializers.FloatField(read_only=False, required=False)
    supplier = serializers.CharField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    transportation_fee = serializers.JSONField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = AsnListModel
        ref_name = 'ASNFileListRenderSerializer'
        exclude = ['openid', 'is_delete', ]

class FileDetailRenderSerializer(serializers.ModelSerializer):
    asn_code = serializers.CharField(read_only=False, required=False)
    asn_status = serializers.IntegerField(read_only=False, required=False)
    goods_code = serializers.CharField(read_only=False, required=False)
    goods_desc = serializers.CharField(read_only=False, required=False)
    goods_qty = serializers.IntegerField(read_only=False, required=False)
    goods_actual_qty = serializers.IntegerField(read_only=False, required=False)
    sorted_qty = serializers.IntegerField(read_only=False, required=False)
    goods_shortage_qty = serializers.IntegerField(read_only=False, required=False)
    goods_more_qty = serializers.IntegerField(read_only=False, required=False)
    goods_damage_qty = serializers.IntegerField(read_only=False, required=False)
    goods_weight = serializers.FloatField(read_only=False, required=False)
    goods_volume = serializers.FloatField(read_only=False, required=False)
    goods_cost = serializers.FloatField(read_only=False, required=False)
    supplier = serializers.CharField(read_only=False, required=False)
    creater = serializers.CharField(read_only=False, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = AsnDetailModel
        ref_name = 'ASNFileDetailRenderSerializer'
        exclude = ['openid', 'is_delete', ]
