from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from binproperty.models import ListModel as binproperty
from binsize.models import ListModel as binsize
from django.db.models import Q


class MyPageNumberPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = "max_page"
    max_page_size = 1000
    page_query_param = 'page'

    def get_paginated_response(self, data):
        bin_property_list_data = binproperty.objects.filter(Q(openid=self.request.auth.openid, is_delete=False) |
                                                            Q(openid='init_data', is_delete=False))
        bin_property_list = []
        for i in range(len(bin_property_list_data)):
            bin_property_list.append(bin_property_list_data[i].bin_property)
        bin_size_list_data = binsize.objects.filter(openid=self.request.auth.openid, is_delete=False)
        bin_size_list = []
        for i in range(len(bin_size_list_data)):
            bin_size_list.append(bin_size_list_data[i].bin_size)
        return Response(OrderedDict([
            ('bin_size_list', bin_size_list),
            ('bin_property_list', bin_property_list),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
