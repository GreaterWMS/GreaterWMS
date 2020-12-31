from rest_framework import viewsets
from .models import DnListModel, DnDetailModel, PickingListModel
from . import serializers
from .page import MyPageNumberPaginationDNList
from utils.page import MyPageNumberPagination
from utils.datasolve import sumOfList, transportation_calculate
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import DnListFilter, DnDetailFilter
from rest_framework.exceptions import APIException
from customer.models import ListModel as customer
from warehouse.models import ListModel as warehouse
from goods.models import ListModel as goods
from payment.models import TransportationFeeListModel as transportation
from stock.models import StockListModel as stocklist
from stock.models import StockBinModel as stockbin
from binset.models import ListModel as binset
from django.db.models import Q
import re

class DnListViewSet(viewsets.ModelViewSet):
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
    queryset = DnListModel.objects.all()
    serializer_class = serializers.DNListGetSerializer
    pagination_class = MyPageNumberPaginationDNList
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = DnListFilter

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
                return self.queryset.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.DNListGetSerializer
        elif self.action == 'retrieve':
            return serializers.DNListGetSerializer
        elif self.action == 'create':
            return serializers.DNListPostSerializer
        elif self.action == 'update':
            return serializers.DNListUpdateSerializer
        elif self.action == 'partial_update':
            return serializers.DNListPartialUpdateSerializer
        elif self.action == 'destroy':
            return serializers.DNListGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['openid'] = self.request.auth.openid
        if self.queryset.filter(openid=data['openid'], is_delete=False).exists():
            dn_last_code = self.queryset.filter(openid=data['openid']).first().dn_code
            dn_add_code = str(int(re.findall(r'\d+', str(dn_last_code), re.IGNORECASE)[0]) + 1).zfill(8)
            data['dn_code'] = 'DN' + dn_add_code
        else:
            data['dn_code'] = 'DN00000001'
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=200, headers=headers)

    def destroy(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot delete data which not yours"})
        else:
            if qs.dn_status == 1:
                qs.is_delete = True
                dn_detail_list = DnDetailModel.objects.filter(openid=self.request.auth.openid, dn_code=qs.dn_code,
                                              dn_status=1, is_delete=False)
                for i in range(len(dn_detail_list)):
                    goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                goods_code=str(dn_detail_list[i].goods_code)).first()
                    goods_qty_change.dn_stock = goods_qty_change.dn_stock - int(dn_detail_list[i].goods_qty)
                    goods_qty_change.save()
                dn_detail_list.update(is_delete=True)
                qs.save()
                serializer = self.get_serializer(qs, many=False)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=200, headers=headers)
            else:
                raise APIException({"detail": "This order has Confirmed or Deliveried"})

class DnDetailViewSet(viewsets.ModelViewSet):
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
    queryset = DnDetailModel.objects.all()
    serializer_class = serializers.DNDetailGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = DnDetailFilter

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
                return self.queryset.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.DNDetailGetSerializer
        elif self.action == 'retrieve':
            return serializers.DNDetailGetSerializer
        elif self.action == 'create':
            return serializers.DNDetailPostSerializer
        elif self.action == 'update':
            return serializers.DNDetailUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = request.data
        if DnListModel.objects.filter(openid=self.request.auth.openid, dn_code=str(data['dn_code']), is_delete=False).exists():
            if customer.objects.filter(openid=self.request.auth.openid, customer_name=str(data['customer']), is_delete=False).exists():
                for i in range(len(data['goods_code'])):
                    check_data = {
                        'openid': self.request.auth.openid,
                        'dn_code': str(data['dn_code']),
                        'customer': str(data['customer']),
                        'goods_code': str(data['goods_code'][i]),
                        'goods_qty': int(data['goods_qty'][i]),
                        'creater': str(data['creater'])
                    }
                    serializer = self.get_serializer(data=check_data)
                    serializer.is_valid(raise_exception=True)
                post_data_list = []
                weight_list = []
                volume_list = []
                for j in range(len(data['goods_code'])):
                    goods_detail = goods.objects.filter(openid=self.request.auth.openid,
                                                        goods_code=str(data['goods_code'][j]),
                                                        is_delete=False).first()
                    goods_weight = round(goods_detail.goods_weight * int(data['goods_qty'][j]) / 1000, 8)
                    goods_volume = round(goods_detail.unit_volume * int(data['goods_qty'][j]), 8)
                    if stocklist.objects.filter(openid=self.request.auth.openid, goods_code=str(data['goods_code'][j]),
                                                can_order_stock__gte=0).exists():
                        goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                    goods_code=str(data['goods_code'][j])).first()
                        goods_qty_change.dn_stock = goods_qty_change.dn_stock + int(data['goods_qty'][j])
                        goods_qty_change.save()
                    else:
                        stocklist.objects.create(openid=self.request.auth.openid,
                                                 goods_code=str(data['goods_code'][j]),
                                                 goods_desc=goods_detail.goods_desc,
                                                 dn_stock=int(data['goods_qty'][j]))
                    post_data = DnDetailModel(openid=self.request.auth.openid,
                                              dn_code=str(data['dn_code']),
                                              customer=str(data['customer']),
                                              goods_code=str(data['goods_code'][j]),
                                              goods_qty=int(data['goods_qty'][j]),
                                              goods_weight=goods_weight,
                                              goods_volume=goods_volume,
                                              creater=str(data['creater']))
                    weight_list.append(goods_weight)
                    volume_list.append(goods_volume)
                    post_data_list.append(post_data)
                total_weight = sumOfList(weight_list, len(weight_list))
                total_volume = sumOfList(volume_list, len(volume_list))
                customer_city = customer.objects.filter(openid=self.request.auth.openid,
                                                        customer_name=str(data['customer']),
                                                        is_delete=False).first().customer_city
                warehouse_city = warehouse.objects.filter(openid=self.request.auth.openid).first().warehouse_city
                transportation_fee = transportation.objects.filter(
                    Q(openid=self.request.auth.openid, send_city__icontains=warehouse_city, receiver_city__icontains=customer_city,
                      is_delete=False) | Q(openid='init_data', send_city__icontains=warehouse_city, receiver_city__icontains=customer_city,
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
                DnDetailModel.objects.bulk_create(post_data_list, batch_size=100)
                DnListModel.objects.filter(openid=self.request.auth.openid, dn_code=str(data['dn_code'])).update(
                    customer=str(data['customer']), total_weight=total_weight, total_volume=total_volume,
                    transportation_fee=transportation_res)
                return Response({"success": "Yes"}, status=200)
            else:
                raise APIException({"detail": "customer does not exists"})
        else:
            raise APIException({"detail": "DN Code does not exists"})

    def update(self, request, *args, **kwargs):
        data = request.data
        if DnListModel.objects.filter(openid=self.request.auth.openid, dn_code=str(data['dn_code']),
                                       dn_status=1, is_delete=False).exists():
            if customer.objects.filter(openid=self.request.auth.openid, customer_name=str(data['customer']),
                                       is_delete=False).exists():
                for i in range(len(data['goods_code'])):
                    check_data = {
                        'openid': self.request.auth.openid,
                        'dn_code': str(data['dn_code']),
                        'customer': str(data['customer']),
                        'goods_code': str(data['goods_code'][i]),
                        'goods_qty': int(data['goods_qty'][i]),
                        'creater': str(data['creater'])
                    }
                    serializer = self.get_serializer(data=check_data)
                    serializer.is_valid(raise_exception=True)
                dn_detail_list = DnDetailModel.objects.filter(openid=self.request.auth.openid,
                                              dn_code=str(data['dn_code']))
                for v in range(len(dn_detail_list)):
                    goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                goods_code=str(dn_detail_list[v].goods_code)).first()
                    goods_qty_change.dn_stock = goods_qty_change.dn_stock - dn_detail_list[v].goods_qty
                    if goods_qty_change.dn_stock < 0:
                        goods_qty_change.dn_stock = 0
                    goods_qty_change.save()
                dn_detail_list.is_delete = True
                dn_detail_list.save()
                post_data_list = []
                weight_list = []
                volume_list = []
                for j in range(len(data['goods_code'])):
                    goods_detail = goods.objects.filter(openid=self.request.auth.openid,
                                                        goods_code=str(data['goods_code'][j]),
                                                        is_delete=False).first()
                    goods_weight = round(goods_detail.goods_weight * int(data['goods_qty'][j]) / 1000, 8)
                    goods_volume = round(goods_detail.unit_volume * int(data['goods_qty'][j]), 8)
                    if stocklist.objects.filter(openid=self.request.auth.openid, goods_code=str(data['goods_code'][j]),
                                                can_order_stock__gt=0).exists():
                        goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                    goods_code=str(data['goods_code'][j])).first()
                        goods_qty_change.dn_stock = goods_qty_change.dn_stock + int(data['goods_qty'][j])
                        goods_qty_change.save()
                    else:
                        stocklist.objects.create(openid=self.request.auth.openid,
                                                 goods_code=str(data['goods_code'][j]),
                                                 goods_desc=goods_detail.goods_desc,
                                                 dn_stock=int(data['goods_qty'][j]))
                    post_data = DnDetailModel(openid=self.request.auth.openid,
                                              dn_code=str(data['dn_code']),
                                              customer=str(data['customer']),
                                              goods_code=str(data['goods_code'][j]),
                                              goods_qty=int(data['goods_qty'][j]),
                                              goods_weight=goods_weight,
                                              goods_volume=goods_volume,
                                              creater=str(data['creater']))
                    weight_list.append(goods_weight)
                    volume_list.append(goods_volume)
                    post_data_list.append(post_data)
                total_weight = sumOfList(weight_list, len(weight_list))
                total_volume = sumOfList(volume_list, len(volume_list))
                customer_city = customer.objects.filter(openid=self.request.auth.openid,
                                                        customer_name=str(data['customer']),
                                                        is_delete=False).first().customer_city
                warehouse_city = warehouse.objects.filter(openid=self.request.auth.openid).first().warehouse_city
                transportation_fee = transportation.objects.filter(
                    Q(openid=self.request.auth.openid, send_city__icontains=warehouse_city,
                      receiver_city__icontains=customer_city,
                      is_delete=False) | Q(openid='init_data', send_city__icontains=warehouse_city,
                                           receiver_city__icontains=customer_city,
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
                DnDetailModel.objects.bulk_create(post_data_list, batch_size=100)
                DnListModel.objects.filter(openid=self.request.auth.openid, dn_code=str(data['dn_code'])).update(
                    customer=str(data['customer']), total_weight=total_weight, total_volume=total_volume,
                    transportation_fee=transportation_res)
                return Response({"success": "Yes"}, status=200)
            else:
                raise APIException({"detail": "Customer does not exists"})
        else:
            raise APIException({"detail": "DN Code has been Confirmed or does not exists"})

class DnViewPrintViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）
    """
    queryset = DnListModel.objects.all()
    serializer_class = serializers.DNListGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = DnListFilter

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
                return self.queryset.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.DNDetailGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def retrieve(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot update data which not yours"})
        else:
            context = {}
            dn_detail_list = DnDetailModel.objects.filter(openid=self.request.auth.openid,
                                                            dn_code=qs.dn_code)
            dn_detail = serializers.DNDetailGetSerializer(dn_detail_list, many=True)
            customer_detail = customer.objects.filter(openid=self.request.auth.openid,
                                                            customer_name=qs.customer).first()
            warehouse_detail = warehouse.objects.filter(openid=self.request.auth.openid,).first()
            context['dn_detail'] = dn_detail.data
            context['customer_detail'] = {
                "customer_name": customer_detail.customer_name,
                "customer_city": customer_detail.customer_city,
                "customer_address": customer_detail.customer_address,
                "customer_contact": customer_detail.customer_contact
            }
            context['warehouse_detail'] = {
                "warehouse_name": warehouse_detail.warehouse_name,
                "warehouse_city": warehouse_detail.warehouse_city,
                "warehouse_address": warehouse_detail.warehouse_address,
                "warehouse_contact": warehouse_detail.warehouse_contact
            }
        return Response(context, status=200)

class DnNewOrderViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）
    """
    queryset = DnListModel.objects.all()
    serializer_class = serializers.DNListGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = DnListFilter

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
                return self.queryset.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.DNListPartialUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot delete data which not yours"})
        else:
            if qs.dn_status == 1:
                qs.dn_status = 2
                dn_detail_list = DnDetailModel.objects.filter(openid=self.request.auth.openid, dn_code=qs.dn_code,
                                                                dn_status=1, is_delete=False)
                for i in range(len(dn_detail_list)):
                    goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                goods_code=str(dn_detail_list[i].goods_code)).first()
                    goods_qty_change.can_order_stock = goods_qty_change.can_order_stock - dn_detail_list[i].goods_qty
                    goods_qty_change.ordered_stock = goods_qty_change.ordered_stock + dn_detail_list[i].goods_qty
                    goods_qty_change.dn_stock = goods_qty_change.dn_stock - dn_detail_list[i].goods_qty
                    if goods_qty_change.can_order_stock < 0:
                        goods_qty_change.can_order_stock = 0
                    goods_qty_change.save()
                dn_detail_list.update(dn_status=2)
                qs.save()
                serializer = self.get_serializer(qs, many=False)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=200, headers=headers)
            else:
                raise APIException({"detail": "This order has deliveried"})

class DnOrderReleaseViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）
    """
    queryset = DnListModel.objects.all()
    serializer_class = serializers.DNListGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = DnListFilter

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
                return self.queryset.filter(openid=self.request.auth.openid, dn_status=2, is_delete=False).order_by('create_time')
            else:
                return self.queryset.filter(openid=self.request.auth.openid, dn_status=2, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.DNListUpdateSerializer
        elif self.action == 'update':
            return serializers.DNListUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        qs = self.get_queryset()
        for v in range(len(qs)):
            dn_detail_list = DnDetailModel.objects.filter(openid=self.request.auth.openid, dn_code=qs[v].dn_code,
                                                          dn_status=2, is_delete=False)
            picking_list = []
            picking_list_label = 0
            back_order_list = []
            back_order_list_label = 0
            back_order_goods_weight_list = []
            back_order_goods_volume_list = []
            back_order_base_code = DnListModel.objects.filter(openid=self.request.auth.openid,
                                                              is_delete=False).order_by('-id').first().dn_code
            dn_last_code = re.findall(r'\d+', str(back_order_base_code), re.IGNORECASE)
            back_order_dn_code = 'DN' + str(int(dn_last_code[0]) + 1).zfill(8)
            total_weight = qs[v].total_weight
            total_volume = qs[v].total_volume
            for i in range(len(dn_detail_list)):
                goods_detail = goods.objects.filter(openid=self.request.auth.openid,
                                                    goods_code=str(dn_detail_list[i].goods_code),
                                                    is_delete=False).first()
                if stocklist.objects.filter(openid=self.request.auth.openid,
                                            goods_code=str(dn_detail_list[i].goods_code)).exists():
                    pass
                else:
                    stocklist.objects.create(openid=self.request.auth.openid,
                                             goods_code=str(goods_detail.goods_code),
                                             goods_desc=goods_detail.goods_desc,
                                             dn_stock=int(dn_detail_list[i].goods_qty))
                goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                            goods_code=str(
                                                                dn_detail_list[i].goods_code)).first()
                goods_bin_stock_list = stockbin.objects.filter(openid=self.request.auth.openid,
                                                               goods_code=str(dn_detail_list[i].goods_code),
                                                               bin_property="Normal").order_by('-id')
                can_pick_qty = goods_qty_change.onhand_stock - goods_qty_change.pick_stock - goods_qty_change.picked_stock
                if can_pick_qty > 0:
                    if dn_detail_list[i].goods_qty > can_pick_qty:
                        if qs[v].back_order_label == False:
                            dn_pick_qty = dn_detail_list[i].pick_qty
                            for j in range(len(goods_bin_stock_list)):
                                bin_can_pick_qty = goods_bin_stock_list[j].goods_qty - \
                                                   goods_bin_stock_list[j].pick_qty - \
                                                   goods_bin_stock_list[j].picked_qty
                                if bin_can_pick_qty > 0:
                                    goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[
                                                                           j].pick_qty + bin_can_pick_qty
                                    goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - bin_can_pick_qty
                                    goods_qty_change.pick_stock = goods_qty_change.pick_stock + bin_can_pick_qty
                                    picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                         dn_code=dn_detail_list[i].dn_code,
                                                                         bin_name=goods_bin_stock_list[j].bin_name,
                                                                         goods_code=goods_bin_stock_list[
                                                                             i].goods_code,
                                                                         pick_qty=bin_can_pick_qty,
                                                                         creater=self.request.auth.name))
                                    picking_list_label = 1
                                    dn_pick_qty = dn_pick_qty + bin_can_pick_qty
                                    goods_qty_change.save()
                                    goods_bin_stock_list[j].save()
                                elif bin_can_pick_qty == 0:
                                    continue
                                else:
                                    continue
                            dn_detail_list[i].pick_qty = dn_pick_qty
                            dn_back_order_qty = dn_detail_list[i].goods_qty - \
                                                dn_detail_list[i].pick_qty - \
                                                dn_detail_list[i].picked_qty
                            dn_detail_list[i].goods_qty = dn_pick_qty
                            dn_detail_list[i].dn_status = 3
                            goods_qty_change.back_order_stock = goods_qty_change.back_order_stock + \
                                                                dn_back_order_qty
                            back_order_goods_volume = round(goods_detail.unit_volume * dn_back_order_qty, 8)
                            back_order_goods_weight = round(
                                (goods_detail.goods_weight * dn_back_order_qty) / 1000, 8)
                            back_order_list.append(DnDetailModel(dn_code=back_order_dn_code,
                                                                 dn_status=2,
                                                                 customer=qs[v].customer,
                                                                 goods_code=dn_detail_list[i].goods_code,
                                                                 goods_qty=dn_back_order_qty,
                                                                 goods_weight=back_order_goods_weight,
                                                                 goods_volume=back_order_goods_volume,
                                                                 creater=self.request.auth.name,
                                                                 back_order_label=True,
                                                                 openid=self.request.auth.openid,
                                                                 create_time=dn_detail_list[i].create_time))
                            back_order_list_label = 1
                            total_weight = total_weight - back_order_goods_weight
                            total_volume = total_volume - back_order_goods_volume
                            dn_detail_list[i].goods_weight = dn_detail_list[i].goods_weight - \
                                                             back_order_goods_weight
                            dn_detail_list[i].goods_volume = dn_detail_list[i].goods_volume - \
                                                             back_order_goods_volume
                            back_order_goods_weight_list.append(back_order_goods_weight)
                            back_order_goods_volume_list.append(back_order_goods_volume)
                            goods_qty_change.save()
                            dn_detail_list[i].save()
                        else:
                            dn_pick_qty = dn_detail_list[i].pick_qty
                            for j in range(len(goods_bin_stock_list)):
                                bin_can_pick_qty = goods_bin_stock_list[j].goods_qty - \
                                                   goods_bin_stock_list[j].pick_qty - \
                                                   goods_bin_stock_list[j].picked_qty
                                if bin_can_pick_qty > 0:
                                    goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[
                                                                           j].pick_qty + bin_can_pick_qty
                                    goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - bin_can_pick_qty
                                    goods_qty_change.pick_stock = goods_qty_change.pick_stock + bin_can_pick_qty
                                    picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                         dn_code=dn_detail_list[i].dn_code,
                                                                         bin_name=goods_bin_stock_list[j].bin_name,
                                                                         goods_code=goods_bin_stock_list[
                                                                             i].goods_code,
                                                                         pick_qty=bin_can_pick_qty,
                                                                         creater=self.request.auth.name))
                                    picking_list_label = 1
                                    dn_pick_qty = dn_pick_qty + bin_can_pick_qty
                                    goods_qty_change.save()
                                    goods_bin_stock_list[j].save()
                                elif bin_can_pick_qty == 0:
                                    continue
                                else:
                                    continue
                            dn_detail_list[i].pick_qty = dn_pick_qty
                            dn_back_order_qty = dn_detail_list[i].goods_qty - \
                                                dn_detail_list[i].pick_qty - \
                                                dn_detail_list[i].picked_qty
                            dn_detail_list[i].goods_qty = dn_pick_qty
                            dn_detail_list[i].dn_status = 3
                            back_order_goods_volume = round(goods_detail.unit_volume * dn_back_order_qty, 8)
                            back_order_goods_weight = round(
                                (goods_detail.goods_weight * dn_back_order_qty) / 1000, 8)
                            back_order_list.append(DnDetailModel(dn_code=back_order_dn_code,
                                                                 dn_status=2,
                                                                 customer=qs[v].customer,
                                                                 goods_code=dn_detail_list[i].goods_code,
                                                                 goods_qty=dn_back_order_qty,
                                                                 goods_weight=back_order_goods_weight,
                                                                 goods_volume=back_order_goods_volume,
                                                                 creater=self.request.auth.name,
                                                                 back_order_label=True,
                                                                 openid=self.request.auth.openid,
                                                                 create_time=dn_detail_list[i].create_time))
                            back_order_list_label = 1
                            total_weight = total_weight - back_order_goods_weight
                            total_volume = total_volume - back_order_goods_volume
                            dn_detail_list[i].goods_weight = dn_detail_list[i].goods_weight - \
                                                             back_order_goods_weight
                            dn_detail_list[i].goods_volume = dn_detail_list[i].goods_volume - \
                                                             back_order_goods_volume
                            back_order_goods_weight_list.append(back_order_goods_weight)
                            back_order_goods_volume_list.append(back_order_goods_volume)
                            dn_detail_list[i].save()
                    elif dn_detail_list[i].goods_qty == can_pick_qty:
                        for j in range(len(goods_bin_stock_list)):
                            bin_can_pick_qty = goods_bin_stock_list[j].goods_qty - goods_bin_stock_list[
                                j].pick_qty - \
                                               goods_bin_stock_list[j].picked_qty
                            if bin_can_pick_qty > 0:
                                dn_need_pick_qty = dn_detail_list[i].goods_qty - dn_detail_list[i].pick_qty - \
                                                   dn_detail_list[i].picked_qty
                                if dn_need_pick_qty > bin_can_pick_qty:
                                    goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[
                                                                           j].pick_qty + bin_can_pick_qty
                                    goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - bin_can_pick_qty
                                    goods_qty_change.pick_stock = goods_qty_change.pick_stock + bin_can_pick_qty
                                    picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                         dn_code=dn_detail_list[i].dn_code,
                                                                         bin_name=goods_bin_stock_list[j].bin_name,
                                                                         goods_code=goods_bin_stock_list[
                                                                             i].goods_code,
                                                                         pick_qty=bin_can_pick_qty,
                                                                         creater=self.request.auth.name))
                                    picking_list_label = 1
                                    dn_detail_list[i].pick_qty = dn_detail_list[i].pick_qty + bin_can_pick_qty
                                    goods_bin_stock_list[j].save()
                                    goods_qty_change.save()
                                elif dn_need_pick_qty == bin_can_pick_qty:
                                    goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[
                                                                           j].pick_qty + bin_can_pick_qty
                                    goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - bin_can_pick_qty
                                    goods_qty_change.pick_stock = goods_qty_change.pick_stock + bin_can_pick_qty
                                    picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                         dn_code=dn_detail_list[i].dn_code,
                                                                         bin_name=goods_bin_stock_list[j].bin_name,
                                                                         goods_code=goods_bin_stock_list[
                                                                             i].goods_code,
                                                                         pick_qty=bin_can_pick_qty,
                                                                         creater=self.request.auth.name))
                                    picking_list_label = 1
                                    dn_detail_list[i].pick_qty = dn_detail_list[i].pick_qty + bin_can_pick_qty
                                    dn_detail_list[i].dn_status = 3
                                    dn_detail_list[i].save()
                                    goods_bin_stock_list[j].save()
                                    goods_qty_change.save()
                                    break
                                else:
                                    break
                            elif bin_can_pick_qty == 0:
                                continue
                            else:
                                continue
                    elif dn_detail_list[i].goods_qty < can_pick_qty:
                        for j in range(len(goods_bin_stock_list)):
                            bin_can_pick_qty = goods_bin_stock_list[j].goods_qty - \
                                               goods_bin_stock_list[j].pick_qty - \
                                               goods_bin_stock_list[j].picked_qty
                            if bin_can_pick_qty > 0:
                                dn_need_pick_qty = dn_detail_list[i].goods_qty - \
                                                   dn_detail_list[i].pick_qty - \
                                                   dn_detail_list[i].picked_qty
                                if dn_need_pick_qty > bin_can_pick_qty:
                                    goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[j].pick_qty + \
                                                                       bin_can_pick_qty
                                    goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - \
                                                                     bin_can_pick_qty
                                    goods_qty_change.pick_stock = goods_qty_change.pick_stock + \
                                                                  bin_can_pick_qty
                                    picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                         dn_code=dn_detail_list[i].dn_code,
                                                                         bin_name=goods_bin_stock_list[j].bin_name,
                                                                         goods_code=goods_bin_stock_list[
                                                                             i].goods_code,
                                                                         pick_qty=bin_can_pick_qty,
                                                                         creater=self.request.auth.name))
                                    picking_list_label = 1
                                    dn_detail_list[i].pick_qty = dn_detail_list[i].pick_qty + \
                                                                 bin_can_pick_qty
                                    dn_detail_list[i].save()
                                    goods_bin_stock_list[j].save()
                                    goods_qty_change.save()
                                elif dn_need_pick_qty == bin_can_pick_qty:
                                    goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[
                                                                           j].pick_qty + bin_can_pick_qty
                                    goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - bin_can_pick_qty
                                    goods_qty_change.pick_stock = goods_qty_change.pick_stock + bin_can_pick_qty
                                    picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                         dn_code=dn_detail_list[i].dn_code,
                                                                         bin_name=goods_bin_stock_list[j].bin_name,
                                                                         goods_code=goods_bin_stock_list[
                                                                             i].goods_code,
                                                                         pick_qty=bin_can_pick_qty,
                                                                         creater=self.request.auth.name))
                                    picking_list_label = 1
                                    dn_detail_list[i].pick_qty = dn_detail_list[i].pick_qty + bin_can_pick_qty
                                    dn_detail_list[i].dn_status = 3
                                    dn_detail_list[i].save()
                                    goods_bin_stock_list[j].save()
                                    goods_qty_change.save()
                                    break
                                elif dn_need_pick_qty < bin_can_pick_qty:
                                    goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[j].pick_qty + \
                                                                       dn_need_pick_qty
                                    goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - \
                                                                     dn_need_pick_qty
                                    goods_qty_change.pick_stock = goods_qty_change.pick_stock + \
                                                                  dn_need_pick_qty
                                    picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                         dn_code=dn_detail_list[i].dn_code,
                                                                         bin_name=goods_bin_stock_list[j].bin_name,
                                                                         goods_code=goods_bin_stock_list[
                                                                             i].goods_code,
                                                                         pick_qty=dn_need_pick_qty,
                                                                         creater=self.request.auth.name))
                                    picking_list_label = 1
                                    dn_detail_list[i].pick_qty = dn_detail_list[i].pick_qty + dn_need_pick_qty
                                    dn_detail_list[i].dn_status = 3
                                    dn_detail_list[i].save()
                                    goods_bin_stock_list[j].save()
                                    goods_qty_change.save()
                                    break
                                else:
                                    break
                            elif bin_can_pick_qty == 0:
                                continue
                            else:
                                continue
                    else:
                        continue
                elif can_pick_qty == 0:
                    if qs[v].back_order_label == False:
                        goods_qty_change.back_order_stock = goods_qty_change.back_order_stock + dn_detail_list[
                            i].goods_qty
                        back_order_goods_volume = round(goods_detail.unit_volume * dn_detail_list[i].goods_qty, 8)
                        back_order_goods_weight = round(
                            (goods_detail.goods_weight * dn_detail_list[i].goods_qty) / 1000, 8)
                        back_order_list.append(DnDetailModel(dn_code=back_order_dn_code,
                                                             dn_status=2,
                                                             customer=qs[v].customer,
                                                             goods_code=dn_detail_list[i].goods_code,
                                                             goods_qty=dn_detail_list[i].goods_qty,
                                                             goods_weight=back_order_goods_weight,
                                                             goods_volume=back_order_goods_volume,
                                                             creater=self.request.auth.name,
                                                             back_order_label=True,
                                                             openid=self.request.auth.openid,
                                                             create_time=dn_detail_list[i].create_time))
                        back_order_list_label = 1
                        total_weight = total_weight - back_order_goods_weight
                        total_volume = total_volume - back_order_goods_volume
                        back_order_goods_weight_list.append(back_order_goods_weight)
                        back_order_goods_volume_list.append(back_order_goods_volume)
                        dn_detail_list[i].is_delete = True
                        dn_detail_list[i].save()
                        goods_qty_change.save()
                    else:
                        continue
                else:
                    continue
            if picking_list_label == 1:
                if back_order_list_label == 1:
                    back_order_total_volume = sumOfList(back_order_goods_volume_list,
                                                        len(back_order_goods_volume_list))
                    back_order_total_weight = sumOfList(back_order_goods_weight_list,
                                                        len(back_order_goods_weight_list))
                    customer_city = customer.objects.filter(openid=self.request.auth.openid,
                                                            customer_name=str(qs[v].customer),
                                                            is_delete=False).first().customer_city
                    warehouse_city = warehouse.objects.filter(
                        openid=self.request.auth.openid).first().warehouse_city
                    transportation_fee = transportation.objects.filter(
                        Q(openid=self.request.auth.openid, send_city__icontains=warehouse_city,
                          receiver_city__icontains=customer_city,
                          is_delete=False) | Q(openid='init_data', send_city__icontains=warehouse_city,
                                               receiver_city__icontains=customer_city,
                                               is_delete=False))
                    transportation_res = {
                        "detail": []
                    }
                    transportation_back_order_res = {
                        "detail": []
                    }
                    if len(transportation_fee) >= 1:
                        transportation_list = []
                        transportation_back_order_list = []
                        for k in range(len(transportation_fee)):
                            transportation_cost = transportation_calculate(total_weight,
                                                                           total_volume,
                                                                           transportation_fee[k].weight_fee,
                                                                           transportation_fee[k].volume_fee,
                                                                           transportation_fee[k].min_payment)
                            transportation_back_order_cost = transportation_calculate(back_order_total_weight,
                                                                                      back_order_total_volume,
                                                                                      transportation_fee[
                                                                                          k].weight_fee,
                                                                                      transportation_fee[
                                                                                          k].volume_fee,
                                                                                      transportation_fee[
                                                                                          k].min_payment)
                            transportation_detail = {
                                "transportation_supplier": transportation_fee[k].transportation_supplier,
                                "transportation_cost": transportation_cost
                            }
                            transportation_back_order_detail = {
                                "transportation_supplier": transportation_fee[k].transportation_supplier,
                                "transportation_cost": transportation_back_order_cost
                            }
                            transportation_list.append(transportation_detail)
                            transportation_back_order_list.append(transportation_back_order_detail)
                        transportation_res['detail'] = transportation_list
                        transportation_back_order_res['detail'] = transportation_back_order_list
                    DnListModel.objects.create(openid=self.request.auth.openid,
                                               dn_code=back_order_dn_code,
                                               dn_status=2,
                                               total_weight=back_order_total_weight,
                                               total_volume=back_order_total_volume,
                                               customer=qs[v].customer,
                                               creater=self.request.auth.name,
                                               back_order_label=True,
                                               transportation_fee=transportation_back_order_res,
                                               create_time=qs[v].create_time)
                    PickingListModel.objects.bulk_create(picking_list, batch_size=100)
                    DnDetailModel.objects.bulk_create(back_order_list, batch_size=100)
                    qs[v].total_weight = total_weight
                    qs[v].total_volume = total_volume
                    qs[v].transportation_fee = transportation_res
                    qs[v].dn_status = 3
                    qs[v].save()
                elif back_order_list_label == 0:
                    PickingListModel.objects.bulk_create(picking_list, batch_size=100)
                    qs[v].dn_status = 3
                    qs[v].save()
                else:
                    continue
            elif picking_list_label == 0:
                if back_order_list_label == 1:
                    DnDetailModel.objects.bulk_create(back_order_list, batch_size=100)
                    DnListModel.objects.create(openid=self.request.auth.openid,
                                               dn_code=back_order_dn_code,
                                               dn_status=2,
                                               total_weight=qs[v].total_weight,
                                               total_volume=qs[v].total_volume,
                                               customer=qs[v].customer,
                                               creater=self.request.auth.name,
                                               back_order_label=True,
                                               transportation_fee=qs[v].transportation_fee,
                                               create_time=qs[v].create_time)
                    qs[v].is_delete = True
                    qs[v].dn_status = 3
                    qs[v].save()
                elif back_order_list_label == 0:
                    continue
                else:
                    continue
            else:
                continue
        return Response({"detail": "success"}, status=200)

    def update(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot Release Order data which not yours"})
        else:
            if qs.dn_status == 2:
                dn_detail_list = DnDetailModel.objects.filter(openid=self.request.auth.openid, dn_code=qs.dn_code,
                                                                dn_status=2, is_delete=False)
                picking_list = []
                picking_list_label = 0
                back_order_list = []
                back_order_list_label = 0
                back_order_goods_weight_list = []
                back_order_goods_volume_list = []
                back_order_base_code = DnListModel.objects.filter(openid=self.request.auth.openid, is_delete=False).order_by('-id').first().dn_code
                dn_last_code = re.findall(r'\d+', str(back_order_base_code), re.IGNORECASE)
                back_order_dn_code = 'DN' + str(int(dn_last_code[0]) + 1).zfill(8)
                total_weight = qs.total_weight
                total_volume = qs.total_volume
                for i in range(len(dn_detail_list)):
                    goods_detail = goods.objects.filter(openid=self.request.auth.openid,
                                                        goods_code=str(dn_detail_list[i].goods_code),
                                                        is_delete=False).first()
                    if stocklist.objects.filter(openid=self.request.auth.openid,
                                                goods_code=str(dn_detail_list[i].goods_code)).exists():
                        pass
                    else:
                        stocklist.objects.create(openid=self.request.auth.openid,
                                                 goods_code=str(goods_detail.goods_code),
                                                 goods_desc=goods_detail.goods_desc,
                                                 dn_stock=int(dn_detail_list[i].goods_qty))
                    goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                goods_code=str(
                                                                    dn_detail_list[i].goods_code)).first()
                    goods_bin_stock_list = stockbin.objects.filter(openid=self.request.auth.openid,
                                                                   goods_code=str(dn_detail_list[i].goods_code),
                                                                   bin_property="Normal").order_by('-id')
                    can_pick_qty = goods_qty_change.onhand_stock - goods_qty_change.pick_stock - goods_qty_change.picked_stock
                    if can_pick_qty > 0:
                        if dn_detail_list[i].goods_qty > can_pick_qty:
                            if qs.back_order_label == False:
                                dn_pick_qty = dn_detail_list[i].pick_qty
                                for j in range(len(goods_bin_stock_list)):
                                    bin_can_pick_qty = goods_bin_stock_list[j].goods_qty - \
                                                       goods_bin_stock_list[j].pick_qty - \
                                                       goods_bin_stock_list[j].picked_qty
                                    if bin_can_pick_qty > 0:
                                        goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[
                                                                               j].pick_qty + bin_can_pick_qty
                                        goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - bin_can_pick_qty
                                        goods_qty_change.pick_stock = goods_qty_change.pick_stock + bin_can_pick_qty
                                        picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                             dn_code=dn_detail_list[i].dn_code,
                                                                             bin_name=goods_bin_stock_list[j].bin_name,
                                                                             goods_code=goods_bin_stock_list[
                                                                                 i].goods_code,
                                                                             pick_qty=bin_can_pick_qty,
                                                                             creater=self.request.auth.name))
                                        picking_list_label = 1
                                        dn_pick_qty = dn_pick_qty + bin_can_pick_qty
                                        goods_qty_change.save()
                                        goods_bin_stock_list[j].save()
                                    elif bin_can_pick_qty == 0:
                                        continue
                                    else:
                                        continue
                                dn_detail_list[i].pick_qty = dn_pick_qty
                                dn_back_order_qty = dn_detail_list[i].goods_qty - \
                                                   dn_detail_list[i].pick_qty - \
                                                   dn_detail_list[i].picked_qty
                                dn_detail_list[i].goods_qty = dn_pick_qty
                                dn_detail_list[i].dn_status = 3
                                goods_qty_change.back_order_stock = goods_qty_change.back_order_stock + \
                                                                    dn_back_order_qty
                                back_order_goods_volume = round(goods_detail.unit_volume * dn_back_order_qty, 8)
                                back_order_goods_weight = round(
                                    (goods_detail.goods_weight * dn_back_order_qty) / 1000, 8)
                                back_order_list.append(DnDetailModel(dn_code=back_order_dn_code,
                                                                     dn_status=2,
                                                                     customer=qs.customer,
                                                                     goods_code=dn_detail_list[i].goods_code,
                                                                     goods_qty=dn_back_order_qty,
                                                                     goods_weight=back_order_goods_weight,
                                                                     goods_volume=back_order_goods_volume,
                                                                     creater=self.request.auth.name,
                                                                     back_order_label=True,
                                                                     openid=self.request.auth.openid,
                                                                     create_time=dn_detail_list[i].create_time))
                                back_order_list_label = 1
                                total_weight = total_weight - back_order_goods_weight
                                total_volume = total_volume - back_order_goods_volume
                                dn_detail_list[i].goods_weight = dn_detail_list[i].goods_weight - \
                                                                 back_order_goods_weight
                                dn_detail_list[i].goods_volume = dn_detail_list[i].goods_volume - \
                                                                 back_order_goods_volume
                                back_order_goods_weight_list.append(back_order_goods_weight)
                                back_order_goods_volume_list.append(back_order_goods_volume)
                                goods_qty_change.save()
                                dn_detail_list[i].save()
                            else:
                                dn_pick_qty = dn_detail_list[i].pick_qty
                                for j in range(len(goods_bin_stock_list)):
                                    bin_can_pick_qty = goods_bin_stock_list[j].goods_qty - \
                                                       goods_bin_stock_list[j].pick_qty - \
                                                       goods_bin_stock_list[j].picked_qty
                                    if bin_can_pick_qty > 0:
                                        goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[
                                                                               j].pick_qty + bin_can_pick_qty
                                        goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - bin_can_pick_qty
                                        goods_qty_change.pick_stock = goods_qty_change.pick_stock + bin_can_pick_qty
                                        picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                             dn_code=dn_detail_list[i].dn_code,
                                                                             bin_name=goods_bin_stock_list[j].bin_name,
                                                                             goods_code=goods_bin_stock_list[
                                                                                 i].goods_code,
                                                                             pick_qty=bin_can_pick_qty,
                                                                             creater=self.request.auth.name))
                                        picking_list_label = 1
                                        dn_pick_qty = dn_pick_qty + bin_can_pick_qty
                                        goods_qty_change.save()
                                        goods_bin_stock_list[j].save()
                                    elif bin_can_pick_qty == 0:
                                        continue
                                    else:
                                        continue
                                dn_detail_list[i].pick_qty = dn_pick_qty
                                dn_back_order_qty = dn_detail_list[i].goods_qty - \
                                                    dn_detail_list[i].pick_qty - \
                                                    dn_detail_list[i].picked_qty
                                dn_detail_list[i].goods_qty = dn_pick_qty
                                dn_detail_list[i].dn_status = 3
                                back_order_goods_volume = round(goods_detail.unit_volume * dn_back_order_qty, 8)
                                back_order_goods_weight = round(
                                    (goods_detail.goods_weight * dn_back_order_qty) / 1000, 8)
                                back_order_list.append(DnDetailModel(dn_code=back_order_dn_code,
                                                                     dn_status=2,
                                                                     customer=qs.customer,
                                                                     goods_code=dn_detail_list[i].goods_code,
                                                                     goods_qty=dn_back_order_qty,
                                                                     goods_weight=back_order_goods_weight,
                                                                     goods_volume=back_order_goods_volume,
                                                                     creater=self.request.auth.name,
                                                                     back_order_label=True,
                                                                     openid=self.request.auth.openid,
                                                                     create_time=dn_detail_list[i].create_time))
                                back_order_list_label = 1
                                total_weight = total_weight - back_order_goods_weight
                                total_volume = total_volume - back_order_goods_volume
                                dn_detail_list[i].goods_weight = dn_detail_list[i].goods_weight - \
                                                                 back_order_goods_weight
                                dn_detail_list[i].goods_volume = dn_detail_list[i].goods_volume - \
                                                                 back_order_goods_volume
                                back_order_goods_weight_list.append(back_order_goods_weight)
                                back_order_goods_volume_list.append(back_order_goods_volume)
                                dn_detail_list[i].save()
                        elif dn_detail_list[i].goods_qty == can_pick_qty:
                            for j in range(len(goods_bin_stock_list)):
                                bin_can_pick_qty = goods_bin_stock_list[j].goods_qty - goods_bin_stock_list[j].pick_qty - \
                                                   goods_bin_stock_list[j].picked_qty
                                if bin_can_pick_qty > 0:
                                    dn_need_pick_qty = dn_detail_list[i].goods_qty - dn_detail_list[i].pick_qty - dn_detail_list[i].picked_qty
                                    if dn_need_pick_qty > bin_can_pick_qty:
                                        goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[
                                                                               j].pick_qty + bin_can_pick_qty
                                        goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - bin_can_pick_qty
                                        goods_qty_change.pick_stock = goods_qty_change.pick_stock + bin_can_pick_qty
                                        picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                        dn_code=dn_detail_list[i].dn_code,
                                                                        bin_name=goods_bin_stock_list[j].bin_name,
                                                                        goods_code=goods_bin_stock_list[i].goods_code,
                                                                        pick_qty=bin_can_pick_qty,
                                                                        creater=self.request.auth.name))
                                        picking_list_label = 1
                                        dn_detail_list[i].pick_qty = dn_detail_list[i].pick_qty + bin_can_pick_qty
                                        goods_bin_stock_list[j].save()
                                        goods_qty_change.save()
                                    elif dn_need_pick_qty == bin_can_pick_qty:
                                        goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[
                                                                               j].pick_qty + bin_can_pick_qty
                                        goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - bin_can_pick_qty
                                        goods_qty_change.pick_stock = goods_qty_change.pick_stock + bin_can_pick_qty
                                        picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                        dn_code=dn_detail_list[i].dn_code,
                                                                        bin_name=goods_bin_stock_list[j].bin_name,
                                                                        goods_code=goods_bin_stock_list[i].goods_code,
                                                                        pick_qty=bin_can_pick_qty,
                                                                        creater=self.request.auth.name))
                                        picking_list_label = 1
                                        dn_detail_list[i].pick_qty = dn_detail_list[i].pick_qty + bin_can_pick_qty
                                        dn_detail_list[i].dn_status = 3
                                        dn_detail_list[i].save()
                                        goods_bin_stock_list[j].save()
                                        goods_qty_change.save()
                                        break
                                    else:
                                        break
                                elif bin_can_pick_qty == 0:
                                    continue
                                else:
                                    continue
                        elif dn_detail_list[i].goods_qty < can_pick_qty:
                            for j in range(len(goods_bin_stock_list)):
                                bin_can_pick_qty = goods_bin_stock_list[j].goods_qty - \
                                                   goods_bin_stock_list[j].pick_qty - \
                                                   goods_bin_stock_list[j].picked_qty
                                if bin_can_pick_qty > 0:
                                    dn_need_pick_qty = dn_detail_list[i].goods_qty - \
                                                       dn_detail_list[i].pick_qty - \
                                                       dn_detail_list[i].picked_qty
                                    if dn_need_pick_qty > bin_can_pick_qty:
                                        goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[j].pick_qty + \
                                                                           bin_can_pick_qty
                                        goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - \
                                                                         bin_can_pick_qty
                                        goods_qty_change.pick_stock = goods_qty_change.pick_stock + \
                                                                      bin_can_pick_qty
                                        picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                             dn_code=dn_detail_list[i].dn_code,
                                                                             bin_name=goods_bin_stock_list[j].bin_name,
                                                                             goods_code=goods_bin_stock_list[i].goods_code,
                                                                             pick_qty=bin_can_pick_qty,
                                                                             creater=self.request.auth.name))
                                        picking_list_label = 1
                                        dn_detail_list[i].pick_qty = dn_detail_list[i].pick_qty + \
                                                                     bin_can_pick_qty
                                        dn_detail_list[i].save()
                                        goods_bin_stock_list[j].save()
                                        goods_qty_change.save()
                                    elif dn_need_pick_qty == bin_can_pick_qty:
                                        goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[
                                                                               j].pick_qty + bin_can_pick_qty
                                        goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - bin_can_pick_qty
                                        goods_qty_change.pick_stock = goods_qty_change.pick_stock + bin_can_pick_qty
                                        picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                        dn_code=dn_detail_list[i].dn_code,
                                                                        bin_name=goods_bin_stock_list[j].bin_name,
                                                                        goods_code=goods_bin_stock_list[i].goods_code,
                                                                        pick_qty=bin_can_pick_qty,
                                                                        creater=self.request.auth.name))
                                        picking_list_label = 1
                                        dn_detail_list[i].pick_qty = dn_detail_list[i].pick_qty + bin_can_pick_qty
                                        dn_detail_list[i].dn_status = 3
                                        dn_detail_list[i].save()
                                        goods_bin_stock_list[j].save()
                                        goods_qty_change.save()
                                        break
                                    elif dn_need_pick_qty < bin_can_pick_qty:
                                        goods_bin_stock_list[j].pick_qty = goods_bin_stock_list[j].pick_qty + \
                                                                           dn_need_pick_qty
                                        goods_qty_change.ordered_stock = goods_qty_change.ordered_stock - \
                                                                         dn_need_pick_qty
                                        goods_qty_change.pick_stock = goods_qty_change.pick_stock + \
                                                                      dn_need_pick_qty
                                        picking_list.append(PickingListModel(openid=self.request.auth.openid,
                                                                             dn_code=dn_detail_list[i].dn_code,
                                                                             bin_name=goods_bin_stock_list[j].bin_name,
                                                                             goods_code=goods_bin_stock_list[i].goods_code,
                                                                             pick_qty=dn_need_pick_qty,
                                                                             creater=self.request.auth.name))
                                        picking_list_label = 1
                                        dn_detail_list[i].pick_qty = dn_detail_list[i].pick_qty + dn_need_pick_qty
                                        dn_detail_list[i].dn_status = 3
                                        dn_detail_list[i].save()
                                        goods_bin_stock_list[j].save()
                                        goods_qty_change.save()
                                        break
                                    else:
                                        break
                                elif bin_can_pick_qty == 0:
                                    continue
                                else:
                                    continue
                        else:
                            pass
                    elif can_pick_qty == 0:
                        if qs.back_order_label == False:
                            goods_qty_change.back_order_stock = goods_qty_change.back_order_stock + dn_detail_list[i].goods_qty
                            back_order_goods_volume = round(goods_detail.unit_volume * dn_detail_list[i].goods_qty, 8)
                            back_order_goods_weight = round((goods_detail.goods_weight * dn_detail_list[i].goods_qty) / 1000, 8)
                            back_order_list.append(DnDetailModel(dn_code=back_order_dn_code,
                                                                 dn_status=2,
                                                                 customer=qs.customer,
                                                                 goods_code=dn_detail_list[i].goods_code,
                                                                 goods_qty=dn_detail_list[i].goods_qty,
                                                                 goods_weight=back_order_goods_weight,
                                                                 goods_volume=back_order_goods_volume,
                                                                 creater=self.request.auth.name,
                                                                 back_order_label=True,
                                                                 openid=self.request.auth.openid,
                                                                 create_time=dn_detail_list[i].create_time))
                            back_order_list_label = 1
                            total_weight = total_weight - back_order_goods_weight
                            total_volume = total_volume - back_order_goods_volume
                            back_order_goods_weight_list.append(back_order_goods_weight)
                            back_order_goods_volume_list.append(back_order_goods_volume)
                            dn_detail_list[i].is_delete = True
                            dn_detail_list[i].save()
                            goods_qty_change.save()
                        else:
                            continue
                    else:
                        continue
                if picking_list_label == 1:
                    if back_order_list_label == 1:
                        back_order_total_volume = sumOfList(back_order_goods_volume_list,
                                                            len(back_order_goods_volume_list))
                        back_order_total_weight = sumOfList(back_order_goods_weight_list,
                                                            len(back_order_goods_weight_list))
                        customer_city = customer.objects.filter(openid=self.request.auth.openid,
                                                                customer_name=str(qs.customer),
                                                                is_delete=False).first().customer_city
                        warehouse_city = warehouse.objects.filter(
                            openid=self.request.auth.openid).first().warehouse_city
                        transportation_fee = transportation.objects.filter(
                            Q(openid=self.request.auth.openid, send_city__icontains=warehouse_city,
                              receiver_city__icontains=customer_city,
                              is_delete=False) | Q(openid='init_data', send_city__icontains=warehouse_city,
                                                   receiver_city__icontains=customer_city,
                                                   is_delete=False))
                        transportation_res = {
                            "detail": []
                        }
                        transportation_back_order_res = {
                            "detail": []
                        }
                        if len(transportation_fee) >= 1:
                            transportation_list = []
                            transportation_back_order_list = []
                            for k in range(len(transportation_fee)):
                                transportation_cost = transportation_calculate(total_weight,
                                                                               total_volume,
                                                                               transportation_fee[k].weight_fee,
                                                                               transportation_fee[k].volume_fee,
                                                                               transportation_fee[k].min_payment)
                                transportation_back_order_cost = transportation_calculate(back_order_total_weight,
                                                                               back_order_total_volume,
                                                                               transportation_fee[k].weight_fee,
                                                                               transportation_fee[k].volume_fee,
                                                                               transportation_fee[k].min_payment)
                                transportation_detail = {
                                    "transportation_supplier": transportation_fee[k].transportation_supplier,
                                    "transportation_cost": transportation_cost
                                }
                                transportation_back_order_detail = {
                                    "transportation_supplier": transportation_fee[k].transportation_supplier,
                                    "transportation_cost": transportation_back_order_cost
                                }
                                transportation_list.append(transportation_detail)
                                transportation_back_order_list.append(transportation_back_order_detail)
                            transportation_res['detail'] = transportation_list
                            transportation_back_order_res['detail'] = transportation_back_order_list
                        DnListModel.objects.create(openid=self.request.auth.openid,
                                                   dn_code=back_order_dn_code,
                                                   dn_status=2,
                                                   total_weight=back_order_total_weight,
                                                   total_volume=back_order_total_volume,
                                                   customer=qs.customer,
                                                   creater=self.request.auth.name,
                                                   back_order_label=True,
                                                   transportation_fee=transportation_back_order_res,
                                                   create_time=qs.create_time)
                        PickingListModel.objects.bulk_create(picking_list, batch_size=100)
                        DnDetailModel.objects.bulk_create(back_order_list, batch_size=100)
                        qs.total_weight = total_weight
                        qs.total_volume = total_volume
                        qs.transportation_fee = transportation_res
                        qs.dn_status = 3
                        qs.save()
                    elif back_order_list_label == 0:
                        PickingListModel.objects.bulk_create(picking_list, batch_size=100)
                        qs.dn_status = 3
                        qs.save()
                        return Response({"detail": "success"}, status=200)
                    else:
                        raise APIException({"detail": "This Order Does Not in Release Status"})
                elif picking_list_label == 0:
                    if back_order_list_label == 1:
                        DnDetailModel.objects.bulk_create(back_order_list, batch_size=100)
                        DnListModel.objects.create(openid=self.request.auth.openid,
                                                   dn_code=back_order_dn_code,
                                                   dn_status=2,
                                                   total_weight=qs.total_weight,
                                                   total_volume=qs.total_volume,
                                                   customer=qs.customer,
                                                   creater=self.request.auth.name,
                                                   back_order_label=True,
                                                   transportation_fee=qs.transportation_fee,
                                                   create_time=qs.create_time)
                        qs.is_delete = True
                        qs.dn_status = 3
                        qs.save()
                    elif back_order_list_label == 0:
                        return Response({"detail": "success"}, status=200)
                    else:
                        raise APIException({"detail": "This Order Does Not in Release Status"})
                else:
                    raise APIException({"detail": "This Order Does Not in Release Status"})
                return Response({"detail": "success"}, status=200)
            else:
                raise APIException({"detail": "This Order Does Not in Release Status"})

class DnSortedViewSet(viewsets.ModelViewSet):
    """
        create:
            Finish Sorted
    """
    queryset = DnListModel.objects.all()
    serializer_class = serializers.DNListGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = DnListFilter

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
                return self.queryset.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.DNListUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, pk):
        qs = self.get_object()
        if qs.dn_status != 3:
            raise APIException({"detail": "This dn Status does not correct"})
        else:
            data = request.data
            for i in range(len(data['goods_code'])):
                check_data = {
                    'openid': self.request.auth.openid,
                    'dn_code': str(data['dn_code']),
                    'customer': str(data['customer']),
                    'goods_code': str(data['goods_code'][i]),
                    'goods_qty': int(data['goods_qty'][i]),
                    'creater': str(data['creater'])
                }
                serializer = self.get_serializer(data=check_data)
                serializer.is_valid(raise_exception=True)
            qs.dn_status = 4
            for j in range(len(data['goods_code'])):
                goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                            goods_code=str(data['goods_code'][j])).first()
                dn_detail = DnDetailModel.objects.filter(openid=self.request.auth.openid, dn_code=str(data['dn_code']),
                                                  dn_status=3, customer=str(data['customer']),
                                                  goods_code=str(data['goods_code'][j])).first()
                dn_detail.dn_status = 4
                dn_detail.goods_actual_qty = int(data['goods_qty'][j])
                goods_qty_check = dn_detail.goods_qty - int(data['goods_qty'][j])
                if goods_qty_check > 0:
                    dn_detail.goods_shortage_qty = goods_qty_check
                    dn_detail.goods_more_qty = 0
                    goods_qty_change.goods_qty = goods_qty_change.goods_qty - goods_qty_check
                    goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - dn_detail.goods_qty
                    goods_qty_change.sorted_stock = goods_qty_change.sorted_stock + int(data['goods_qty'][j])
                elif goods_qty_check == 0:
                    dn_detail.goods_shortage_qty = 0
                    dn_detail.goods_more_qty = 0
                    goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - int(data['goods_qty'][j])
                    goods_qty_change.sorted_stock = goods_qty_change.sorted_stock + int(data['goods_qty'][j])
                elif goods_qty_check < 0:
                    dn_detail.goods_shortage_qty = 0
                    dn_detail.goods_more_qty = abs(goods_qty_check)
                    goods_qty_change.goods_qty = goods_qty_change.goods_qty + abs(goods_qty_check)
                    goods_qty_change.pre_sort_stock = goods_qty_change.pre_sort_stock - dn_detail.goods_qty
                    goods_qty_change.sorted_stock = goods_qty_change.sorted_stock + int(data['goods_qty'][j])
                else:
                    pass
                dn_detail.save()
                goods_qty_change.save()
            qs.save()
            return Response({"ok": "ok"}, status=200)

class MoveToBinViewSet(viewsets.ModelViewSet):
    """
        create:
            Create a data line（post）
    """
    queryset = DnDetailModel.objects.all()
    serializer_class = serializers.MoveToBinSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = DnDetailFilter

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
                return self.queryset.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.DNDetailGetSerializer
        elif self.action == 'create':
            return serializers.MoveToBinSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot delete data which not yours"})
        else:
            if qs.dn_status != 4:
                raise APIException({"detail": "dn Status does not correct , Can not Move To Bin"})
            else:
                data = request.data
                if 'bin_name' not in data:
                    raise APIException({"detail": "Please Enter the Bin Name"})
                else:
                    bin_detail = binset.objects.filter(openid=self.request.auth.openid,
                                                                bin_name=str(data['bin_name'])).first()
                    dn_detail = DnListModel.objects.filter(openid=self.request.auth.openid,
                                                                dn_code=str(data['dn_code'])).first()
                    goods_qty_change = stocklist.objects.filter(openid=self.request.auth.openid,
                                                                goods_code=str(data['goods_code'])).first()
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
                        elif bin_detail.bin_property == 'Cross_Docking':
                            goods_qty_change.cross_dock_stock = goods_qty_change.cross_dock_stock + int(data['qty'])
                        elif bin_detail.bin_property == 'Holding':
                            goods_qty_change.hold_stock = goods_qty_change.hold_stock + int(data['qty'])
                        else:
                            goods_qty_change.can_order_stock = goods_qty_change.can_order_stock + int(data['qty'])
                        qs.save()
                        goods_qty_change.save()
                        stockbin.objects.create(openid=self.request.auth.openid,
                                                bin_name=str(data['bin_name']), goods_code=str(data['goods_code']),
                                                goods_desc=goods_qty_change.goods_desc, goods_qty=int(data['qty']),
                                                bin_size=bin_detail.bin_size, bin_property=bin_detail.bin_property)
                        if bin_detail.empty_label == True:
                            bin_detail.empty_label = False
                            bin_detail.save()
                    elif move_qty == 0:
                        qs.sorted_qty = qs.sorted_qty + int(data['qty'])
                        qs.dn_status = 5
                        dn_detail.dn_status = 5
                        goods_qty_change.sorted_stock = goods_qty_change.sorted_stock - int(data['qty'])
                        goods_qty_change.onhand_stock = goods_qty_change.onhand_stock + int(data['qty'])
                        if bin_detail.bin_property == 'Damage':
                            goods_qty_change.damage_stock = goods_qty_change.damage_stock + int(data['qty'])
                            qs.goods_damage_qty = qs.goods_damage_qty + int(data['qty'])
                        elif bin_detail.bin_property == 'Inspection':
                            goods_qty_change.inspect_stock = goods_qty_change.inspect_stock + int(data['qty'])
                        elif bin_detail.bin_property == 'Cross_Docking':
                            goods_qty_change.cross_dock_stock = goods_qty_change.cross_dock_stock + int(data['qty'])
                        elif bin_detail.bin_property == 'Holding':
                            goods_qty_change.hold_stock = goods_qty_change.hold_stock + int(data['qty'])
                        else:
                            goods_qty_change.can_order_stock = goods_qty_change.can_order_stock + int(data['qty'])
                        qs.save()
                        goods_qty_change.save()
                        stockbin.objects.create(openid=self.request.auth.openid,
                                                bin_name=str(data['bin_name']), goods_code=str(data['goods_code']),
                                                goods_desc=goods_qty_change.goods_desc, goods_qty=int(data['qty']),
                                                bin_size=bin_detail.bin_size, bin_property=bin_detail.bin_property)
                        if bin_detail.empty_label == True:
                            bin_detail.empty_label = False
                            bin_detail.save()
                    elif move_qty < 0:
                        raise APIException({"detail": "Move Qty must < Actual Arrive Qty"})
                    else:
                        pass
                    return Response({"success": "Yes"}, status=200)
