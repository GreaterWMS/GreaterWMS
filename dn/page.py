from collections import OrderedDict
from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils.urls import remove_query_param, replace_query_param

from customer.models import ListModel as customer

class MyPageNumberPaginationDNList(PageNumberPagination):
    page_size = 30
    page_size_query_param = "max_page"
    max_page_size = 1000
    page_query_param = 'page'

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page.previous_page_number()
        ssl_check = str(self.request.META.get('HTTP_ORIGIN')).split(':')[0]
        url_combine = str(url).split(':')
        if len(str(url).split(':')) == 2:
            url = ssl_check + ':' + url_combine[1]
            if page_number == 1:
                return remove_query_param(url, self.page_query_param)
            return replace_query_param(url, self.page_query_param, page_number)
        elif len(str(url).split(':')) == 3:
            url = ssl_check + ':' + url_combine[1] + ':' + url_combine[2]
            if page_number == 1:
                return remove_query_param(url, self.page_query_param)
            return replace_query_param(url, self.page_query_param, page_number)
        else:
            raise APIException({"detail": "Wrong API Url"})

    def get_next_link(self):
        if not self.page.has_next():
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page.next_page_number()
        ssl_check = str(self.request.META.get('HTTP_ORIGIN')).split(':')[0]
        url_combine = str(url).split(':')
        if len(str(url).split(':')) == 2:
            url = ssl_check + ':' + url_combine[1]
            return replace_query_param(url, self.page_query_param, page_number)
        elif len(str(url).split(':')) == 3:
            url = ssl_check + ':' + url_combine[1] + ':' + url_combine[2]
            return replace_query_param(url, self.page_query_param, page_number)
        else:
            raise APIException({"detail": "Wrong API Url"})

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
