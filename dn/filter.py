from django_filters import FilterSet
from .models import DnListModel, DnDetailModel, PickingListModel

class DnListFilter(FilterSet):
    class Meta:
        model = DnListModel
        fields = {
            "id": ['exact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "back_order_label": ['exact', 'iexact'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }

class DnDetailFilter(FilterSet):
    class Meta:
        model = DnDetailModel
        fields = {
            "id": ['exact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "dn_code": ['exact', 'iexact', 'contains', 'icontains'],
            "dn_status": ['exact', 'iexact'],
            "pick_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "picked_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "intransit_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "delivery_actual_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "delivery_shortage_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "delivery_more_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "delivery_damage_qty": ['exact', 'iexact', 'gt', 'lt', 'gte', 'lte'],
            "back_order_label": ['exact', 'iexact'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }

class DnPickingListFilter(FilterSet):
    class Meta:
        model = PickingListModel
        fields = {
            "id": ['exact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "dn_code": ['exact', 'iexact', 'contains', 'icontains'],
            "bin_name": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_code": ['exact', 'iexact', 'contains', 'icontains'],
            "pick_qty": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "picked_qty": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "creater": ['exact', 'iexact', 'contains', 'icontains'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }
