from django_filters import FilterSet
from .models import CyclecountModeDayModel

class Filter(FilterSet):
    class Meta:
        model = CyclecountModeDayModel
        fields = {
            "id": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }

