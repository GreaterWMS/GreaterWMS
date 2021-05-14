from rest_framework import viewsets
import pandas as pd
import numpy as np
from utils.datasolve import data_validate
from goods.models import ListModel as goodslist
from goodsunit.models import ListModel as goodsunit
from goodsclass.models import ListModel as goodsclass
from goodsbrand.models import ListModel as goodsbrand
from goodscolor.models import ListModel as goodscolor
from goodsshape.models import ListModel as goodsshape
from goodsspecs.models import ListModel as goodsspecs
from goodsorigin.models import ListModel as goodsorigin
from goods import files as goodsfiles
from supplier.models import ListModel as supplier
from supplier import files as supplierfiles
from customer.models import ListModel as customer
from customer import files as customerfiles
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class GoodlistfileViewSet(viewsets.ModelViewSet):
    """
        create:
            Create a data line（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return goodslist.objects.filter(openid=self.request.auth.openid)
        else:
            return goodslist.objects.filter().none()

    def get_lang(self):
        if self.request.GET.get('lang', ''):
            lang = self.request.GET.get('lang', '')
        else:
            lang = 'zh-hans'
        if lang == 'zh-hans':
            data_header = goodsfiles.cn_data_header()
        elif lang == 'en-us':
            data_header = goodsfiles.en_data_header()
        else:
            data_header = goodsfiles.en_data_header()
        return data_header

    def create(self, request, *args, **kwargs):
        data_header = self.get_lang()
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            if excel_type in ['xlsx', 'xls', 'csv']:
                self.get_queryset().delete()
                goodsunit.objects.all().delete()
                goodsclass.objects.all().delete()
                goodsbrand.objects.all().delete()
                goodscolor.objects.all().delete()
                goodsshape.objects.all().delete()
                goodsspecs.objects.all().delete()
                goodsorigin.objects.all().delete()
                df = pd.read_excel(files)
                df.drop_duplicates(keep='first', inplace=True)
                data_list = df.drop_duplicates(subset=[data_header.get('goods_code')], keep='first').values
                for d in range(len(data_list)):
                    data_validate(str(data_list[d]))
                for i in range(len(data_list)):
                    goodslist.objects.create(openid=self.request.auth.openid,
                                             goods_code=data_list[i][0],
                                             goods_desc=data_list[i][1],
                                             goods_supplier=data_list[i][2],
                                             goods_weight=data_list[i][3],
                                             goods_w=data_list[i][4],
                                             goods_d=data_list[i][5],
                                             goods_h=data_list[i][6],
                                             unit_volume=data_list[i][7],
                                             goods_unit=data_list[i][8],
                                             goods_class=data_list[i][9],
                                             goods_brand=data_list[i][10],
                                             goods_color=data_list[i][11],
                                             goods_shape=data_list[i][12],
                                             goods_specs=data_list[i][13],
                                             goods_origin=data_list[i][14],
                                             goods_cost=data_list[i][15],
                                             goods_price=data_list[i][16],
                                             creater=self.request.auth.name
                                             )
                goods_unit_list = df.drop_duplicates(subset=[data_header.get('goods_unit')], keep='first').loc[:,
                                    data_header.get('goods_unit')].values
                for i in range(len(goods_unit_list)):
                    goodsunit.objects.create(openid=self.request.auth.openid,
                                             goods_unit=goods_unit_list[i],
                                             creater=self.request.auth.name
                                             )
                goods_class_list = df.drop_duplicates(subset=[data_header.get('goods_class')], keep='first').loc[:,
                                    data_header.get('goods_class')].values
                for i in range(len(goods_class_list)):
                    goodsclass.objects.create(openid=self.request.auth.openid,
                                              goods_class=goods_class_list[i],
                                              creater=self.request.auth.name
                                              )
                goods_brand_list = df.drop_duplicates(subset=[data_header.get('goods_brand')], keep='first').loc[:,
                                    data_header.get('goods_brand')].values
                for i in range(len(goods_brand_list)):
                    goodsbrand.objects.create(openid=self.request.auth.openid,
                                              goods_brand=goods_brand_list[i],
                                              creater=self.request.auth.name
                                              )
                goods_color_list = df.drop_duplicates(subset=[data_header.get('goods_color')], keep='first').loc[:,
                                    data_header.get('goods_color')].values
                for i in range(len(goods_color_list)):
                    goodscolor.objects.create(openid=self.request.auth.openid,
                                              goods_color=goods_color_list[i],
                                              creater=self.request.auth.name
                                              )
                goods_shape_list = df.drop_duplicates(subset=[data_header.get('goods_shape')], keep='first').loc[:,
                                    data_header.get('goods_shape')].values
                for i in range(len(goods_shape_list)):
                    goodsshape.objects.create(openid=self.request.auth.openid,
                                              goods_shape=goods_shape_list[i],
                                              creater=self.request.auth.name
                                              )
                goods_specs_list = df.drop_duplicates(subset=[data_header.get('goods_specs')], keep='first').loc[:,
                                    data_header.get('goods_specs')].values
                for i in range(len(goods_specs_list)):
                    goodsspecs.objects.create(openid=self.request.auth.openid,
                                              goods_specs=goods_specs_list[i],
                                              creater=self.request.auth.name
                                              )
                goods_origin_list = df.drop_duplicates(subset=[data_header.get('goods_origin')], keep='first').loc[:,
                                    data_header.get('goods_origin')].values
                for i in range(len(goods_origin_list)):
                    goodsorigin.objects.create(openid=self.request.auth.openid,
                                               goods_origin=goods_origin_list[i],
                                               creater=self.request.auth.name
                                               )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "Success"})

class SupplierfileViewSet(viewsets.ModelViewSet):
    """
        create:
            Create a data line（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return supplier.objects.filter(openid=self.request.auth.openid)
        else:
            return supplier.objects.filter().none()

    def get_lang(self):
        if self.request.GET.get('lang', ''):
            lang = self.request.GET.get('lang', '')
        else:
            lang = 'zh-hans'
        if lang == 'zh-hans':
            data_header = supplierfiles.cn_data_header()
        elif lang == 'en-us':
            data_header = supplierfiles.en_data_header()
        else:
            data_header = supplierfiles.en_data_header()
        return data_header

    def create(self, request, *args, **kwargs):
        data_header = self.get_lang()
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            if excel_type in ['xlsx', 'xls', 'csv']:
                self.get_queryset().delete()
                df = pd.read_excel(files)
                df.drop_duplicates(keep='first', inplace=True)
                data_list = df.drop_duplicates(subset=[data_header.get('supplier_name')], keep='first').values
                for d in range(len(data_list)):
                    data_validate(str(data_list[d]))
                for i in range(len(data_list)):
                    supplier.objects.create(openid=self.request.auth.openid,
                                            supplier_name=data_list[i][0],
                                            supplier_city=data_list[i][1],
                                            supplier_address=data_list[i][2],
                                            supplier_contact=data_list[i][3],
                                            supplier_manager=data_list[i][4],
                                            supplier_level=data_list[i][5],
                                            creater=self.request.auth.name
                                            )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "Success"})


class CustomerfileViewSet(viewsets.ModelViewSet):
    """
        create:
            Create a data line（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return customer.objects.filter(openid=self.request.auth.openid)
        else:
            return customer.objects.filter().none()

    def get_lang(self):
        if self.request.GET.get('lang', ''):
            lang = self.request.GET.get('lang', '')
        else:
            lang = 'zh-hans'
        if lang == 'zh-hans':
            data_header = customerfiles.cn_data_header()
        elif lang == 'en-us':
            data_header = customerfiles.en_data_header()
        else:
            data_header = customerfiles.en_data_header()
        return data_header

    def create(self, request, *args, **kwargs):
        data_header = self.get_lang()
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            if excel_type in ['xlsx', 'xls', 'csv']:
                self.get_queryset().delete()
                df = pd.read_excel(files)
                df.drop_duplicates(keep='first', inplace=True)
                data_list = df.drop_duplicates(subset=[data_header.get('customer_name')], keep='first').values
                for d in range(len(data_list)):
                    data_validate(str(data_list[d]))
                for i in range(len(data_list)):
                    customer.objects.create(openid=self.request.auth.openid,
                                            customer_name=data_list[i][0],
                                            customer_city=data_list[i][1],
                                            customer_address=data_list[i][2],
                                            customer_contact=data_list[i][3],
                                            customer_manager=data_list[i][4],
                                            customer_level=data_list[i][5],
                                            creater=self.request.auth.name
                                            )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "Success"})
