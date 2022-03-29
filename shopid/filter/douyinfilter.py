from django_filters import FilterSet
from shopid.models.douyinmodels import ListModel

class Filter(FilterSet):
    class Meta:
        model = ListModel
        fields = {
            "id": ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte', 'isnull', 'in', 'range'],
            "openid": ['exact', 'iexact', 'contains', 'icontains'],
            "appid": ['exact', 'iexact', 'contains', 'icontains'],
            "shop_mode": ['exact', 'iexact', 'contains', 'icontains'],
            "shop_appid": ['exact', 'iexact', 'contains', 'icontains'],
            "shop_app_secret": ['exact', 'iexact', 'contains', 'icontains'],
            "shop_id": ['exact', 'iexact', 'contains', 'icontains'],
            "sandbox": ['exact', 'iexact'],
            "proxy": ['exact', 'iexact'],
            "t_code": ['exact', 'iexact'],
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }