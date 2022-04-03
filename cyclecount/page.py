from rest_framework.pagination import PageNumberPagination
from rest_framework.utils.urls import replace_query_param, remove_query_param
from rest_framework.exceptions import APIException

class CycleCountPageNumberPagination(PageNumberPagination):
    page_size = 10000
    page_size_query_param = "max_page"
    max_page_size = 20000
    page_query_param = 'page'
