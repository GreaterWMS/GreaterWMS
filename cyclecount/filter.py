from django_filters import FilterSet
from .models import CyclecountModeDayModel
from .models import QTYRecorder
class Filter(FilterSet):
    class Meta:
        model = CyclecountModeDayModel
        fields = {
            "id": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }

class QTYRecorderListFilter(FilterSet):
    class Meta:
        model = QTYRecorder
        fields = {
            "id": ['exact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "mode_code": ['exact', 'iexact', 'contains', 'icontains'],
            "bin_name": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_code": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_desc": ['exact', 'iexact', 'contains', 'icontains'],
            "goods_qty": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'range'],
            "creater": ['exact', 'iexact', 'contains', 'icontains'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }