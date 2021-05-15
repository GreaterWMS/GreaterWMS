from rest_framework import viewsets
import pandas as pd
import numpy as np
from utils.datasolve import data_validate
from utils.datasolve import is_number
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
                    if str(data_list[i][0]) == 'nan':
                        continue
                    else:
                        if str(data_list[i][1]) == 'nan':
                            data_list[i][1] = 'None'
                        if str(data_list[i][2]) == 'nan':
                            data_list[i][2] = 'None'
                        if is_number(str(data_list[i][3])):
                            if str(data_list[i][3]) == 'nan':
                                data_list[i][3] = 0
                        else:
                            data_list[i][3] = 0
                        if is_number(str(data_list[i][4])):
                            if str(data_list[i][4]) == 'nan':
                                data_list[i][4] = 0
                        else:
                            data_list[i][4] = 0
                        if is_number(str(data_list[i][5])):
                            if str(data_list[i][5]) == 'nan':
                                data_list[i][5] = 0
                        else:
                            data_list[i][5] = 0
                        if is_number(str(data_list[i][6])):
                            if str(data_list[i][6]) == 'nan':
                                data_list[i][6] = 0
                        else:
                            data_list[i][6] = 0
                        if is_number(str(data_list[i][7])):
                            if str(data_list[i][7]) == 'nan':
                                data_list[i][7] = 0
                        else:
                            data_list[i][7] = 0
                        if str(data_list[i][8]) == 'nan':
                            data_list[i][8] = 'None'
                        if str(data_list[i][9]) == 'nan':
                            data_list[i][9] = 'None'
                        if str(data_list[i][10]) == 'nan':
                            data_list[i][10] = 'None'
                        if str(data_list[i][11]) == 'nan':
                            data_list[i][11] = 'None'
                        if str(data_list[i][12]) == 'nan':
                            data_list[i][12] = 'None'
                        if str(data_list[i][13]) == 'nan':
                            data_list[i][13] = 'None'
                        if str(data_list[i][14]) == 'nan':
                            data_list[i][14] = 'None'
                        if is_number(str(data_list[i][15])):
                            if str(data_list[i][15]) == 'nan':
                                data_list[i][15] = 0
                        else:
                            data_list[i][15] = 0
                        if is_number(str(data_list[i][16])):
                            if str(data_list[i][16]) == 'nan':
                                data_list[i][16] = 0
                        else:
                            data_list[i][16] = 0
                        goodslist.objects.create(openid=self.request.auth.openid,
                                                 goods_code=str(data_list[i][0]).strip(),
                                                 goods_desc=str(data_list[i][1]).strip(),
                                                 goods_supplier=str(data_list[i][2]).strip(),
                                                 goods_weight=data_list[i][3],
                                                 goods_w=data_list[i][4],
                                                 goods_d=data_list[i][5],
                                                 goods_h=data_list[i][6],
                                                 unit_volume=data_list[i][7],
                                                 goods_unit=str(data_list[i][8]).strip(),
                                                 goods_class=str(data_list[i][9]).strip(),
                                                 goods_brand=str(data_list[i][10]).strip(),
                                                 goods_color=str(data_list[i][11]).strip(),
                                                 goods_shape=str(data_list[i][12]).strip(),
                                                 goods_specs=str(data_list[i][13]).strip(),
                                                 goods_origin=str(data_list[i][14]).strip(),
                                                 goods_cost=data_list[i][15],
                                                 goods_price=data_list[i][16],
                                                 creater=self.request.auth.name
                                                 )
                goods_unit_list = df.drop_duplicates(subset=[data_header.get('goods_unit')], keep='first').loc[:,
                                    data_header.get('goods_unit')].values
                for i in goods_unit_list:
                    if str(i) == 'nan':
                        i = 'None'
                    goodsunit.objects.create(openid=self.request.auth.openid,
                                             goods_unit=str(i).strip(),
                                             creater=self.request.auth.name
                                             )
                goods_class_list = df.drop_duplicates(subset=[data_header.get('goods_class')], keep='first').loc[:,
                                    data_header.get('goods_class')].values
                for i in goods_class_list:
                    if str(i) == 'nan':
                        i = 'None'
                    goodsclass.objects.create(openid=self.request.auth.openid,
                                              goods_class=str(i).strip(),
                                              creater=self.request.auth.name
                                              )
                goods_brand_list = df.drop_duplicates(subset=[data_header.get('goods_brand')], keep='first').loc[:,
                                    data_header.get('goods_brand')].values
                for i in goods_brand_list:
                    if str(i) == 'nan':
                        i = 'None'
                    goodsbrand.objects.create(openid=self.request.auth.openid,
                                              goods_brand=str(i).strip(),
                                              creater=self.request.auth.name
                                              )
                goods_color_list = df.drop_duplicates(subset=[data_header.get('goods_color')], keep='first').loc[:,
                                    data_header.get('goods_color')].values
                for i in goods_color_list:
                    if str(i) == 'nan':
                        i = 'None'
                    goodscolor.objects.create(openid=self.request.auth.openid,
                                              goods_color=str(i).strip(),
                                              creater=self.request.auth.name
                                              )
                goods_shape_list = df.drop_duplicates(subset=[data_header.get('goods_shape')], keep='first').loc[:,
                                    data_header.get('goods_shape')].values
                for i in goods_shape_list:
                    if str(i) == 'nan':
                        i = 'None'
                    goodsshape.objects.create(openid=self.request.auth.openid,
                                              goods_shape=str(i).strip(),
                                              creater=self.request.auth.name
                                              )
                goods_specs_list = df.drop_duplicates(subset=[data_header.get('goods_specs')], keep='first').loc[:,
                                    data_header.get('goods_specs')].values
                for i in goods_specs_list:
                    if str(i) == 'nan':
                        i = 'None'
                    goodsspecs.objects.create(openid=self.request.auth.openid,
                                              goods_specs=str(i).strip(),
                                              creater=self.request.auth.name
                                              )
                goods_origin_list = df.drop_duplicates(subset=[data_header.get('goods_origin')], keep='first').loc[:,
                                    data_header.get('goods_origin')].values
                for i in goods_origin_list:
                    if str(i) == 'nan':
                        i = 'None'
                    goodsorigin.objects.create(openid=self.request.auth.openid,
                                               goods_origin=str(i).strip(),
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
                    if str(data_list[i][0]) == 'nan':
                        continue
                    else:
                        if str(data_list[i][1]) == 'nan':
                            data_list[i][1] = 'None'
                        if str(data_list[i][2]) == 'nan':
                            data_list[i][2] = 'None'
                        if is_number(str(data_list[i][3])):
                            if str(data_list[i][3]) == 'nan':
                                data_list[i][3] = 0
                        else:
                            data_list[i][3] = 0
                        if str(data_list[i][4]) == 'nan':
                            data_list[i][4] = 'None'
                        if is_number(str(data_list[i][5])):
                            if str(data_list[i][5]) == 'nan':
                                data_list[i][5] = 0
                        else:
                            data_list[i][5] = 0
                        supplier.objects.create(openid=self.request.auth.openid,
                                                supplier_name=str(data_list[i][0]).strip(),
                                                supplier_city=str(data_list[i][1]).strip(),
                                                supplier_address=str(data_list[i][2]).strip(),
                                                supplier_contact=data_list[i][3],
                                                supplier_manager=str(data_list[i][4]).strip(),
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
                    if str(data_list[i][0]) == 'nan':
                        continue
                    else:
                        if str(data_list[i][1]) == 'nan':
                            data_list[i][1] = 'None'
                        if str(data_list[i][2]) == 'nan':
                            data_list[i][2] = 'None'
                        if is_number(str(data_list[i][3])):
                            if str(data_list[i][3]) == 'nan':
                                data_list[i][3] = 0
                        else:
                            data_list[i][3] = 0
                        if str(data_list[i][4]) == 'nan':
                            data_list[i][4] = 'None'
                        if is_number(str(data_list[i][5])):
                            if str(data_list[i][5]) == 'nan':
                                data_list[i][5] = 0
                        else:
                            data_list[i][5] = 0
                        customer.objects.create(openid=self.request.auth.openid,
                                                customer_name=str(data_list[i][0]).strip(),
                                                customer_city=str(data_list[i][1]).strip(),
                                                customer_address=str(data_list[i][2]).strip(),
                                                customer_contact=data_list[i][3],
                                                customer_manager=str(data_list[i][4]).strip(),
                                                customer_level=data_list[i][5],
                                                creater=self.request.auth.name
                                                )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "Success"})
