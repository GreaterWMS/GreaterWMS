from django_filters import FilterSet
from .models import StockListModel, StockBinModel

class StockListFilter(FilterSet):
    class Meta:
        model = StockListModel
        fields = {
            "id": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "goods_code": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_desc": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_qty": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "onhand_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "can_order_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "ordered_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "inspect_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "hold_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "damage_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "asn_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "dn_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "pre_load_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "pre_sort_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "sorted_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "pick_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "picked_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "back_order_stock": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "supplier": ['exact', 'iexact', 'contains', 'icontains'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }

class StockBinFilter(FilterSet):
    class Meta:
        model = StockBinModel
        fields = {
            "id": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "bin_name": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_code": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_desc": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_qty": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "pick_qty": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "picked_qty": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "bin_size": ['exact', 'iexact', 'contains', 'icontains'],
            "bin_property": ['exact', 'iexact', 'contains', 'icontains'],
            "t_code": ['exact', 'iexact'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }
