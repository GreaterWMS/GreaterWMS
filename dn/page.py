from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from customer.models import ListModel as customer

class MyPageNumberPaginationDNList(PageNumberPagination):
    page_size = 30
    page_size_query_param = "max_page"
    max_page_size = 1000
    page_query_param = 'page'

    def get_paginated_response(self, data):
        customer_list_data = customer.objects.filter(openid=self.request.auth.openid, is_delete=False)
        customer_list = []
        for i in range(len(customer_list_data)):
            customer_list.append(customer_list_data[i].customer_name)
        return Response(OrderedDict([
            ('customer_list', customer_list),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
