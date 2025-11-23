from django_filters import FilterSet
from .models import ListModel

class Filter(FilterSet):
    class Meta:
        model = ListModel
        fields = {
            "customer_id": ['exact', 'iexact', 'contains', 'icontains'],
            "customer_name": ['exact', 'iexact', 'contains', 'icontains'],
            "customer_group": ['exact', 'iexact', 'contains', 'icontains'],
            "customer_contact": ['exact', 'iexact', 'contains', 'icontains'],
            "customer_bank_account": ['exact', 'iexact', 'contains', 'icontains'],
            "customer_password": ['exact', 'iexact', 'contains', 'icontains'],
            "customer_refrigeration_fee":['exact', 'gt','gte','lt','lte','isnull','in','range'],
            "customer_loading_fee": ['exact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "customer_film_laminating_fee": ['exact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "is_delete": ['exact', 'iexact'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }

