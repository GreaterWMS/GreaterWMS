from rest_framework import viewsets, views
import pandas as pd
import numpy as np
from utils.datasolve import data_validate
from utils.datasolve import is_number
from utils.md5 import Md5
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
from payment.models import TransportationFeeListModel as freight
from capital.models import ListModel as capital
from scanner.models import ListModel as scanner
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from staff.models import ListModel as staff

class GoodlistfileViewSet(views.APIView):
    """
        create:
            Upload One Excel（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return goodslist.objects.filter(openid=self.request.auth.openid)
        else:
            return goodslist.objects.filter().none()

    def get_lang(self):
        if self.request.user:
            lang = self.request.META.get('HTTP_LANGUAGE')
        else:
            lang = 'en-us'
        if lang == 'zh-hans':
            data_header = goodsfiles.cn_data_header()
        elif lang == 'en-us':
            data_header = goodsfiles.en_data_header()
        else:
            data_header = goodsfiles.en_data_header()
        return data_header

    def post(self, request, *args, **kwargs):
        data_header = self.get_lang()
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                              id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
            if excel_type in ['xlsx', 'xls', 'csv']:
                self.get_queryset().delete()
                goodsunit.objects.all().delete()
                goodsclass.objects.all().delete()
                goodsbrand.objects.all().delete()
                goodscolor.objects.all().delete()
                goodsshape.objects.all().delete()
                goodsspecs.objects.all().delete()
                goodsorigin.objects.all().delete()
                scanner.objects.filter(openid=self.request.auth.openid, mode='GOODS').delete()
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
                            data_list[i][1] = 'N/A'
                        if str(data_list[i][2]) == 'nan':
                            data_list[i][2] = 'N/A'
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
                            data_list[i][8] = 'N/A'
                        if str(data_list[i][9]) == 'nan':
                            data_list[i][9] = 'N/A'
                        if str(data_list[i][10]) == 'nan':
                            data_list[i][10] = 'N/A'
                        if str(data_list[i][11]) == 'nan':
                            data_list[i][11] = 'N/A'
                        if str(data_list[i][12]) == 'nan':
                            data_list[i][12] = 'N/A'
                        if str(data_list[i][13]) == 'nan':
                            data_list[i][13] = 'N/A'
                        if str(data_list[i][14]) == 'nan':
                            data_list[i][14] = 'N/A'
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
                        bar_code = Md5.md5(str(data_list[i][0]).strip())
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
                                                 bar_code=bar_code,
                                                 creater=str(staff_name)
                                                 )
                        scanner.objects.create(openid=self.request.auth.openid, mode="GOODS",
                                               code=str(data_list[i][0]).strip(),
                                               bar_code=bar_code)
                goods_supplier_list = df.drop_duplicates(subset=[data_header.get('goods_supplier')], keep='first').loc[
                                      :,
                                      data_header.get('goods_supplier')].values
                for i in goods_supplier_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if supplier.objects.filter(openid=self.request.auth.openid,
                                            supplier_name=str(i).strip()).exists():
                        pass
                    else:
                        supplier.objects.create(openid=self.request.auth.openid,
                                                supplier_name=str(i).strip(),
                                                supplier_city="Supplier City",
                                                supplier_address="Supplier Address",
                                                supplier_contact="Supplier Contact",
                                                supplier_manager="Supplier Manager",
                                                creater=str(staff_name)
                                                )
                goods_unit_list = df.drop_duplicates(subset=[data_header.get('goods_unit')], keep='first').loc[:,
                                    data_header.get('goods_unit')].values
                for i in goods_unit_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsunit.objects.filter(openid=self.request.auth.openid,
                                                goods_unit=str(i).strip()).exists():
                        pass
                    else:
                        goodsunit.objects.create(openid=self.request.auth.openid,
                                                 goods_unit=str(i).strip(),
                                                 creater=str(staff_name)
                                                 )
                goods_class_list = df.drop_duplicates(subset=[data_header.get('goods_class')], keep='first').loc[:,
                                    data_header.get('goods_class')].values
                for i in goods_class_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsclass.objects.filter(openid=self.request.auth.openid,
                                                 goods_class=str(i).strip()).exists():
                        pass
                    else:
                        goodsclass.objects.create(openid=self.request.auth.openid,
                                                  goods_class=str(i).strip(),
                                                  creater=str(staff_name)
                                                  )
                goods_brand_list = df.drop_duplicates(subset=[data_header.get('goods_brand')], keep='first').loc[:,
                                    data_header.get('goods_brand')].values
                for i in goods_brand_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsbrand.objects.filter(openid=self.request.auth.openid,
                                               goods_brand=str(i).strip()).exists():
                        pass
                    else:
                        goodsbrand.objects.create(openid=self.request.auth.openid,
                                                  goods_brand=str(i).strip(),
                                                  creater=str(staff_name)
                                                  )
                goods_color_list = df.drop_duplicates(subset=[data_header.get('goods_color')], keep='first').loc[:,
                                    data_header.get('goods_color')].values
                for i in goods_color_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodscolor.objects.filter(openid=self.request.auth.openid,
                                                 goods_color=str(i).strip()).exists():
                        pass
                    else:
                        goodscolor.objects.create(openid=self.request.auth.openid,
                                                  goods_color=str(i).strip(),
                                                  creater=str(staff_name)
                                                  )
                goods_shape_list = df.drop_duplicates(subset=[data_header.get('goods_shape')], keep='first').loc[:,
                                    data_header.get('goods_shape')].values
                for i in goods_shape_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsshape.objects.filter(openid=self.request.auth.openid,
                                                 goods_shape=str(i).strip()).exists():
                        pass
                    else:
                        goodsshape.objects.create(openid=self.request.auth.openid,
                                                  goods_shape=str(i).strip(),
                                                  creater=str(staff_name)
                                                  )
                goods_specs_list = df.drop_duplicates(subset=[data_header.get('goods_specs')], keep='first').loc[:,
                                    data_header.get('goods_specs')].values
                for i in goods_specs_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsspecs.objects.filter(openid=self.request.auth.openid,
                                                 goods_specs=str(i).strip()).exists():
                        pass
                    else:
                        goodsspecs.objects.create(openid=self.request.auth.openid,
                                                  goods_specs=str(i).strip(),
                                                  creater=str(staff_name)
                                                  )
                goods_origin_list = df.drop_duplicates(subset=[data_header.get('goods_origin')], keep='first').loc[:,
                                    data_header.get('goods_origin')].values
                for i in goods_origin_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsorigin.objects.filter(openid=self.request.auth.openid,
                                                  goods_origin=str(i).strip()).exists():
                        pass
                    else:
                        goodsorigin.objects.create(openid=self.request.auth.openid,
                                                   goods_origin=str(i).strip(),
                                                   creater=str(staff_name)
                                                   )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "success"})

class SupplierfileViewSet(views.APIView):
    """
        create:
            Upload One Excel（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return supplier.objects.filter(openid=self.request.auth.openid)
        else:
            return supplier.objects.filter().none()

    def get_lang(self):
        if self.request.user:
            lang = self.request.META.get('HTTP_LANGUAGE')
        else:
            lang = 'en-us'
        if lang == 'zh-hans':
            data_header = supplierfiles.cn_data_header()
        elif lang == 'en-us':
            data_header = supplierfiles.en_data_header()
        else:
            data_header = supplierfiles.en_data_header()
        return data_header

    def post(self, request, *args, **kwargs):
        data_header = self.get_lang()
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                              id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
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
                            data_list[i][1] = 'N/A'
                        if str(data_list[i][2]) == 'nan':
                            data_list[i][2] = 'N/A'
                        if is_number(str(data_list[i][3])):
                            if str(data_list[i][3]) == 'nan':
                                data_list[i][3] = 0
                        else:
                            data_list[i][3] = 0
                        if str(data_list[i][4]) == 'nan':
                            data_list[i][4] = 'N/A'
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
                                                creater=str(staff_name)
                                                )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "success"})

class CustomerfileViewSet(views.APIView):
    """
        create:
            Upload One Excel（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return customer.objects.filter(openid=self.request.auth.openid)
        else:
            return customer.objects.filter().none()

    def get_lang(self):
        if self.request.user:
            lang = self.request.META.get('HTTP_LANGUAGE')
        else:
            lang = 'en-us'
        if lang == 'zh-hans':
            data_header = customerfiles.cn_data_header()
        elif lang == 'en-us':
            data_header = customerfiles.en_data_header()
        else:
            data_header = customerfiles.en_data_header()
        return data_header

    def post(self, request, *args, **kwargs):
        data_header = self.get_lang()
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                              id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
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
                            data_list[i][1] = 'N/A'
                        if str(data_list[i][2]) == 'nan':
                            data_list[i][2] = 'N/A'
                        if is_number(str(data_list[i][3])):
                            if str(data_list[i][3]) == 'nan':
                                data_list[i][3] = 0
                        else:
                            data_list[i][3] = 0
                        if str(data_list[i][4]) == 'nan':
                            data_list[i][4] = 'N/A'
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
                                                creater=str(staff_name)
                                                )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "success"})

class CapitalfileViewSet(views.APIView):
    """
        create:
            Upload One Excel（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return capital.objects.filter(openid=self.request.auth.openid)
        else:
            return capital.objects.filter().none()

    def post(self, request, *args, **kwargs):
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                              id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
            if excel_type in ['xlsx', 'xls', 'csv']:
                self.get_queryset().delete()
                df = pd.read_excel(files)
                data_list = df.drop_duplicates(keep='first', inplace=True)
                for d in range(len(data_list)):
                    data_validate(str(data_list[d]))
                for i in range(len(data_list)):
                    if str(data_list[i][0]) == 'nan':
                        continue
                    else:
                        if is_number(str(data_list[i][1])):
                            if str(data_list[i][1]) == 'nan':
                                data_list[i][1] = 0
                        else:
                            data_list[i][1] = 0
                        if is_number(str(data_list[i][2])):
                            if str(data_list[i][2]) == 'nan':
                                data_list[i][2] = 0
                        else:
                            data_list[i][2] = 0
                        capital.objects.create(openid=self.request.auth.openid,
                                               capital_name=str(data_list[i][0]).strip(),
                                               capital_qty=data_list[i][1],
                                               capital_cost=data_list[i][2],
                                               creater=str(staff_name)
                                               )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "success"})

class FreightfileViewSet(views.APIView):
    """
        create:
            Upload One Excel（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return freight.objects.filter(openid=self.request.auth.openid)
        else:
            return freight.objects.filter().none()

    def post(self, request, *args, **kwargs):
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                              id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
            if excel_type in ['xlsx', 'xls', 'csv']:
                self.get_queryset().delete()
                df = pd.read_excel(files)
                data_list = df.drop_duplicates(keep='first', inplace=True).values
                for d in range(len(data_list)):
                    data_validate(str(data_list[d]))
                for i in range(len(data_list)):
                        if str(data_list[i][0]) == 'nan':
                            data_list[i][0] = 'N/A'
                        if str(data_list[i][1]) == 'nan':
                            data_list[i][1] = 'N/A'
                        if is_number(str(data_list[i][2])):
                            if str(data_list[i][2]) == 'nan':
                                data_list[i][2] = 0
                        else:
                            data_list[i][2] = 0
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
                        if str(data_list[i][5]) == 'nan':
                            data_list[i][5] = 'N/A'
                        freight.objects.create(openid=self.request.auth.openid,
                                               send_city=str(data_list[i][0]).strip(),
                                               receiver_city=str(data_list[i][1]).strip(),
                                               weight_fee=data_list[i][2],
                                               volume_fee=data_list[i][3],
                                               min_payment=data_list[i][4],
                                               transportation_supplier=str(data_list[i][5]).strip(),
                                               creater=str(staff_name)
                                               )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "success"})

class GoodlistfileAddViewSet(views.APIView):
    """
        create:
            Upload One Excel（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return goodslist.objects.filter(openid=self.request.auth.openid)
        else:
            return goodslist.objects.filter().none()

    def get_lang(self):
        if self.request.user:
            lang = self.request.META.get('HTTP_LANGUAGE')
        else:
            lang = 'en-us'
        if lang == 'zh-hans':
            data_header = goodsfiles.cn_data_header()
        elif lang == 'en-us':
            data_header = goodsfiles.en_data_header()
        else:
            data_header = goodsfiles.en_data_header()
        return data_header

    def post(self, request, *args, **kwargs):
        data_header = self.get_lang()
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                              id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
            if excel_type in ['xlsx', 'xls', 'csv']:
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
                            data_list[i][1] = 'N/A'
                        if str(data_list[i][2]) == 'nan':
                            data_list[i][2] = 'N/A'
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
                            data_list[i][8] = 'N/A'
                        if str(data_list[i][9]) == 'nan':
                            data_list[i][9] = 'N/A'
                        if str(data_list[i][10]) == 'nan':
                            data_list[i][10] = 'N/A'
                        if str(data_list[i][11]) == 'nan':
                            data_list[i][11] = 'N/A'
                        if str(data_list[i][12]) == 'nan':
                            data_list[i][12] = 'N/A'
                        if str(data_list[i][13]) == 'nan':
                            data_list[i][13] = 'N/A'
                        if str(data_list[i][14]) == 'nan':
                            data_list[i][14] = 'N/A'
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
                        if goodslist.objects.filter(openid=self.request.auth.openid,
                                                     goods_code=str(data_list[i][0]).strip()).exists():
                            pass
                        else:
                            bar_code = Md5.md5(str(data_list[i][0]).strip())
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
                                                     bar_code=bar_code,
                                                     creater=str(staff_name)
                                                     )
                            scanner.objects.create(openid=self.request.auth.openid, mode="GOODS",
                                                   code=str(data_list[i][0]).strip(),
                                                   bar_code=bar_code)
                goods_supplier_list = df.drop_duplicates(subset=[data_header.get('goods_supplier')], keep='first').loc[:,
                                      data_header.get('goods_supplier')].values
                for i in goods_supplier_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if supplier.objects.filter(openid=self.request.auth.openid,
                                               supplier_name=str(i).strip()).exists():
                        pass
                    else:
                        supplier.objects.create(openid=self.request.auth.openid,
                                                supplier_name=str(i).strip(),
                                                supplier_city="Supplier City",
                                                supplier_address="Supplier Address",
                                                supplier_contact="Supplier Contact",
                                                supplier_manager="Supplier Manager",
                                                creater=str(staff_name)
                                                )
                goods_unit_list = df.drop_duplicates(subset=[data_header.get('goods_unit')], keep='first').loc[:,
                                    data_header.get('goods_unit')].values
                for i in goods_unit_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsunit.objects.filter(openid=self.request.auth.openid,
                                                goods_unit=str(i).strip()).exists():
                        pass
                    else:
                        goodsunit.objects.create(openid=self.request.auth.openid,
                                                 goods_unit=str(i).strip(),
                                                 creater=str(staff_name)
                                                 )
                goods_class_list = df.drop_duplicates(subset=[data_header.get('goods_class')], keep='first').loc[:,
                                    data_header.get('goods_class')].values
                for i in goods_class_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsclass.objects.filter(openid=self.request.auth.openid,
                                              goods_class=str(i).strip()).exists():
                        pass
                    else:
                        goodsclass.objects.create(openid=self.request.auth.openid,
                                                  goods_class=str(i).strip(),
                                                  creater=str(staff_name)
                                                  )
                goods_brand_list = df.drop_duplicates(subset=[data_header.get('goods_brand')], keep='first').loc[:,
                                    data_header.get('goods_brand')].values
                for i in goods_brand_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsbrand.objects.filter(openid=self.request.auth.openid,
                                                 goods_brand=str(i).strip()).exists():
                        pass
                    else:
                        goodsbrand.objects.create(openid=self.request.auth.openid,
                                                  goods_brand=str(i).strip(),
                                                  creater=str(staff_name)
                                                  )
                goods_color_list = df.drop_duplicates(subset=[data_header.get('goods_color')], keep='first').loc[:,
                                    data_header.get('goods_color')].values
                for i in goods_color_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodscolor.objects.filter(openid=self.request.auth.openid,
                                                 goods_color=str(i).strip()).exists():
                        pass
                    else:
                        goodscolor.objects.create(openid=self.request.auth.openid,
                                                  goods_color=str(i).strip(),
                                                  creater=str(staff_name)
                                                  )
                goods_shape_list = df.drop_duplicates(subset=[data_header.get('goods_shape')], keep='first').loc[:,
                                    data_header.get('goods_shape')].values
                for i in goods_shape_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsshape.objects.filter(openid=self.request.auth.openid,
                                                 goods_shape=str(i).strip()).exists():
                        pass
                    else:
                        goodsshape.objects.create(openid=self.request.auth.openid,
                                                  goods_shape=str(i).strip(),
                                                  creater=str(staff_name)
                                                  )
                goods_specs_list = df.drop_duplicates(subset=[data_header.get('goods_specs')], keep='first').loc[:,
                                    data_header.get('goods_specs')].values
                for i in goods_specs_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsspecs.objects.filter(openid=self.request.auth.openid,
                                              goods_specs=str(i).strip()).exists():
                        pass
                    else:
                        goodsspecs.objects.create(openid=self.request.auth.openid,
                                                  goods_specs=str(i).strip(),
                                                  creater=str(staff_name)
                                                  )
                goods_origin_list = df.drop_duplicates(subset=[data_header.get('goods_origin')], keep='first').loc[:,
                                    data_header.get('goods_origin')].values
                for i in goods_origin_list:
                    if str(i) == 'nan':
                        i = 'N/A'
                    if goodsorigin.objects.filter(openid=self.request.auth.openid,
                                                  goods_origin=str(i).strip()).exists():
                        pass
                    else:
                        goodsorigin.objects.create(openid=self.request.auth.openid,
                                                   goods_origin=str(i).strip(),
                                                   creater=str(staff_name)
                                                   )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "success"})

