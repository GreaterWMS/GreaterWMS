from django_filters import FilterSet
from .models import ListModel

class Filter(FilterSet):
    class Meta:
        model = ListModel
        fields = {
            "id": ['exact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "capital_name": ['exact', 'iexact', 'contains', 'icontains'],
            "capital_qty": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "capital_cost": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "creater": ['exact', 'iexact', 'contains', 'icontains'],
            "is_delete": ['exact', 'iexact'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }
