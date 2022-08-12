from rest_framework import viewsets
from .models import AsnListModel, AsnDetailModel
from . import serializers
from .page import MyPageNumberPaginationASNList
from utils.page import MyPageNumberPagination
from utils.datasolve import sumOfList, transportation_calculate
from utils.fbmsg import FBMsg
from utils.md5 import Md5
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import AsnListFilter, AsnDetailFilter
from rest_framework.exceptions import APIException
from supplier.models import ListModel as supplier
from warehouse.models import ListModel as warehouse
from goods.models import ListModel as goods
from payment.models import TransportationFeeListModel as transportation
from stock.models import StockListModel as stocklist
from stock.models import StockBinModel as stockbin
from binset.models import ListModel as binset
from scanner.models import ListModel as scanner
from cyclecount.models import QTYRecorder as qtychangerecorder
from cyclecount.models import CyclecountModeDayModel as cyclecount
from django.db.models import Q
from django.db.models import Sum
from .serializers import FileListRenderSerializer, FileDetailRenderSerializer
from django.http import StreamingHttpResponse
from django.utils import timezone
from .files import FileListRenderCN, FileListRenderEN, FileDetailRenderCN, FileDetailRenderEN
from rest_framework.settings import api_settings
from dateutil.relativedelta import relativedelta
from staff.models import ListModel as staff

class AsnListViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）
        list:
            Response a data list（all）
        create:
            Create a data line（post）

        delete:
            Delete a data line（delete)

    """
    pagination_class = MyPageNumberPaginationASNList
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = AsnListFilter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            empty_qs = AsnListModel.objects.filter(Q(openid=self.request.auth.openid, asn_status=1, is_delete=False) & Q(supplier=''))
            cur_date = timezone.now()
            date_check = relativedelta(day=1)
            if len(empty_qs) > 0:
                for i in range(len(empty_qs)):
                    if empty_qs[i].create_time <= cur_date - date_check:
                        empty_qs[i].delete()
            if id is None:
                return AsnListModel.objects.filter(Q(openid=self.request.auth.openid, is_delete=False) & ~Q(supplier=''))
            else:
                return AsnListModel.objects.filter(Q(openid=self.request.auth.openid, id=id, is_delete=False) & ~Q(supplier=''))
        else:
            return AsnListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'destroy']:
            return serializers.ASNListGetSerializer
        elif self.action in ['create']:
            return serializers.ASNListPostSerializer
        elif self.action in ['update']:
            return serializers.ASNListUpdateSerializer
        elif self.action in ['partial_update']:
            return serializers.ASNListPartialUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def notice_lang(self):
        return FBMsg(self.request.META.get('HTTP_LANGUAGE'))

    def create(self, request, *args, **kwargs):
        data = self.request.data
        data['openid'] = self.request.auth.openid
        custom_asn = self.request.GET.get('custom_asn', '')
        if custom_asn:
            data['asn_code'] = custom_asn
        else:
            qs_set = AsnListModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            order_day =str(timezone.now().strftime('%Y%m%d'))
            if len(qs_set) > 0:
                asn_last_code = qs_set.order_by('-id').first().asn_code
                if str(asn_last_code[3:11]) == order_day:
                    order_create_no = str(int(asn_last_code[11:]) + 1)
                    data['asn_code'] = 'ASN' + order_day + order_create_no
                else:
                    data['asn_code'] = 'ASN' + order_day + '1'
            else:
                data['asn_code'] = 'ASN' + order_day + '1'
        data['bar_code'] = Md5.md5(data['asn_code'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        scanner.objects.create(openid=self.request.auth.openid, mode="ASN", code=data['asn_code'], bar_code=data['bar_code'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=200, headers=headers)

    def destroy(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot delete data which not yours"})
        else:
            if qs.asn_status == 1:
                qs.is_delete = True
                asn_detail_list = AsnDetailModel.objects.filter(openid=self.request.auth.openid, asn_code=qs.asn_code,
                                              asn_status=1, is_delete=False)
                for i in range(len(asn_detail_list)):
                    goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                goods_code=str(asn_detail_list[i].goods_code)).first()
                    goods_qty_change.goods_qty = goods_qty_change.goods_qty - int(asn_detail_list[i].goods_qty)
                    goods_qty_change.asn_stock = goods_qty_change.asn_stock - int(asn_detail_list[i].goods_qty)
                    goods_qty_change.save()
                asn_detail_list.update(is_delete=True)
                qs.save()
                serializer = self.get_serializer(qs, many=False)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=200, headers=headers)
            else:
                raise APIException({"detail": "This ASN Status Is Not '1'"})

class AsnDetailViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）

        list:
            Response a data list（all）

        create:
            Create a data line（post）

        update:
            Update a data（put：update）
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = AsnDetailFilter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return AsnDetailModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return AsnDetailModel.objects.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return AsnDetailModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.ASNDetailGetSerializer
        elif self.action in ['create']:
            return serializers.ASNDetailPostSerializer
        elif self.action in ['update']:
            return serializers.ASNDetailUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        if AsnListModel.objects.filter(openid=self.request.auth.openid, asn_code=str(data['asn_code']), is_delete=False).exists():
            if supplier.objects.filter(openid=self.request.auth.openid, supplier_name=str(data['supplier']), is_delete=False).exists():
                staff_name = staff.objects.filter(openid=self.request.auth.openid, id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
                for i in range(len(data['goods_code'])):
                    check_data = {
                        'openid': self.request.auth.openid,
                        'asn_code': str(data['asn_code']),
                        'supplier': str(data['supplier']),
                        'goods_code': str(data['goods_code'][i]),
                        'goods_qty': int(data['goods_qty'][i]),
                        'creater': str(staff_name)
                    }
                    serializer = self.get_serializer(data=check_data)
                    serializer.is_valid(raise_exception=True)
                post_data_list = []
                weight_list = []
                volume_list = []
                cost_list = []
                for j in range(len(data['goods_code'])):
                    goods_detail = goods.objects.filter(openid=self.request.auth.openid,
                                                        goods_code=str(data['goods_code'][j]),
                                                        is_delete=False).first()
                    goods_weight = round(goods_detail.goods_weight * int(data['goods_qty'][j]) / 1000, 4)
                    goods_volume = round(goods_detail.unit_volume * int(data['goods_qty'][j]), 4)
                    goods_cost = round(goods_detail.goods_cost * int(data['goods_qty'][j]), 2)
                    if stocklist.objects.filter(openid=self.request.auth.openid, goods_code=str(data['goods_code'][j])).exists():
                        goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                 goods_code=str(data['goods_code'][j])).first()
                        goods_qty_change.goods_qty = goods_qty_change.goods_qty + int(data['goods_qty'][j])
                        goods_qty_change.asn_stock = goods_qty_change.asn_stock + int(data['goods_qty'][j])
                        goods_qty_change.save()
                    else:
                        stocklist.objects.create(openid=self.request.auth.openid,
                                                 goods_code=str(data['goods_code'][j]),
                                                 goods_desc=goods_detail.goods_desc,
                                                 goods_qty=int(data['goods_qty'][j]),
                                                 asn_stock=int(data['goods_qty'][j]))
                    post_data = AsnDetailModel(openid=self.request.auth.openid,
                                               asn_code=str(data['asn_code']),
                                               supplier=str(data['supplier']),
                                               goods_code=str(data['goods_code'][j]),
                                               goods_desc=str(goods_detail.goods_desc),
                                               goods_qty=int(data['goods_qty'][j]),
                                               goods_weight=goods_weight,
                                               goods_volume=goods_volume,
                                               goods_cost=goods_cost,
                                               creater=str(staff_name))
                    post_data_list.append(post_data)
                    weight_list.append(goods_weight)
                    volume_list.append(goods_volume)
                    cost_list.append(goods_cost)
                total_weight = sumOfList(weight_list, len(weight_list))
                total_volume = sumOfList(volume_list, len(volume_list))
                total_cost = sumOfList(cost_list, len(cost_list))
                supplier_city = supplier.objects.filter(openid=self.request.auth.openid,
                                                        supplier_name=str(data['supplier']),
                                                        is_delete=False).first().supplier_city
                warehouse_city = warehouse.objects.filter(openid=self.request.auth.openid).first().warehouse_city
                transportation_fee = transportation.objects.filter(
                    Q(openid=self.request.auth.openid, send_city__icontains=supplier_city, receiver_city__icontains=warehouse_city,
                      is_delete=False) | Q(openid='init_data', send_city__icontains=supplier_city, receiver_city__icontains=warehouse_city,
                                           is_delete=False))
                transportation_res = {
                    "detail": []
                }
                if len(transportation_fee) >= 1:
                    transportation_list = []
                    for k in range(len(transportation_fee)):
                        transportation_cost = transportation_calculate(total_weight,
                                                                       total_volume,
                                                                       transportation_fee[k].weight_fee,
                                                                       transportation_fee[k].volume_fee,
                                                                       transportation_fee[k].min_payment)
                        transportation_detail = {
                            "transportation_supplier": transportation_fee[k].transportation_supplier,
                            "transportation_cost": transportation_cost
                        }
                        transportation_list.append(transportation_detail)
                    transportation_res['detail'] = transportation_list
                AsnDetailModel.objects.bulk_create(post_data_list, batch_size=100)
                AsnListModel.objects.filter(openid=self.request.auth.openid, asn_code=str(data['asn_code'])).update(
                    supplier=str(data['supplier']), total_weight=total_weight, total_volume=total_volume,
                    total_cost=total_cost, transportation_fee=transportation_res)
                return Response({"detail": "success"}, status=200)
            else:
                raise APIException({"detail": "Supplier does not exists"})
        else:
            raise APIException({"detail": "ASN Code does not exists"})

    def update(self, request, *args, **kwargs):
        data = self.request.data
        if AsnListModel.objects.filter(openid=self.request.auth.openid, asn_code=str(data['asn_code']),
                                       asn_status=1, is_delete=False).exists():
            if supplier.objects.filter(openid=self.request.auth.openid, supplier_name=str(data['supplier']),
                                       is_delete=False).exists():
                staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                                  id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
                for i in range(len(data['goods_code'])):
                    check_data = {
                        'openid': self.request.auth.openid,
                        'asn_code': str(data['asn_code']),
                        'supplier': str(data['supplier']),
                        'goods_code': str(data['goods_code'][i]),
                        'goods_qty': int(data['goods_qty'][i]),
                        'creater': str(staff_name)
                    }
                    serializer = self.get_serializer(data=check_data)
                    serializer.is_valid(raise_exception=True)
                asn_detail_list = AsnDetailModel.objects.filter(openid=self.request.auth.openid,
                                              asn_code=str(data['asn_code']), is_delete=False)
                for v in range(len(asn_detail_list)):
                    goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                goods_code=str(asn_detail_list[v].goods_code)).first()
                    goods_qty_change.goods_qty = goods_qty_change.goods_qty - asn_detail_list[v].goods_qty
                    if goods_qty_change.goods_qty < 0:
                        goods_qty_change.goods_qty = 0
                    goods_qty_change.asn_stock = goods_qty_change.asn_stock - asn_detail_list[v].goods_qty
                    if goods_qty_change.asn_stock < 0:
                        goods_qty_change.asn_stock = 0
                    goods_qty_change.save()
                    asn_detail_list[v].is_delete = True
                    asn_detail_list[v].save()
                post_data_list = []
                weight_list = []
                volume_list = []
                for j in range(len(data['goods_code'])):
                    goods_detail = goods.objects.filter(openid=self.request.auth.openid,
                                                        goods_code=str(data['goods_code'][j]),
                                                        is_delete=False).first()
                    goods_weight = round(goods_detail.goods_weight * int(data['goods_qty'][j]) / 1000, 4)
                    goods_volume = round(goods_detail.unit_volume * int(data['goods_qty'][j]), 4)
                    goods_cost = round(goods_detail.goods_cost * int(data['goods_qty'][j]), 2)
                    if stocklist.objects.filter(openid=self.request.auth.openid, goods_code=str(data['goods_code'][j])).exists():
                        goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                 goods_code=str(data['goods_code'][j])).first()
                        goods_qty_change.goods_qty = goods_qty_change.goods_qty + int(data['goods_qty'][j])
                        goods_qty_change.asn_stock = goods_qty_change.asn_stock + int(data['goods_qty'][j])
                        goods_qty_change.save()
                    else:
                        stocklist.objects.create(openid=self.request.auth.openid,
                                                 goods_code=str(data['goods_code'][j]),
                                                 goods_desc=goods_detail.goods_desc,
                                                 goods_qty=int(data['goods_qty'][j]),
                                                 asn_stock=int(data['goods_qty'][j]))
                    post_data = AsnDetailModel(openid=self.request.auth.openid,
                                               asn_code=str(data['asn_code']),
                                               supplier=str(data['supplier']),
                                               goods_code=str(data['goods_code'][j]),
                                               goods_desc=str(goods_detail.goods_desc),
                                               goods_qty=int(data['goods_qty'][j]),
                                               goods_weight=goods_weight,
                                               goods_volume=goods_volume,
                                               creater=str(staff_name))
                    post_data_list.append(post_data)
                    weight_list.append(goods_weight)
                    volume_list.append(goods_volume)
                total_weight = sumOfList(weight_list, len(weight_list))
                total_volume = sumOfList(volume_list, len(volume_list))
                supplier_city = supplier.objects.filter(openid=self.request.auth.openid,
                                                        supplier_name=str(data['supplier']),
                                                        is_delete=False).first().supplier_city
                warehouse_city = warehouse.objects.filter(openid=self.request.auth.openid).first().warehouse_city
                transportation_fee = transportation.objects.filter(
                    Q(openid=self.request.auth.openid, send_city__icontains=supplier_city,
                      receiver_city__icontains=warehouse_city,
                      is_delete=False) | Q(openid='init_data', send_city__icontains=supplier_city,
                                           receiver_city__icontains=warehouse_city,
                                           is_delete=False))
                transportation_res = {
                    "detail": []
                }
                if len(transportation_fee) >= 1:
                    transportation_list = []
                    for k in range(len(transportation_fee)):
                        transportation_cost = transportation_calculate(total_weight,
                                                                       total_volume,
                                                                       transportation_fee[k].weight_fee,
                                                                       transportation_fee[k].volume_fee,
                                                                       transportation_fee[k].min_payment)
                        transportation_detail = {
                            "transportation_supplier": transportation_fee[k].transportation_supplier,
                            "transportation_cost": transportation_cost
                        }
                        transportation_list.append(transportation_detail)
                    transportation_res['detail'] = transportation_list
                AsnDetailModel.objects.bulk_create(post_data_list, batch_size=100)
                AsnListModel.objects.filter(openid=self.request.auth.openid, asn_code=str(data['asn_code'])).update(
                    supplier=str(data['supplier']), total_weight=total_weight, total_volume=total_volume,
                    transportation_fee=transportation_res)
                return Response({"detail": "success"}, status=200)
            else:
                raise APIException({"detail": "Supplier does not exists"})
        else:
            raise APIException({"detail": "This ASN Status Is Not 1"})

class AsnViewPrintViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = AsnListFilter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return AsnListModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return AsnListModel.objects.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return AsnListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return serializers.ASNDetailGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def retrieve(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot update data which not yours"})
        else:
            context = {}
            asn_detail_list = AsnDetailModel.objects.filter(openid=self.request.auth.openid,
                                                            asn_code=qs.asn_code,
                                                            is_delete=False)
            asn_detail = serializers.ASNDetailGetSerializer(asn_detail_list, many=True)
            supplier_detail = supplier.objects.filter(openid=self.request.auth.openid,
                                                            supplier_name=qs.supplier).first()
            warehouse_detail = warehouse.objects.filter(openid=self.request.auth.openid,).first()
            context['asn_detail'] = asn_detail.data
            context['supplier_detail'] = {
                "supplier_name": supplier_detail.supplier_name,
                "supplier_city": supplier_detail.supplier_city,
                "supplier_address": supplier_detail.supplier_address,
                "supplier_contact": supplier_detail.supplier_contact
            }
            context['warehouse_detail'] = {
                "warehouse_name": warehouse_detail.warehouse_name,
                "warehouse_city": warehouse_detail.warehouse_city,
                "warehouse_address": warehouse_detail.warehouse_address,
                "warehouse_contact": warehouse_detail.warehouse_contact
            }
        return Response(context, status=200)

class AsnPreLoadViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = AsnListFilter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return AsnListModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return AsnListModel.objects.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return AsnListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.ASNListPartialUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot delete data which not yours"})
        else:
            if qs.asn_status == 1:
                if AsnDetailModel.objects.filter(openid=self.request.auth.openid, asn_code=qs.asn_code,
                                                                asn_status=1, is_delete=False).exists():
                    qs.asn_status = 2
                    asn_detail_list = AsnDetailModel.objects.filter(openid=self.request.auth.openid, asn_code=qs.asn_code,
                                                                    asn_status=1, is_delete=False)
                    for i in range(len(asn_detail_list)):
                        goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                    goods_code=str(asn_detail_list[i].goods_code)).first()
                        goods_qty_change.asn_stock = goods_qty_change.asn_stock - asn_detail_list[i].goods_qty
                        if goods_qty_change.asn_stock < 0:
                            goods_qty_change.asn_stock = 0
                        goods_qty_change.pre_load_stock = goods_qty_change.pre_load_stock + asn_detail_list[i].goods_qty
                        goods_qty_change.save()
                    asn_detail_list.update(asn_status=2)
                    qs.save()
                    serializer = self.get_serializer(qs, many=False)
                    headers = self.get_success_headers(serializer.data)
                    return Response(serializer.data, status=200, headers=headers)
                else:
                    raise APIException({"detail": "Please Enter The ASN Detail"})
            else:
                raise APIException({"detail": "This ASN Status Is Not 1"})

class AsnPreSortViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = AsnListFilter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return AsnListModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return AsnListModel.objects.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return AsnListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.ASNListUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot delete data which not yours"})
        else:
            if qs.asn_status == 2:
                qs.asn_status = 3
                asn_detail_list = AsnDetailModel.objects.filter(openid=self.request.auth.openid, asn_code=qs.asn_code,
                                                                asn_status=2, is_delete=False)
                for i in range(len(asn_detail_list)):
                    goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                goods_code=str(asn_detail_list[i].goods_code)).first()
                    goods_qty_change.pre_load_stock = goods_qty_change.pre_load_stock - asn_detail_list[i].goods_qty
                    if goods_qty_change.pre_load_stock < 0:
                        goods_qty_change.pre_load_stock = 0
                    goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock + asn_detail_list[i].goods_qty
                    goods_qty_change.save()
                asn_detail_list.update(asn_status=3)
                qs.save()
                serializer = self.get_serializer(qs, many=False)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=200, headers=headers)
            else:
                raise APIException({"detail": "This ASN Status Is Not 2"})

class AsnSortedViewSet(viewsets.ModelViewSet):
    """
        create:
            Finish Sorted

        update:
            All Sorted
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = AsnListFilter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return AsnListModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return AsnListModel.objects.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return AsnListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return serializers.ASNSortedPostSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, pk):
        qs = self.get_object()
        if qs.asn_status != 3:
            raise APIException({"detail": "This ASN Status Is Not 3"})
        else:
            data = self.request.data
            for j in range(len(data['goodsData'])):
                goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                            goods_code=str(
                                                                data['goodsData'][j].get('goods_code'))).first()
                asn_detail = AsnDetailModel.objects.filter(openid=self.request.auth.openid,
                                                           asn_code=str(data['asn_code']),
                                                           asn_status=3, supplier=str(data['supplier']),
                                                           goods_code=str(
                                                               data['goodsData'][j].get('goods_code'))).first()
                goods_detail = goods.objects.filter(openid=self.request.auth.openid,
                                                    goods_code=str(data['goodsData'][j].get('goods_code')),
                                                    is_delete=False).first()
                if int(data['goodsData'][j].get('goods_actual_qty')) == 0:
                    asn_detail.goods_actual_qty = int(data['goodsData'][j].get('goods_actual_qty'))
                    asn_detail.goods_shortage_qty = asn_detail.goods_qty
                    asn_detail.goods_cost = 0
                    qs.total_cost = qs.total_cost - (asn_detail.goods_shortage_qty * goods_detail.goods_cost)
                    goods_qty_change.goods_qty = goods_qty_change.goods_qty - asn_detail.goods_qty
                    goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - asn_detail.goods_qty
                    asn_detail.asn_status = 5
                    asn_detail.save()
                    goods_qty_change.save()
                    if goods_qty_change.goods_qty == 0 and goods_qty_change.back_order_stock == 0:
                        goods_qty_change.delete()
                else:
                    asn_detail.goods_actual_qty = int(data['goodsData'][j].get('goods_actual_qty'))
                    goods_qty_check = asn_detail.goods_qty - int(data['goodsData'][j].get('goods_actual_qty'))
                    if goods_qty_check > 0:
                        asn_detail.goods_shortage_qty = goods_qty_check
                        asn_detail.goods_more_qty = 0
                        asn_detail.goods_cost = asn_detail.goods_cost - (asn_detail.goods_shortage_qty * goods_detail.goods_cost)
                        qs.total_cost = qs.total_cost - (asn_detail.goods_shortage_qty * goods_detail.goods_cost)
                        goods_qty_change.goods_qty = goods_qty_change.goods_qty - goods_qty_check
                        goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - asn_detail.goods_qty
                        goods_qty_change.sorted_stock = goods_qty_change.sorted_stock + int(data['goodsData'][j].get('goods_actual_qty'))
                    elif goods_qty_check == 0:
                        asn_detail.goods_shortage_qty = 0
                        asn_detail.goods_more_qty = 0
                        goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - int(data['goodsData'][j].get('goods_actual_qty'))
                        goods_qty_change.sorted_stock = goods_qty_change.sorted_stock + int(data['goodsData'][j].get('goods_actual_qty'))
                    elif goods_qty_check < 0:
                        asn_detail.goods_shortage_qty = 0
                        asn_detail.goods_more_qty = abs(goods_qty_check)
                        asn_detail.goods_cost = asn_detail.goods_cost + (asn_detail.goods_more_qty * goods_detail.goods_cost)
                        qs.total_cost = qs.total_cost + (asn_detail.goods_more_qty * goods_detail.goods_cost)
                        goods_qty_change.goods_qty = goods_qty_change.goods_qty + abs(goods_qty_check)
                        goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - asn_detail.goods_qty
                        goods_qty_change.sorted_stock = goods_qty_change.sorted_stock + int(data['goodsData'][j].get('goods_actual_qty'))
                    asn_detail.asn_status = 4
                    asn_detail.save()
                    goods_qty_change.save()
                    if goods_qty_change.goods_qty == 0 and goods_qty_change.back_order_stock == 0:
                        goods_qty_change.delete()
            if AsnDetailModel.objects.filter(openid=self.request.auth.openid, asn_code=str(data['asn_code']),
                                                      asn_status=4, supplier=str(data['supplier'])).exists():
                qs.asn_status = 4
            else:
                qs.asn_status = 5
            qs.save()
            return Response({"detail": "success"}, status=200)

    def update(self, request, *args, **kwargs):
        data = self.request.data
        qs = self.get_queryset().filter(asn_code=data['asn_code']).first()
        if qs.asn_status != 3:
            raise APIException({"detail": "This ASN Status Is Not 3"})
        else:
            for j in range(len(data['goodsData'])):
                goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                            goods_code=str(
                                                                data['goodsData'][j].get('goods_code'))).first()
                asn_detail = AsnDetailModel.objects.filter(openid=self.request.auth.openid,
                                                           asn_code=str(data['asn_code']),
                                                           goods_code=str(
                                                               data['goodsData'][j].get('goods_code'))).first()
                goods_detail = goods.objects.filter(openid=self.request.auth.openid,
                                                    goods_code=str(data['goodsData'][j].get('goods_code')),
                                                    is_delete=False).first()
                if int(data['goodsData'][j].get('goods_actual_qty')) == 0:
                    asn_detail.goods_actual_qty = int(data['goodsData'][j].get('goods_actual_qty'))
                    asn_detail.goods_shortage_qty = asn_detail.goods_qty
                    asn_detail.goods_cost = 0
                    qs.total_cost = qs.total_cost - (asn_detail.goods_shortage_qty * goods_detail.goods_cost)
                    goods_qty_change.goods_qty = goods_qty_change.goods_qty - asn_detail.goods_qty
                    goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - asn_detail.goods_qty
                    asn_detail.asn_status = 5
                    asn_detail.save()
                    goods_qty_change.save()
                    if goods_qty_change.goods_qty == 0 and goods_qty_change.back_order_stock == 0:
                        goods_qty_change.delete()
                else:
                    asn_detail.goods_actual_qty = int(data['goodsData'][j].get('goods_actual_qty'))
                    goods_qty_check = asn_detail.goods_qty - int(data['goodsData'][j].get('goods_actual_qty'))
                    if goods_qty_check > 0:
                        asn_detail.goods_shortage_qty = goods_qty_check
                        asn_detail.goods_more_qty = 0
                        asn_detail.goods_cost = asn_detail.goods_cost - (asn_detail.goods_shortage_qty * goods_detail.goods_cost)
                        qs.total_cost = qs.total_cost - (asn_detail.goods_shortage_qty * goods_detail.goods_cost)
                        goods_qty_change.goods_qty = goods_qty_change.goods_qty - goods_qty_check
                        goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - asn_detail.goods_qty
                        goods_qty_change.sorted_stock = goods_qty_change.sorted_stock + int(data['goodsData'][j].get('goods_actual_qty'))
                    elif goods_qty_check == 0:
                        asn_detail.goods_shortage_qty = 0
                        asn_detail.goods_more_qty = 0
                        goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - int(data['goodsData'][j].get('goods_actual_qty'))
                        goods_qty_change.sorted_stock = goods_qty_change.sorted_stock + int(data['goodsData'][j].get('goods_actual_qty'))
                    elif goods_qty_check < 0:
                        asn_detail.goods_shortage_qty = 0
                        asn_detail.goods_more_qty = abs(goods_qty_check)
                        asn_detail.goods_cost = asn_detail.goods_cost + (asn_detail.goods_more_qty * goods_detail.goods_cost)
                        qs.total_cost = qs.total_cost + (asn_detail.goods_more_qty * goods_detail.goods_cost)
                        goods_qty_change.goods_qty = goods_qty_change.goods_qty + abs(goods_qty_check)
                        goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - asn_detail.goods_qty
                        goods_qty_change.sorted_stock = goods_qty_change.sorted_stock + int(data['goodsData'][j].get('goods_actual_qty'))
                    asn_detail.asn_status = 4
                    asn_detail.save()
                    goods_qty_change.save()
                    if goods_qty_change.goods_qty == 0 and goods_qty_change.back_order_stock == 0:
                        goods_qty_change.delete()
            if AsnDetailModel.objects.filter(openid=self.request.auth.openid, asn_code=str(data['asn_code']),
                                                      asn_status=4).exists():
                qs.asn_status = 4
            else:
                qs.asn_status = 5
            qs.save()
            return Response({"detail": "success"}, status=200)

class MoveToBinViewSet(viewsets.ModelViewSet):
    """
        create:
            Create a data line（post）
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = AsnDetailFilter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return AsnDetailModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return AsnDetailModel.objects.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return AsnDetailModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return serializers.ASNDetailGetSerializer
        elif self.action in ['create', 'update']:
            return serializers.MoveToBinSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot delete data which not yours"})
        else:
            if qs.asn_status != 4:
                raise APIException({"detail": "This ASN Status Is Not 4"})
            else:
                data = self.request.data
                if 'bin_name' not in data:
                    raise APIException({"detail": "Please Enter the Bin Name"})
                else:
                    bin_detail = binset.objects.filter(openid=self.request.auth.openid,
                                                       bin_name=str(data['bin_name'])).first()
                    asn_detail = AsnListModel.objects.filter(openid=self.request.auth.openid,
                                                             asn_code=str(data['asn_code'])).first()
                    goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                goods_code=str(data['goods_code'])).first()
                    if int(data['qty']) <= 0:
                        raise APIException({"detail": "Move QTY Must > 0"})
                    else:
                        staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                                          id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
                        move_qty = qs.goods_actual_qty - qs.sorted_qty - int(data['qty'])
                        if move_qty > 0:
                            qs.sorted_qty = qs.sorted_qty + int(data['qty'])
                            goods_qty_change.sorted_stock = goods_qty_change.sorted_stock - int(data['qty'])
                            goods_qty_change.onhand_stock = goods_qty_change.onhand_stock + int(data['qty'])
                            if bin_detail.bin_property == 'Damage':
                                goods_qty_change.damage_stock = goods_qty_change.damage_stock + int(data['qty'])
                                qs.goods_damage_qty = qs.goods_damage_qty + int(data['qty'])
                            elif bin_detail.bin_property == 'Inspection':
                                goods_qty_change.inspect_stock = goods_qty_change.inspect_stock + int(data['qty'])
                            elif bin_detail.bin_property == 'Holding':
                                goods_qty_change.hold_stock = goods_qty_change.hold_stock + int(data['qty'])
                            else:
                                goods_qty_change.can_order_stock = goods_qty_change.can_order_stock + int(data['qty'])
                            qs.save()
                            goods_qty_change.save()
                            stockbin.objects.create(openid=self.request.auth.openid,
                                                    bin_name=str(data['bin_name']),
                                                    goods_code=str(data['goods_code']),
                                                    goods_desc=goods_qty_change.goods_desc,
                                                    goods_qty=int(data['qty']),
                                                    bin_size=bin_detail.bin_size,
                                                    bin_property=bin_detail.bin_property,
                                                    t_code=Md5.md5(str(data['goods_code'])),
                                                    create_time=qs.create_time
                                                    )
                            qtychangerecorder.objects.create(openid=self.request.auth.openid,
                                                             mode_code=qs.asn_code,
                                                             bin_name=str(data['bin_name']),
                                                             goods_code=str(data['goods_code']),
                                                             goods_qty=int(data['qty']),
                                                             creater=str(staff_name)
                                                             )
                            cur_date = timezone.now().date()
                            line_data = cyclecount.objects.filter(openid=self.request.auth.openid,
                                                                  bin_name=str(data['bin_name']),
                                                                  goods_code=str(data['goods_code']),
                                                                  create_time__gte=cur_date)
                            bin_check = stockbin.objects.filter(openid=self.request.auth.openid,
                                                                bin_name=str(data['bin_name']),
                                                                goods_code=str(data['goods_code']),
                                                                )
                            if bin_check.exists():
                                bin_stock = bin_check.aggregate(sum=Sum('goods_qty'))["sum"]
                            else:
                                bin_stock = 0
                            if line_data.exists():
                                line_data.goods_qty = bin_stock + int(data['qty'])
                                line_data.update(goods_qty=line_data.goods_qty)
                            else:
                                cyclecount.objects.create(openid=self.request.auth.openid,
                                                          bin_name=str(data['bin_name']),
                                                          goods_code=str(data['goods_code']),
                                                          goods_qty=int(data['qty']),
                                                          creater=str(staff_name)
                                                          )
                            if bin_detail.empty_label == True:
                                bin_detail.empty_label = False
                                bin_detail.save()
                        elif move_qty == 0:
                            qs.sorted_qty = qs.sorted_qty + int(data['qty'])
                            qs.asn_status = 5
                            goods_qty_change.sorted_stock = goods_qty_change.sorted_stock - int(data['qty'])
                            goods_qty_change.onhand_stock = goods_qty_change.onhand_stock + int(data['qty'])
                            if bin_detail.bin_property == 'Damage':
                                goods_qty_change.damage_stock = goods_qty_change.damage_stock + int(data['qty'])
                                qs.goods_damage_qty = qs.goods_damage_qty + int(data['qty'])
                            elif bin_detail.bin_property == 'Inspection':
                                goods_qty_change.inspect_stock = goods_qty_change.inspect_stock + int(data['qty'])
                            elif bin_detail.bin_property == 'Holding':
                                goods_qty_change.hold_stock = goods_qty_change.hold_stock + int(data['qty'])
                            else:
                                goods_qty_change.can_order_stock = goods_qty_change.can_order_stock + int(data['qty'])
                            qtychangerecorder.objects.create(openid=self.request.auth.openid,
                                                             mode_code=qs.asn_code,
                                                             bin_name=str(data['bin_name']),
                                                             goods_code=str(data['goods_code']),
                                                             goods_qty=int(data['qty']),
                                                             creater=str(staff_name)
                                                             )
                            cur_date = timezone.now().date()
                            line_data = cyclecount.objects.filter(openid=self.request.auth.openid,
                                                                  bin_name=str(data['bin_name']),
                                                                  goods_code=str(data['goods_code']),
                                                                  create_time__gte=cur_date)
                            bin_check = stockbin.objects.filter(openid=self.request.auth.openid,
                                                                bin_name=str(data['bin_name']),
                                                                goods_code=str(data['goods_code']),
                                                                )
                            if bin_check.exists():
                                bin_stock = bin_check.aggregate(sum=Sum('goods_qty'))["sum"]
                            else:
                                bin_stock = 0
                            if line_data.exists():
                                line_data.goods_qty = bin_stock + int(data['qty'])
                                line_data.update(goods_qty=line_data.goods_qty)
                            else:
                                cyclecount.objects.create(openid=self.request.auth.openid,
                                                          bin_name=str(data['bin_name']),
                                                          goods_code=str(data['goods_code']),
                                                          goods_qty=int(data['qty']),
                                                          creater=str(staff_name),
                                                          t_code=Md5.md5(str(data['bin_name']))
                                                          )
                            qs.save()
                            goods_qty_change.save()
                            if AsnDetailModel.objects.filter(openid=self.request.auth.openid,
                                                             asn_code=str(data['asn_code']),
                                                             asn_status=4
                                                             ).exists():
                                pass
                            else:
                                asn_detail.asn_status = 5
                                asn_detail.save()
                            stockbin.objects.create(openid=self.request.auth.openid,
                                                    bin_name=str(data['bin_name']),
                                                    goods_code=str(data['goods_code']),
                                                    goods_desc=goods_qty_change.goods_desc,
                                                    goods_qty=int(data['qty']),
                                                    bin_size=bin_detail.bin_size,
                                                    bin_property=bin_detail.bin_property,
                                                    t_code=Md5.md5(str(data['goods_code'])),
                                                    create_time=qs.create_time)
                            if bin_detail.empty_label == True:
                                bin_detail.empty_label = False
                                bin_detail.save()
                        elif move_qty < 0:
                            raise APIException({"detail": "Move Qty must < Actual Arrive Qty"})
                        return Response({"detail": "success"}, status=200)

    def update(self, request, *args, **kwargs):
        data = self.request.data
        qs_list = self.get_queryset().filter(asn_code=data['asn_code'])
        if qs_list[0].openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot delete data which not yours"})
        else:
            if 'bin_name' not in data:
                raise APIException({"detail": "Please Enter the Bin Name"})
            else:
                bin_detail = binset.objects.filter(openid=self.request.auth.openid,
                                                   bin_name=str(data['bin_name'])).first()
                asn_detail = AsnListModel.objects.filter(openid=self.request.auth.openid,
                                                         asn_code=str(data['asn_code'])
                                                         ).first()
                staff_name = staff.objects.filter(openid=self.request.auth.openid,
                                                  id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
                for i in range(len(data['res_data'])):
                    goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                goods_code=str(data['res_data'][i]['goods_code'])).first()
                    if int(data['res_data'][i]['qty']) <= 0:
                        continue
                    else:
                        qs = qs_list.filter(goods_code=str(data['res_data'][i]['goods_code'])).first()
                        move_qty = qs.goods_actual_qty - qs.sorted_qty - int(data['res_data'][i]['qty'])
                        if move_qty > 0:
                            qs.sorted_qty = qs.sorted_qty + int(data['res_data'][i]['qty'])
                            goods_qty_change.sorted_stock = goods_qty_change.sorted_stock - int(data['res_data'][i]['qty'])
                            goods_qty_change.onhand_stock = goods_qty_change.onhand_stock + int(data['res_data'][i]['qty'])
                            if bin_detail.bin_property == 'Damage':
                                goods_qty_change.damage_stock = goods_qty_change.damage_stock + int(data['res_data'][i]['qty'])
                                qs.goods_damage_qty = qs.goods_damage_qty + int(data['res_data'][i]['qty'])
                            elif bin_detail.bin_property == 'Inspection':
                                goods_qty_change.inspect_stock = goods_qty_change.inspect_stock + int(data['res_data'][i]['qty'])
                            elif bin_detail.bin_property == 'Holding':
                                goods_qty_change.hold_stock = goods_qty_change.hold_stock + int(data['res_data'][i]['qty'])
                            else:
                                goods_qty_change.can_order_stock = goods_qty_change.can_order_stock + int(data['res_data'][i]['qty'])
                            qs.save()
                            goods_qty_change.save()
                            stockbin.objects.create(openid=self.request.auth.openid,
                                                    bin_name=str(data['bin_name']),
                                                    goods_code=str(data['res_data'][i]['goods_code']),
                                                    goods_desc=goods_qty_change.goods_desc,
                                                    goods_qty=int(data['res_data'][i]['qty']),
                                                    bin_size=bin_detail.bin_size,
                                                    bin_property=bin_detail.bin_property,
                                                    t_code=Md5.md5(str(data['res_data'][i]['goods_code'])),
                                                    create_time=qs.create_time
                                                    )
                            qtychangerecorder.objects.create(openid=self.request.auth.openid,
                                                             mode_code=qs.asn_code,
                                                             bin_name=str(data['bin_name']),
                                                             goods_code=str(data['res_data'][i]['goods_code']),
                                                             goods_qty=int(data['res_data'][i]['qty']),
                                                             creater=str(staff_name)
                                                             )
                            cur_date = timezone.now().date()
                            line_data = cyclecount.objects.filter(openid=self.request.auth.openid,
                                                                  bin_name=str(data['bin_name']),
                                                                  goods_code=str(data['res_data'][i]['goods_code']),
                                                                  create_time__gte=cur_date)
                            bin_check = stockbin.objects.filter(openid=self.request.auth.openid,
                                                                bin_name=str(data['bin_name']),
                                                                goods_code=str(data['res_data'][i]['goods_code']),
                                                                )
                            if bin_check.exists():
                                bin_stock = bin_check.aggregate(sum=Sum('goods_qty'))["sum"]
                            else:
                                bin_stock = 0
                            if line_data.exists():
                                line_data.goods_qty = bin_stock + int(data['res_data'][i]['qty'])
                                line_data.update(goods_qty=line_data.goods_qty)
                            else:
                                cyclecount.objects.create(openid=self.request.auth.openid,
                                                          bin_name=str(data['bin_name']),
                                                          goods_code=str(data['res_data'][i]['goods_code']),
                                                          goods_qty=int(data['res_data'][i]['qty']),
                                                          creater=str(staff_name)
                                                          )
                            if bin_detail.empty_label == True:
                                bin_detail.empty_label = False
                                bin_detail.save()
                        elif move_qty == 0:
                            qs.sorted_qty = qs.sorted_qty + int(data['res_data'][i]['qty'])
                            qs.asn_status = 5
                            goods_qty_change.sorted_stock = goods_qty_change.sorted_stock - int(data['res_data'][i]['qty'])
                            goods_qty_change.onhand_stock = goods_qty_change.onhand_stock + int(data['res_data'][i]['qty'])
                            if bin_detail.bin_property == 'Damage':
                                goods_qty_change.damage_stock = goods_qty_change.damage_stock + int(data['res_data'][i]['qty'])
                                qs.goods_damage_qty = qs.goods_damage_qty + int(data['res_data'][i]['qty'])
                            elif bin_detail.bin_property == 'Inspection':
                                goods_qty_change.inspect_stock = goods_qty_change.inspect_stock + int(data['res_data'][i]['qty'])
                            elif bin_detail.bin_property == 'Holding':
                                goods_qty_change.hold_stock = goods_qty_change.hold_stock + int(data['res_data'][i]['qty'])
                            else:
                                goods_qty_change.can_order_stock = goods_qty_change.can_order_stock + int(data['res_data'][i]['qty'])
                            qtychangerecorder.objects.create(openid=self.request.auth.openid,
                                                             mode_code=qs.asn_code,
                                                             bin_name=str(data['bin_name']),
                                                             goods_code=str(data['res_data'][i]['goods_code']),
                                                             goods_qty=int(data['res_data'][i]['qty']),
                                                             creater=str(staff_name)
                                                             )
                            cur_date = timezone.now().date()
                            line_data = cyclecount.objects.filter(openid=self.request.auth.openid,
                                                                  bin_name=str(data['bin_name']),
                                                                  goods_code=str(data['res_data'][i]['goods_code']),
                                                                  create_time__gte=cur_date)
                            bin_check = stockbin.objects.filter(openid=self.request.auth.openid,
                                                                bin_name=str(data['bin_name']),
                                                                goods_code=str(data['res_data'][i]['goods_code']),
                                                                )
                            if bin_check.exists():
                                bin_stock = bin_check.aggregate(sum=Sum('goods_qty'))["sum"]
                            else:
                                bin_stock = 0
                            if line_data.exists():
                                line_data.goods_qty = bin_stock + int(data['res_data'][i]['qty'])
                                line_data.update(goods_qty=line_data.goods_qty)
                            else:
                                cyclecount.objects.create(openid=self.request.auth.openid,
                                                          bin_name=str(data['bin_name']),
                                                          goods_code=str(data['res_data'][i]['goods_code']),
                                                          goods_qty=int(data['res_data'][i]['qty']),
                                                          creater=str(staff_name),
                                                          t_code=Md5.md5(str(data['bin_name']))
                                                          )
                            qs.save()
                            goods_qty_change.save()
                            if AsnDetailModel.objects.filter(openid=self.request.auth.openid,
                                                             asn_code=str(data['asn_code']),
                                                             asn_status=4
                                                             ).exists():
                                pass
                            else:
                                asn_detail.asn_status = 5
                                asn_detail.save()
                            stockbin.objects.create(openid=self.request.auth.openid,
                                                    bin_name=str(data['bin_name']),
                                                    goods_code=str(data['res_data'][i]['goods_code']),
                                                    goods_desc=goods_qty_change.goods_desc,
                                                    goods_qty=int(data['res_data'][i]['qty']),
                                                    bin_size=bin_detail.bin_size,
                                                    bin_property=bin_detail.bin_property,
                                                    t_code=Md5.md5(str(data['res_data'][i]['goods_code'])),
                                                    create_time=qs.create_time)
                            if bin_detail.empty_label == True:
                                bin_detail.empty_label = False
                                bin_detail.save()
                return Response({"detail": "success"}, status=200)

class FileListDownloadView(viewsets.ModelViewSet):
    renderer_classes = (FileListRenderCN, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = AsnListFilter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            empty_qs = AsnListModel.objects.filter(
                Q(openid=self.request.auth.openid, asn_status=1, is_delete=False) & Q(supplier=''))
            cur_date = timezone.now()
            date_check = relativedelta(day=1)
            if len(empty_qs) > 0:
                for i in range(len(empty_qs)):
                    if empty_qs[i].create_time <= cur_date - date_check:
                        empty_qs[i].delete()
            if id is None:
                return AsnListModel.objects.filter(
                    Q(openid=self.request.auth.openid, is_delete=False) & ~Q(supplier=''))
            else:
                return AsnListModel.objects.filter(
                    Q(openid=self.request.auth.openid, id=id, is_delete=False) & ~Q(supplier=''))
        else:
            return AsnListModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.FileListRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def get_lang(self, data):
        lang = self.request.META.get('HTTP_LANGUAGE')
        if lang:
            if lang == 'zh-hans':
                return FileListRenderCN().render(data)
            else:
                return FileListRenderEN().render(data)
        else:
            return FileListRenderEN().render(data)

    def list(self, request, *args, **kwargs):
        from datetime import datetime
        dt = datetime.now()
        data = (
            FileListRenderSerializer(instance).data
            for instance in self.filter_queryset(self.get_queryset())
        )
        renderer = self.get_lang(data)
        response = StreamingHttpResponse(
            renderer,
            content_type="text/csv"
        )
        response['Content-Disposition'] = "attachment; filename='asnlist_{}.csv'".format(str(dt.strftime('%Y%m%d%H%M%S%f')))
        return response

class FileDetailDownloadView(viewsets.ModelViewSet):
    serializer_class = serializers.FileDetailRenderSerializer
    renderer_classes = (FileDetailRenderCN, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = AsnDetailFilter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return AsnDetailModel.objects.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return AsnDetailModel.objects.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return AsnDetailModel.objects.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.FileDetailRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def get_lang(self, data):
        lang = self.request.META.get('HTTP_LANGUAGE')
        if lang:
            if lang == 'zh-hans':
                return FileDetailRenderCN().render(data)
            else:
                return FileDetailRenderEN().render(data)
        else:
            return FileDetailRenderEN().render(data)

    def list(self, request, *args, **kwargs):
        from datetime import datetime
        dt = datetime.now()
        data = (
            FileDetailRenderSerializer(instance).data
            for instance in self.filter_queryset(self.get_queryset())
        )
        renderer = self.get_lang(data)
        response = StreamingHttpResponse(
            renderer,
            content_type="text/csv"
        )
        response['Content-Disposition'] = "attachment; filename='asndetail_{}.csv'".format(str(dt.strftime('%Y%m%d%H%M%S%f')))
        return response
