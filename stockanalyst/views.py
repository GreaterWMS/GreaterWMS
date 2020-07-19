from rest_framework.views import APIView
from rest_framework.response import Response
from utils.datasolve import DataSolve
from utils.page import MyPageNumberPagination
from utils.fbmsg import FBMsg
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .schemas import ListSchema
from .serializers import StockAnalystSerializers
from django.conf import settings
import os, math, datetime
import pandas as pd
from shipping.models import ShippingModel
from goods.models import GoodsModel
from baseinfo.models import BaseInfoModel
from users.models import Users
from django.db.models import Sum

@method_decorator(csrf_exempt, name='dispatch')
class StockAnaystAPI(APIView):
    '''
        post:
            新增用户
            可以接收一个json数据，也可以接收一个json数据组，但是不可以批量登入
            只有开发者账号的openid才可以发起用户登入请求
    '''
    # schema = BaseInfoSchema()
    def post(self, request, format=None):
        if ShippingModel.objects.filter(appid=request.user.appid).exists():
            if GoodsModel.objects.filter(appid=request.user.appid).exists():
                if BaseInfoModel.objects.filter(appid=request.user.appid).exists():
                    contacts = ShippingModel.objects.filter(appid=request.user.appid)
                    goods_code = contacts.values('goods_code').distinct()
                    data = []
                    for i in range(len(goods_code)):
                        if GoodsModel.objects.filter(appid=request.user.appid, goods_code=goods_code[i]['goods_code']).exists():
                            if BaseInfoModel.objects.filter(appid=request.user.appid, goods_code=goods_code[i]['goods_code']).exists():
                                on_hand_stock = GoodsModel.objects.filter(appid=request.user.appid,
                                                                          goods_code=goods_code[i][
                                                                              'goods_code']).first().on_hand_stock
                                total_leadtime = BaseInfoModel.objects.filter(appid=request.user.appid,
                                                                              goods_code=goods_code[i][
                                                                                  'goods_code']).first().total_leadtime
                                if on_hand_stock == 0:
                                    today = datetime.date.today()
                                    delta1 = datetime.timedelta(days=29)
                                    delta2 = datetime.timedelta(days=59)
                                    delta3 = datetime.timedelta(days=89)
                                    end_date1 = (today - delta1).strftime('%Y-%m-%d')
                                    end_date2 = (today - delta2).strftime('%Y-%m-%d')
                                    end_date3 = (today - delta3).strftime('%Y-%m-%d')
                                    plan_date = today.strftime('%Y-%m-%d')
                                    shipping_data1 = contacts.filter(goods_code=goods_code[i]['goods_code'], shipping_time__range=[end_date1, today]).aggregate(
                                        Sum('shipping_qty'))
                                    shipping_data2 = contacts.filter(goods_code=goods_code[i]['goods_code'], shipping_time__range=[end_date2, today]).aggregate(
                                        Sum('shipping_qty'))
                                    shipping_data3 = contacts.filter(goods_code=goods_code[i]['goods_code'], shipping_time__range=[end_date3, today]).aggregate(
                                        Sum('shipping_qty'))
                                    analyst = {
                                        "goods_code": goods_code[i]['goods_code'],
                                        "shipping_data1": shipping_data1['shipping_qty__sum'],
                                        "shipping_data2": shipping_data2['shipping_qty__sum'],
                                        "shipping_data3": shipping_data3['shipping_qty__sum'],
                                        "plan_date1": plan_date,
                                        "plan_date2": plan_date,
                                        "plan_date3": plan_date,
                                        "plan_date4": 0,
                                        "oos_lv": "已经断货"
                                    }
                                    data.append(analyst)
                                else:
                                    today = datetime.date.today()
                                    delta1 = datetime.timedelta(days=29)
                                    delta2 = datetime.timedelta(days=59)
                                    delta3 = datetime.timedelta(days=89)
                                    end_date1 = (today - delta1).strftime('%Y-%m-%d')
                                    end_date2 = (today - delta2).strftime('%Y-%m-%d')
                                    end_date3 = (today - delta3).strftime('%Y-%m-%d')
                                    shipping_data1 = contacts.filter(goods_code=goods_code[i]['goods_code'], shipping_time__range=[end_date1, today]).aggregate(
                                        Sum('shipping_qty'))
                                    shipping_data2 = contacts.filter(goods_code=goods_code[i]['goods_code'], shipping_time__range=[end_date2, today]).aggregate(
                                        Sum('shipping_qty'))
                                    shipping_data3 = contacts.filter(goods_code=goods_code[i]['goods_code'], shipping_time__range=[end_date3, today]).aggregate(
                                        Sum('shipping_qty'))
                                    avg_qty1 = shipping_data1['shipping_qty__sum'] / 30
                                    avg_qty2 = shipping_data2['shipping_qty__sum'] / 60
                                    avg_qty3 = shipping_data3['shipping_qty__sum'] / 90
                                    avg_qty4 = (avg_qty1 + avg_qty2 + avg_qty3) / 3
                                    stock_check1 = int(on_hand_stock / avg_qty1)
                                    stock_check2 = int(on_hand_stock / avg_qty2)
                                    stock_check3 = int(on_hand_stock / avg_qty3)
                                    stock_check4 = int(on_hand_stock / avg_qty4)
                                    plan_day1 = datetime.timedelta(days=stock_check1)
                                    plan_day2 = datetime.timedelta(days=stock_check2)
                                    plan_day3 = datetime.timedelta(days=stock_check3)
                                    plan_day4 = datetime.timedelta(days=stock_check4)
                                    plan_date1 = (today + plan_day1).strftime('%Y-%m-%d')
                                    plan_date2 = (today + plan_day2).strftime('%Y-%m-%d')
                                    plan_date3 = (today + plan_day3).strftime('%Y-%m-%d')
                                    oos_notice = plan_day4.days / total_leadtime
                                    if oos_notice >= 3:
                                        oos_lv = "库存过多"
                                    elif 3 > oos_notice >= 2:
                                        oos_lv = "库存充足"
                                    elif 2 > oos_notice >= 1:
                                        oos_notice = plan_day4.days / (total_leadtime + 7)
                                        if oos_notice > 1:
                                            oos_lv = "库存正常"
                                        elif oos_notice <= 1:
                                            oos_lv = "断货风险"
                                        else:
                                            oos_lv = "断货风险极大"
                                    else:
                                        oos_lv = "断货风险极大"
                                    analyst = {
                                        "goods_code": goods_code[i]['goods_code'],
                                        "shipping_data1": shipping_data1['shipping_qty__sum'],
                                        "shipping_data2": shipping_data2['shipping_qty__sum'],
                                        "shipping_data3": shipping_data3['shipping_qty__sum'],
                                        "plan_date1": plan_date1,
                                        "plan_date2": plan_date2,
                                        "plan_date3": plan_date3,
                                        "plan_date4": plan_day4.days,
                                        "oos_lv": oos_lv
                                    }
                                    data.append(analyst)
                                    # end_date = (today + delta).strftime('%Y-%m-%d')
                                    # date = [int(x) for x in date_end.split('-')]
                                    # old = datetime.datetime(date[0], date[1], date[2])
                                    # end_date = (old + delta).strftime('%Y-%m-%d')
                            else:
                                continue
                        else:
                            continue
                    ret = FBMsg.ret()
                    ret['data'] = data
                    return Response(ret)
                else:
                    return Response(FBMsg.err_req_baseinfo_list())
            else:
                return Response(FBMsg.err_req_stock_list())
        else:
            return Response(FBMsg.err_req_shipping_list())
