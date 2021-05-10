from rest_framework import viewsets
import pandas as pd
import numpy as np
from goods.models import ListModel as goodslist
from . import serializers
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class GoodlistfileViewSet(viewsets.ModelViewSet):
    """
        create:
            Create a data line（post）
    """
    queryset = goodslist.objects.all()
    serializer_class = serializers.GoodslistSerializer
    pagination_class = []

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.GoodslistSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            if excel_type in ['xlsx', 'xls', 'csv']:
                df = pd.read_excel(files)
                df.drop_duplicates(keep='first', inplace=True)
                goods_list = df.drop_duplicates(subset=['商品单位'], keep='first')
                # print(goods_list)
                # for i in range(len(goods_list)):
                #     print(i)
                # print(df.drop_duplicates(subset=[a], keep='first'))
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "Success"})