class SupplierfileAddViewSet(views.APIView):
    """
        create:
            Upload One Excel（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return supplier.objects.filter(openid=self.request.auth.openid)
        else:
            return supplier.objects.filter().none()

    def get_lang(self):
        if self.request.user:
            lang = self.request.META.get('HTTP_LANGUAGE')
        else:
            lang = 'en-us'
        if lang == 'zh-hans':
            data_header = supplierfiles.cn_data_header()
        elif lang == 'en-us':
            data_header = supplierfiles.en_data_header()
        else:
            data_header = supplierfiles.en_data_header()
        return data_header

    def post(self, request, *args, **kwargs):
        data_header = self.get_lang()
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                              id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
            if excel_type in ['xlsx', 'xls', 'csv']:
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
                            data_list[i][1] = 'N/A'
                        if str(data_list[i][2]) == 'nan':
                            data_list[i][2] = 'N/A'
                        if is_number(str(data_list[i][3])):
                            if str(data_list[i][3]) == 'nan':
                                data_list[i][3] = 0
                        else:
                            data_list[i][3] = 0
                        if str(data_list[i][4]) == 'nan':
                            data_list[i][4] = 'N/A'
                        if is_number(str(data_list[i][5])):
                            if str(data_list[i][5]) == 'nan':
                                data_list[i][5] = 0
                        else:
                            data_list[i][5] = 0
                        if supplier.objects.filter(openid=self.request.auth.openid,
                                                   supplier_name=str(data_list[i][0]).strip(),
                                                   supplier_city=str(data_list[i][1]).strip(),
                                                   supplier_address=str(data_list[i][2]).strip(),
                                                   supplier_contact=data_list[i][3],
                                                   supplier_manager=str(data_list[i][4]).strip(),
                                                   supplier_level=data_list[i][5],
                                                   creater=str(staff_name)
                                                   ).exists():
                            pass
                        else:
                            supplier.objects.create(openid=self.request.auth.openid,
                                                    supplier_name=str(data_list[i][0]).strip(),
                                                    supplier_city=str(data_list[i][1]).strip(),
                                                    supplier_address=str(data_list[i][2]).strip(),
                                                    supplier_contact=data_list[i][3],
                                                    supplier_manager=str(data_list[i][4]).strip(),
                                                    supplier_level=data_list[i][5],
                                                    creater=str(staff_name)
                                                    )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "success"})

class CustomerfileAddViewSet(views.APIView):
    """
        create:
            Upload One Excel（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return customer.objects.filter(openid=self.request.auth.openid)
        else:
            return customer.objects.filter().none()

    def get_lang(self):
        if self.request.user:
            lang = self.request.META.get('HTTP_LANGUAGE')
        else:
            lang = 'en-us'
        if lang == 'zh-hans':
            data_header = customerfiles.cn_data_header()
        elif lang == 'en-us':
            data_header = customerfiles.en_data_header()
        else:
            data_header = customerfiles.en_data_header()
        return data_header

    def post(self, request, *args, **kwargs):
        data_header = self.get_lang()
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                              id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
            if excel_type in ['xlsx', 'xls', 'csv']:
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
                            data_list[i][1] = 'N/A'
                        if str(data_list[i][2]) == 'nan':
                            data_list[i][2] = 'N/A'
                        if is_number(str(data_list[i][3])):
                            if str(data_list[i][3]) == 'nan':
                                data_list[i][3] = 0
                        else:
                            data_list[i][3] = 0
                        if str(data_list[i][4]) == 'nan':
                            data_list[i][4] = 'N/A'
                        if is_number(str(data_list[i][5])):
                            if str(data_list[i][5]) == 'nan':
                                data_list[i][5] = 0
                        else:
                            data_list[i][5] = 0
                        if customer.objects.filter(openid=self.request.auth.openid,
                                                   customer_name=str(data_list[i][0]).strip(),
                                                   customer_city=str(data_list[i][1]).strip(),
                                                   customer_address=str(data_list[i][2]).strip(),
                                                   customer_contact=data_list[i][3],
                                                   customer_manager=str(data_list[i][4]).strip(),
                                                   customer_level=data_list[i][5],
                                                   ).exists():
                            pass
                        else:
                            customer.objects.create(openid=self.request.auth.openid,
                                                    customer_name=str(data_list[i][0]).strip(),
                                                    customer_city=str(data_list[i][1]).strip(),
                                                    customer_address=str(data_list[i][2]).strip(),
                                                    customer_contact=data_list[i][3],
                                                    customer_manager=str(data_list[i][4]).strip(),
                                                    customer_level=data_list[i][5],
                                                    creater=str(staff_name)
                                                    )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "success"})

class CapitalfileAddViewSet(views.APIView):
    """
        create:
            Upload One Excel（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return capital.objects.filter(openid=self.request.auth.openid)
        else:
            return capital.objects.filter().none()

    def post(self, request, *args, **kwargs):
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                              id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
            if excel_type in ['xlsx', 'xls', 'csv']:
                df = pd.read_excel(files)
                data_list = df.drop_duplicates(keep='first', inplace=True)
                for d in range(len(data_list)):
                    data_validate(str(data_list[d]))
                for i in range(len(data_list)):
                    if str(data_list[i][0]) == 'nan':
                        continue
                    else:
                        if is_number(str(data_list[i][1])):
                            if str(data_list[i][1]) == 'nan':
                                data_list[i][1] = 0
                        else:
                            data_list[i][1] = 0
                        if is_number(str(data_list[i][2])):
                            if str(data_list[i][2]) == 'nan':
                                data_list[i][2] = 0
                        else:
                            data_list[i][2] = 0
                        if capital.objects.filter(openid=self.request.auth.openid,
                                                   capital_name=str(data_list[i][0]).strip(),
                                                   capital_qty=data_list[i][1],
                                                   capital_cost=data_list[i][2],
                                                   ).exists():
                            pass
                        else:
                            capital.objects.create(openid=self.request.auth.openid,
                                                   capital_name=str(data_list[i][0]).strip(),
                                                   capital_qty=data_list[i][1],
                                                   capital_cost=data_list[i][2],
                                                   creater=str(staff_name)
                                                   )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "success"})

class FreightfileAddViewSet(views.APIView):
    """
        create:
            Upload One Excel（post）
    """
    pagination_class = []

    def get_queryset(self):
        if self.request.user:
            return freight.objects.filter(openid=self.request.auth.openid)
        else:
            return freight.objects.filter().none()

    def post(self, request, *args, **kwargs):
        files = self.request.FILES.get('file')
        if files:
            excel_type = files.name.split('.')[1]
            staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                              id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
            if excel_type in ['xlsx', 'xls', 'csv']:
                df = pd.read_excel(files)
                data_list = df.drop_duplicates(keep='first', inplace=True).values
                for d in range(len(data_list)):
                    data_validate(str(data_list[d]))
                for i in range(len(data_list)):
                        if str(data_list[i][0]) == 'nan':
                            data_list[i][0] = 'N/A'
                        if str(data_list[i][1]) == 'nan':
                            data_list[i][1] = 'N/A'
                        if is_number(str(data_list[i][2])):
                            if str(data_list[i][2]) == 'nan':
                                data_list[i][2] = 0
                        else:
                            data_list[i][2] = 0
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
                        if str(data_list[i][5]) == 'nan':
                            data_list[i][5] = 'N/A'
                        if freight.objects.filter(openid=self.request.auth.openid,
                                                  send_city=str(data_list[i][0]).strip(),
                                                  receiver_city=str(data_list[i][1]).strip(),
                                                  weight_fee=data_list[i][2],
                                                  volume_fee=data_list[i][3],
                                                  min_payment=data_list[i][4],
                                                  transportation_supplier=str(data_list[i][5]).strip()
                                                  ).exists():
                            pass
                        else:
                            freight.objects.create(openid=self.request.auth.openid,
                                                   send_city=str(data_list[i][0]).strip(),
                                                   receiver_city=str(data_list[i][1]).strip(),
                                                   weight_fee=data_list[i][2],
                                                   volume_fee=data_list[i][3],
                                                   min_payment=data_list[i][4],
                                                   transportation_supplier=str(data_list[i][5]).strip(),
                                                   creater=str(staff_name)
                                                   )
            else:
                raise APIException({"detail": "Can Not Support This File Type"})
        else:
            raise APIException({"detail": "Please Select One File"})
        return Response({"detail": "success"})
