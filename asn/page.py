from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from supplier.models import ListModel as supplier

class MyPageNumberPaginationASNList(PageNumberPagination):
    page_size = 30
    page_size_query_param = "max_page"
    max_page_size = 1000
    page_query_param = 'page'

    def get_paginated_response(self, data):
        supplier_list_data = supplier.objects.filter(openid=self.request.auth.openid, is_delete=False)
        supplier_list = []
        for i in range(len(supplier_list_data)):
            supplier_list.append(supplier_list_data[i].supplier_name)
        return Response(OrderedDict([
            ('supplier_list', supplier_list),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
