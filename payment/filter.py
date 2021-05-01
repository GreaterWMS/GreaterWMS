from django_filters import FilterSet
from .models import TransportationFeeListModel

class TransportationFeeListFilter(FilterSet):
    class Meta:
        model = TransportationFeeListModel
        fields = {
            "id": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "send_city": ['exact', 'iexact', 'contains', 'icontains'],
            "receiver_city": ['exact', 'iexact', 'contains', 'icontains'],
            "weight_fee": ['exact', 'iexact', 'contains', 'icontains', 'gt', 'gte', 'lt', 'lte', 'range'],
            "volume_fee": ['exact', 'iexact', 'contains', 'icontains', 'gt', 'gte', 'lt', 'lte', 'range'],
            "min_payment": ['exact', 'iexact', 'contains', 'icontains', 'gt', 'gte', 'lt', 'lte', 'range'],
            "transportation_supplier": ['exact', 'iexact', 'contains', 'icontains'],
            "creater": ['exact', 'iexact', 'contains', 'icontains'],
            "is_delete": ['exact', 'iexact'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }
