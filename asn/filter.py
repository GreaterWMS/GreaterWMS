from django_filters import FilterSet
from .models import AsnListModel, AsnDetailModel

class AsnListFilter(FilterSet):
    class Meta:
        model = AsnListModel
        fields = {
            "id": ['exact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }

class AsnDetailFilter(FilterSet):
    class Meta:
        model = AsnDetailModel
        fields = {
            "id": ['exact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "asn_code": ['exact', 'iexact', 'contains', 'icontains'],
            "asn_status": ['exact', 'iexact'],
            "goods_actual_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "goods_shortage_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "goods_more_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }
