from rest_framework.views import APIView
from rest_framework.response import Response
from utils.page import MyPageNumberPagination
from utils.fbmsg import FBMsg
from utils.vip_check import VipCheck
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .schemas import APISchema
from .serializers import ListSerializers
from django.conf import settings
import os, math, datetime
import pandas as pd
from .models import ListModel
from users.models import Users

pathname = '库存列表'
pathlink = 'stocklist'

@method_decorator(csrf_exempt, name='dispatch')
class API(APIView):
    '''
        get:
            WMS----获取数据
        ---
        # 实现备注:
        **获取数据列表**<br><br>
        # 参数信息
        |  请求参数    |  类型 |  说明   |  是否必填    |   附加信息 |
        | ---- | ---- | ---- | ---- | ---- |
        |   openid   |   string   | openid |    Y |   openid是必须的参数  |
        |   getfile   |  string    |  下载数据  |  N   |  将数据以excel表格形式下载下来，请求值为"1" |
        |   name   |   string   | 名称 |    N |   结果为模糊查询  |
        |   create_name   |   string   | 创建人 |    N |   结果为模糊查询  |
        |   page   |  int    |   页数  |  N  |  显示哪一页的数据  |
        |   max_page   |  int    |  每页数据条数  |  N   |  max_page在0~1000之间，默认为100 |
        |   sort   |  string    |  排序  |  N   |  请求的数据进行排序，例： "sort": "-create_time" |
        |   date1   |  date    |  根据创建时间查询数据的起始日期  |  N   |  格式 "date1": "2020/01/01" |
        |   date2   |  date    |  根据创建时间查询数据的结束日期  |  N   |  格式 "date2": "2020/01/01"， 默认为今天 |
        |   udate1   |  date    |  根据最后更新时间查询数据的起始日期  |  N   |  格式 "udate1": "2020/01/01" |
        |   udate2   |  date    |  根据最后更新时间查询数据的结束日期  |  N   |  格式 "udate2": "2020/01/01"， 默认为今天 |

        |  响应参数    |  类型 |  说明    |
        | ---- | ---- | ---- |
        |   count   |   int   | 总共多少条数据  |
        |   next   |   string   | 下一页链接  |
        |   previous   |   string   | 上一页链接  |
        |   results   |   string   | 返回的信息结果 |
        |   code   |   string   | 响应结果码  |
        |   msg   |  string    |   响应结果信息  |
        |   ip   |  string    |   请求发起的ip  |
        |   data   |  JSON    |  返回的数据   |
        |   totlepage   |  int    |  总共多少页数据   |

        ## 响应code说明
        |  Code    |  Description    |
        | ---- | ---- |
        |   200   |   请求成功   |
        # 示例:
        ## request:
                - body:
                    Example value:
                    {
                        'openid': '你的openid',
                        'page': 2,
                        'max_page': 1
                    }

        ## response:
                - body:
                     Example value:
                     {
                        "count": 523,
                        "next": "https://scmapi.56yhz.com/baseinfo/list/?max_page=1&page=3&openid={ 你的openid }",
                        "previous": "https://scmapi.56yhz.com/baseinfo/list/?page=1&max_page=10&openid={ 你的openid }",
                        "results": {
                            "code": "200",
                            "msg": "请求完成",
                            "ip": "127.0.0.1",
                            "data": [
                                {
                                    "name": "A522",
                                    "创建人": "***",
                                    "t_code": *********,
                                    "create_time": "2020-05-20 10:59:30",
                                    "last_update_time": "2020-05-20 10:59:30"
                                }
                            ],
                            "totlepage": 523
                        }
                    }
        <br>
        responses:
            400:
              description: "Invalid ID supplied"
            404:
              description: "Pet not found"
            405:
              description: "Validation exception"
    '''
    schema = APISchema()
    def get(self, request, *args, **kwargs):
        vip_id = Users.objects.filter(appid=request.user.appid, developer=1, is_delete=0).first().vip
        vip_check = VipCheck.VipCheck(vip_id)
        if vip_check == "N":
            return Response(FBMsg.wms_vip_get())
        elif vip_check == "Y":
            if request._request.GET.get('getfile', ''):
                if str(request._request.GET.get('getfile', '')) == "1":
                    file_data = ListModel.objects.filter(appid=request.user.appid, is_delete=0)
                    file_detail1 = []
                    file_detail2 = []
                    file_detail3 = []
                    file_detail4 = []
                    file_detail5 = []
                    file_detail6 = []
                    file_detail7 = []
                    file_detail8 = []
                    file_detail9 = []
                    file_detail10 = []
                    file_detail11 = []
                    file_detail12 = []
                    file_detail13 = []
                    file_detail14 = []
                    file_detail15 = []
                    file_detail16 = []
                    filepath = os.path.join(settings.BASE_DIR, 'media/file/' + pathlink + '/' + request.user.appid + '.xlsx')
                    for i in range(len(file_data)):
                        file_detail1.append(file_data[i].name)
                        file_detail2.append(file_data[i].goods_name)
                        file_detail3.append(file_data[i].onhand_stock)
                        file_detail4.append(file_data[i].inspect_stock)
                        file_detail5.append(file_data[i].cross_stock)
                        file_detail6.append(file_data[i].hold_stock)
                        file_detail7.append(file_data[i].damage_stock)
                        file_detail8.append(file_data[i].pre_delivery_stock)
                        file_detail9.append(file_data[i].pre_load_stock)
                        file_detail10.append(file_data[i].load_stock)
                        file_detail11.append(file_data[i].sort_stock)
                        file_detail12.append(file_data[i].pick_stock)
                        file_detail13.append(file_data[i].picked_stock)
                        file_detail14.append(file_data[i].oos_stock)
                        file_detail15.append(file_data[i].create_time.strftime("%Y-%m-%d %H:%M:%S"))
                        file_detail16.append(file_data[i].last_update_time.strftime("%Y-%m-%d %H:%M:%S"))
                    df = pd.DataFrame({pathname: file_detail1,
                                       '商品描述': file_detail2,
                                       '现有库存': file_detail3,
                                       '待检库存': file_detail4,
                                       '暂存库存': file_detail5,
                                       '不可发库存': file_detail6,
                                       '破损库存': file_detail7,
                                       '预计到货库存': file_detail8,
                                       '待卸货库存': file_detail9,
                                       '实际到货库存': file_detail10,
                                       '待上架库存': file_detail11,
                                       '待拣货库存': file_detail12,
                                       '待发货库存': file_detail13,
                                       '欠货库存': file_detail14,
                                       '创建时间': file_detail15,
                                       '最后更新时间': file_detail16})
                    dir_path = os.path.join(settings.BASE_DIR, 'media/file/' + pathlink + '/')
                    if os.path.exists(dir_path):
                        pass
                    else:
                        os.makedirs(dir_path)
                    if os.path.isfile(filepath):
                        os.remove(filepath)
                    else:
                        pass
                    df.to_excel(filepath, sheet_name='sheet1', startcol=0, index=False)
                    file = open(filepath, 'rb')
                    response = FileResponse(file)
                    response['Content-Type'] = 'application/octet-stream'
                    response['Content-Disposition'] = 'attachment;filename="%s.xlsx"' % pathlink
                    return response
                else:
                    ret = FBMsg.wms_errfile()
                    return Response(ret)
            else:
                sort = request._request.GET.get('sort', '-create_time')
                max_page = request._request.GET.get('max_page', 100)
                list = ListModel.objects.filter(appid=request.user.appid, is_delete=0).order_by(sort)
                if request._request.GET.get('name', ''):
                    list = list.filter(name__icontains=str(request._request.GET.get('name', ''))).order_by(sort)
                if request._request.GET.get('goods_name', ''):
                    list = list.filter(goods_name__icontains=str(request._request.GET.get('goods_name', ''))).order_by(sort)
                if request._request.GET.get('date1', ''):
                    try:
                        start_date = request._request.GET.get('date1', '')
                        date = [int(x) for x in start_date.split('/')]
                        new = datetime.datetime(date[0], date[1], date[2])
                        start_date = new.strftime('%Y-%m-%d')
                        if request._request.GET.get('date2', ''):
                            date_end = request._request.GET.get('date2', '')
                            delta = datetime.timedelta(days=1)
                            date = [int(x) for x in date_end.split('/')]
                            old = datetime.datetime(date[0], date[1], date[2])
                            end_date = (old + delta).strftime('%Y-%m-%d')
                        else:
                            today = datetime.date.today()
                            delta = datetime.timedelta(days=1)
                            end_date = (today + delta).strftime('%Y-%m-%d')
                            date = [int(x) for x in end_date.split('-')]
                            old = datetime.datetime(date[0], date[1], date[2])
                        if (old - new).days < 0:
                            return Response(FBMsg.wms_time())
                        else:
                            list = list.filter(create_time__range=[start_date, end_date]).order_by(sort)
                    except:
                        pass
                if request._request.GET.get('udate1', ''):
                    try:
                        start_date = request._request.GET.get('udate1', '')
                        date = [int(x) for x in start_date.split('/')]
                        new = datetime.datetime(date[0], date[1], date[2])
                        start_date = new.strftime('%Y-%m-%d')
                        if request._request.GET.get('udate2', ''):
                            date_end = request._request.GET.get('udate2', '')
                            delta = datetime.timedelta(days=1)
                            date = [int(x) for x in date_end.split('/')]
                            old = datetime.datetime(date[0], date[1], date[2])
                            end_date = (old + delta).strftime('%Y-%m-%d')
                        else:
                            today = datetime.date.today()
                            delta = datetime.timedelta(days=1)
                            end_date = (today + delta).strftime('%Y-%m-%d')
                            date = [int(x) for x in end_date.split('-')]
                            old = datetime.datetime(date[0], date[1], date[2])
                        if (old - new).days < 0:
                            return Response(FBMsg.wms_time())
                        else:
                            list = list.filter(last_update_time__range=[start_date, end_date]).order_by(sort)
                    except:
                        pass
                pg = MyPageNumberPagination()
                pg_list = pg.paginate_queryset(queryset=list, request=request, view=self)
                list_ser = ListSerializers(pg_list, many=True)
                ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                    'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
                ret = FBMsg.ret()
                ret['ip'] = ip
                ret['data'] = list_ser.data
                ret['totlepage'] = math.ceil(list.count()/int(max_page))
                return pg.get_paginated_response(ret)
        else:
            return Response(FBMsg.wms_vip_get())
