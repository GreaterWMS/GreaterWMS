from django_filters import FilterSet
from .models import AsnListModel, AsnDetailModel

class AsnListFilter(FilterSet):
    class Meta:
        model = AsnListModel
        fields = {
            "id": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "asn_code": ['exact', 'iexact', 'contains', 'icontains'],
            "asn_status": ['exact', 'iexact',  'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "total_weight": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "total_volume": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "total_cost": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "supplier": ['exact', 'iexact', 'contains', 'icontains'],
            "creater": ['exact', 'iexact', 'contains', 'icontains'],
            "is_delete": ['exact', 'iexact'],
            "create_time": ['exact', 'iexact', 'year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['exact', 'iexact', 'year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }

class AsnDetailFilter(FilterSet):
    class Meta:
        model = AsnDetailModel
        fields = {
            "id": ['exact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "asn_code": ['exact', 'iexact', 'contains', 'icontains'],
            "asn_status": ['exact', 'iexact'],
            "supplier": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_code": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_desc": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "goods_actual_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "sorted_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "goods_shortage_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "goods_more_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "goods_damage_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "goods_weight": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "goods_volume": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "goods_cost": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "creater": ['exact', 'iexact', 'contains', 'icontains'],
            "is_delete": ['exact', 'iexact'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }
