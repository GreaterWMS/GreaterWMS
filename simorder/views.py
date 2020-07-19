from rest_framework.views import APIView
from rest_framework.response import Response
from utils.datasolve import DataSolve
from utils.fbmsg import FBMsg
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .schemas import ListSchema
from .serializers import StockAnalystSerializers
import os, math, datetime
from shipping.models import ShippingModel
from goods.models import GoodsModel
from baseinfo.models import BaseInfoModel
from users.models import Users
from django.db.models import Sum

@method_decorator(csrf_exempt, name='dispatch')
class SimOrderAPI(APIView):
    '''
        post:
            新增用户
            可以接收一个json数据，也可以接收一个json数据组，但是不可以批量登入
            只有开发者账号的openid才可以发起用户登入请求
    '''
    # schema = BaseInfoSchema()
    def post(self, request, format=None):
        data = DataSolve.datasolve(request)
        try:
            if data['code'] == "1031":
                return Response(FBMsg.err_bad())
        except:
            if ShippingModel.objects.filter(appid=request.user.appid).exists():
                if GoodsModel.objects.filter(appid=request.user.appid).exists():
                    if BaseInfoModel.objects.filter(appid=request.user.appid).exists():
                        if ShippingModel.objects.filter(goods_code=data, appid=request.user.appid).exists():
                            if GoodsModel.objects.filter(goods_code=data, appid=request.user.appid).exists():
                                if BaseInfoModel.objects.filter(goods_code=data, appid=request.user.appid).exists():
                                    on_hand_stock = GoodsModel.objects.filter(goods_code=data, appid=request.user.appid).first().on_hand_stock
                                    lead_time = BaseInfoModel.objects.filter(goods_code=data,
                                                                              appid=request.user.appid).first().total_leadtime
                                    today = datetime.date.today()
                                    delta = datetime.timedelta(days=89)
                                    demand_data = ShippingModel.objects.filter(goods_code=data, appid=request.user.appid,
                                    shipping_time__range=[(today - delta).strftime('%Y-%m-%d'), today])
                                    demand = []
                                    for i in range(len(demand_data)):
                                        demand.append({
                                            "goods_code": data,
                                            "forcast_day": demand_data[i].shipping_time,
                                            "forcast_shipping": demand_data[i].shipping_qty,
                                            "forcast_on_hand": 0,
                                            "plan_order_qty": 0,
                                            "oos": ''
                                        })
                                    for j in range(0, 90):
                                        delta = datetime.timedelta(days=j)
                                        a_date = (today - delta).strftime('%Y-%m-%d')
                                        date = [int(x) for x in a_date.split('-')]
                                        b_date = datetime.date(date[0], date[1], date[2])
                                        check_date = 0
                                        for k in demand:
                                            if (k['forcast_day'] - b_date).days == 0:
                                                check_date = 1
                                        if check_date == 0:
                                            demand.append({
                                                "goods_code": data,
                                                "forcast_day": b_date,
                                                "forcast_shipping": 0,
                                                "forcast_on_hand": 0,
                                                "plan_order_qty": 0,
                                                "oos": ''
                                            })
                                    for k in range(1, 91):
                                        delta = datetime.timedelta(days=k)
                                        plan_date = (today + delta).strftime('%Y-%m-%d')
                                        demand.append({
                                            "goods_code": data,
                                            "forcast_day": plan_date,
                                            "forcast_shipping": 0,
                                            "forcast_on_hand": 0,
                                            "plan_order_qty": 0,
                                            "oos": ''
                                        })
                                    ret = FBMsg.ret()
                                    ret["forcast_on_hand"] = on_hand_stock
                                    ret['lead_time'] = lead_time
                                    ret['data'] = demand
                                    return Response(ret)
                                else:
                                    return Response(FBMsg.err_goods_code())
                            else:
                                return Response(FBMsg.err_goods_code())
                        else:
                            return Response(FBMsg.err_goods_code())
                    else:
                        return Response(FBMsg.err_req_baseinfo_list())
                else:
                    return Response(FBMsg.err_req_stock_list())
            else:
                return Response(FBMsg.err_req_shipping_list())
