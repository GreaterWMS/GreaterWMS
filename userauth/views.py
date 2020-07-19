from rest_framework.views import APIView
from rest_framework.response import Response
from utils.datasolve import DataSolve
from utils.page import MyPageNumberPagination
from utils.fbmsg import FBMsg
from utils.md5 import Md5
from utils.file_vip_check import FileVipCheck
from utils.vip_check import VipCheck
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .schemas import APISchema
from .serializers import ListSerializers
from django.conf import settings
import os, math, datetime
import pandas as pd
from users.models import UserAuth
from users.models import Users

pathname = '权限名称'
pathlink = 'userauth'


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
        |   create_name   |  string    |  创建人  |  N   |  该条数据是由谁创建的 |
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
                                    "create_name": 9,
                                    "aut<int>": 1或者0,
                                    "t_code": *********,
                                    "create_time": "2020-05-20 10:59:30",
                                    "last_update_time": "2020-05-20 10:59:30"
                                }
                            ],
                            "totlepage": 523
                        }
                    }
        post:
            WMS----创建数据
        ---
        # 实现备注:
        **一次只能创建一条数据**<br><br>
        # 参数信息
        |  请求参数    |  类型 |  说明   |  是否必填    |   附加信息 |
        | ---- | ---- | ---- | ---- | ---- |
        |   openid   |   string   | openid |    Y |   openid是必须的参数  |
        |   name   |   string   | 数据名称 |    Y |  服务器会根据上传的字段name，来保存数据   |
        |   aut<int>   |   int   | 权限名 |    Y |  权限名可以自己前端定义不同页面的访问权限，也可以设定为不同API的访问权限   |

        |  响应参数    |  类型 |  说明    |
        | ---- | ---- | ---- |
        |   code   |   string   | 响应结果码  |
        |   msg   |  string    |   响应结果信息  |
        |   ip   |  string    |   请求发起的ip  |
        |   data   |  JSON    |  返回数据   |

        ## 响应code说明
        |  Code    |  Description    |
        | ---- | ---- |
        |   200   |   请求成功   |
        # 示例:
        ## request:
                - body:
                    Example value:
                    {
                        'name': '1',
                    }
        ## response:
                - body:
                     Example value:
                     {
                        "code": "200",
                        "msg": "操作成功",
                        "data": null,
                        "ip": "127.0.0.1"
                    }
        patch:
            WMS----修改数据
        ---
        # 实现备注:
        **一次只能修改一条数据**<br><br>
        # 参数信息
        |  请求参数    |  类型 |  说明   |  是否必填    |   附加信息 |
        | ---- | ---- | ---- | ---- | ---- |
        |   openid   |   string   | openid |    Y |   openid是必须的参数  |
        |   t_code   |   string   | 数据唯一码 |    Y |   该条数据在数据库中的唯一标识  |
        |   name   |   string   | 数据名称 |    N |   向服务器传字段name，来修改服务器的数据  |
        |   aut<int>   |   int   | 权限名 |    N |  权限名可以自己前端定义不同页面的访问权限，也可以设定为不同API的访问权限   |

        |  响应参数    |  类型 |  说明    |
        | ---- | ---- | ---- |
        |   code   |   string   | 响应结果码  |
        |   msg   |  string    |   响应结果信息  |
        |   ip   |  string    |   请求发起的ip  |
        |   data   |  JSON    |  返回数据   |

        ## 响应code说明
        |  Code    |  Description    |
        | ---- | ---- |
        |   200   |   请求成功   |
        # 示例:
        ## request:
                - body:
                    Example value:
                    {
                        't_code: '********************',
                        'name': '1',
                        'aut<int>': 1或者0
                    }
        ## response:
                - body:
                     Example value:
                     {
                        "code": "200",
                        "msg": "操作成功",
                        "data": null,
                        "ip": "127.0.0.1"
                    }
        delete:
            WMS----删除数据
        ---
        # 实现备注:
        **可批量删除数据**<br><br>
        # 参数信息
        |  请求参数    |  类型 |  说明   |  是否必填    |   附加信息 |
        | ---- | ---- | ---- | ---- | ---- |
        |   openid   |   string   | openid |    Y |   openid是必须的参数  |
        |   t_code   |   string   | 数据唯一码 |    Y |   该条数据在数据库中的唯一标识  |

        |  响应参数    |  类型 |  说明    |
        | ---- | ---- | ---- |
        |   code   |   string   | 响应结果码  |
        |   msg   |  string    |   响应结果信息  |
        |   ip   |  string    |   请求发起的ip  |
        |   data   |  JSON    |  返回数据   |

        ## 响应code说明
        |  Code    |  Description    |
        | ---- | ---- |
        |   200   |   请求成功   |
        # 示例:
        ## request:
                - body:
                    Example value:
                    {
                        't_code: '********************'
                    }
        ## response:
                - body:
                     Example value:
                     {
                        "code": "200",
                        "msg": "操作成功",
                        "data": null,
                        "ip": "127.0.0.1"
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
                    file_data = UserAuth.objects.filter(appid=request.user.appid, is_delete=0)
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
                    file_detail17 = []
                    file_detail18 = []
                    file_detail19 = []
                    file_detail20 = []
                    file_detail21 = []
                    file_detail22 = []
                    file_detail23 = []
                    filepath = os.path.join(settings.BASE_DIR,
                                            'media/file/' + pathlink + '/' + request.user.appid + '.xlsx')
                    for i in range(len(file_data)):
                        file_detail1.append(file_data[i].name)
                        file_detail2.append(file_data[i].aut1)
                        file_detail3.append(file_data[i].aut2)
                        file_detail4.append(file_data[i].aut3)
                        file_detail5.append(file_data[i].aut4)
                        file_detail6.append(file_data[i].aut5)
                        file_detail7.append(file_data[i].aut6)
                        file_detail8.append(file_data[i].aut7)
                        file_detail9.append(file_data[i].aut8)
                        file_detail10.append(file_data[i].aut9)
                        file_detail11.append(file_data[i].aut10)
                        file_detail12.append(file_data[i].aut11)
                        file_detail13.append(file_data[i].aut12)
                        file_detail14.append(file_data[i].aut13)
                        file_detail15.append(file_data[i].aut14)
                        file_detail16.append(file_data[i].aut15)
                        file_detail17.append(file_data[i].aut16)
                        file_detail18.append(file_data[i].aut17)
                        file_detail19.append(file_data[i].aut18)
                        file_detail20.append(file_data[i].aut19)
                        file_detail21.append(file_data[i].aut20)
                        file_detail22.append(file_data[i].create_time.strftime("%Y-%m-%d %H:%M:%S"))
                        file_detail23.append(file_data[i].last_update_time.strftime("%Y-%m-%d %H:%M:%S"))
                    df = pd.DataFrame({pathname: file_detail1, 'aut1': file_detail2, 'aut2': file_detail3, 'aut3': file_detail4,
                                       'aut4': file_detail5, 'aut5': file_detail6, 'aut6': file_detail7, 'aut7': file_detail2,
                                       'aut8': file_detail9, 'aut9': file_detail10, 'aut10': file_detail11, 'aut11': file_detail12,
                                       'aut12': file_detail13, 'aut13': file_detail14, 'aut14': file_detail15,
                                       'aut15': file_detail16, 'aut16': file_detail17, 'aut17': file_detail18,
                                       'aut18': file_detail19, 'aut19': file_detail20, 'aut20': file_detail21,
                                       '创建时间': file_detail22, '最后更新时间': file_detail23})
                    dir_path = os.path.join(settings.BASE_DIR, 'media/file/' + pathlink + '/')
                    if os.path.exists(dir_path):
                        pass
                    else:
                        os.makedirs(dir_path)
                    if os.path.isfile(filepath):
                        os.remove(filepath)
                    else:
                        pass
                    df.to_excel(filepath, sheet_name='sheet1', index=False, encoding='utf-8')
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
                list = UserAuth.objects.filter(appid=request.user.appid, is_delete=0).order_by(sort)
                if request._request.GET.get('name', ''):
                    list = list.filter(name__icontains=request._request.GET.get('name', '')).order_by(sort)
                if request._request.GET.get('create_name', ''):
                    list = list.filter(create_name__icontains=request._request.GET.get('create_name', '')).order_by(
                        sort)
                if request._request.GET.get('authorization', ''):
                    if str(request._request.GET.get('authorization', '')) == "1":
                        auth_name = Users.objects.filter(appid=request.user.appid, openid=request.auth,
                                                         is_delete=0).first().auth_name
                        list = list.filter(appid=request.user.appid, name=auth_name, is_delete=0).order_by(sort)
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
                ret['totlepage'] = math.ceil(list.count() / int(max_page))
                return pg.get_paginated_response(ret)
        else:
            return Response(FBMsg.wms_vip_get())

    def post(self, request, *args, **kwargs):
        global aut1, aut2
        vip_id = Users.objects.filter(appid=request.user.appid, developer=1, is_delete=0).first().vip
        vip_check = VipCheck.VipCheck(vip_id)
        if vip_check == "N":
            return Response(FBMsg.wms_vip())
        elif vip_check == "Y":
            data = DataSolve.datasolve(request)
            try:
                if data['code'] == "1031":
                    return Response(FBMsg.err_bad())
            except:
                if UserAuth.objects.filter(appid=request.user.appid, name=data['name'], is_delete=0).exists():
                    ret = FBMsg.wms_same()
                    ret['data'] = data
                    return Response(ret)
                else:
                    create_name = Users.objects.filter(openid=request.auth, appid=request.user.appid,
                                                       is_delete=0).first().name
                    if 'aut1' in data:
                        if str(data['aut1']) == "1":
                            aut1 = 1
                        else:
                            aut1 = 0
                    else:
                        aut1 = 0
                    if 'aut2' in data:
                        if str(data['aut2']) == "1":
                            aut2 = 1
                        else:
                            aut2 = 0
                    else:
                        aut2 = 0
                    if 'aut3' in data:
                        if str(data['aut3']) == "1":
                            aut3 = 1
                        else:
                            aut3 = 0
                    else:
                        aut3 = 0
                    if 'aut4' in data:
                        if str(data['aut4']) == "1":
                            aut4 = 1
                        else:
                            aut4 = 0
                    else:
                        aut4 = 0
                    if 'aut5' in data:
                        if str(data['aut5']) == "1":
                            aut5 = 1
                        else:
                            aut5 = 0
                    else:
                        aut5 = 0
                    if 'aut6' in data:
                        if str(data['aut6']) == "1":
                            aut6 = 1
                        else:
                            aut6 = 0
                    else:
                        aut6 = 0
                    if 'aut7' in data:
                        if str(data['aut7']) == "1":
                            aut7 = 1
                        else:
                            aut7 = 0
                    else:
                        aut7 = 0
                    if 'aut8' in data:
                        if str(data['aut8']) == "1":
                            aut8 = 1
                        else:
                            aut8 = 0
                    else:
                        aut8 = 0
                    if 'aut9' in data:
                        if str(data['aut9']) == "1":
                            aut9 = 1
                        else:
                            aut9 = 0
                    else:
                        aut9 = 0
                    if 'aut10' in data:
                        if str(data['aut10']) == "1":
                            aut10 = 1
                        else:
                            aut10 = 0
                    else:
                        aut10 = 0
                    if 'aut11' in data:
                        if str(data['aut11']) == "1":
                            aut11 = 1
                        else:
                            aut11 = 0
                    else:
                        aut11 = 0
                    if 'aut12' in data:
                        if str(data['aut12']) == "1":
                            aut12 = 1
                        else:
                            aut12 = 0
                    else:
                        aut12 = 0
                    if 'aut13' in data:
                        if str(data['aut13']) == "1":
                            aut13 = 1
                        else:
                            aut13 = 0
                    else:
                        aut13 = 0
                    if 'aut14' in data:
                        if str(data['aut14']) == "1":
                            aut14 = 1
                        else:
                            aut14 = 0
                    else:
                        aut14 = 0
                    if 'aut15' in data:
                        if str(data['aut15']) == "1":
                            aut15 = 1
                        else:
                            aut15 = 0
                    else:
                        aut15 = 0
                    if 'aut16' in data:
                        if str(data['aut16']) == "1":
                            aut16 = 1
                        else:
                            aut16 = 0
                    else:
                        aut16 = 0
                    if 'aut17' in data:
                        if str(data['aut17']) == "1":
                            aut17 = 1
                        else:
                            aut17 = 0
                    else:
                        aut17 = 0
                    if 'aut18' in data:
                        if str(data['aut18']) == "1":
                            aut18 = 1
                        else:
                            aut18 = 0
                    else:
                        aut18 = 0
                    if 'aut19' in data:
                        if str(data['aut19']) == "1":
                            aut19 = 1
                        else:
                            aut19 = 0
                    else:
                        aut19 = 0
                    if 'aut20' in data:
                        if str(data['aut20']) == "1":
                            aut20 = 1
                        else:
                            aut20 = 0
                    else:
                        aut20 = 0
                    UserAuth.objects.create(appid=request.user.appid, name=str(data['name']), create_name=create_name,
                                            t_code=Md5.md5(str(data['name'])), aut1=aut1, aut2=aut2, aut3=aut3,
                                            aut4=aut4,
                                            aut5=aut5, aut6=aut6, aut7=aut7, aut8=aut8, aut9=aut9, aut10=aut10,
                                            aut11=aut11,
                                            aut12=aut12, aut13=aut13, aut14=aut14, aut15=aut15, aut16=aut16,
                                            aut17=aut17, aut18=aut18, aut19=aut19, aut20=aut20)
                    ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                        'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
                    ret = FBMsg.wms_ret()
                    ret['ip'] = ip
                    ret['data'] = data
                    return Response(ret)
        else:
            return Response(FBMsg.wms_vip())

    def patch(self, request, *args, **kwargs):
        vip_id = Users.objects.filter(appid=request.user.appid, developer=1, is_delete=0).first().vip
        vip_check = VipCheck.VipCheck(vip_id)
        if vip_check == "N":
            return Response(FBMsg.wms_vip())
        elif vip_check == "Y":
            data = DataSolve.datasolve(request)
            try:
                if data['code'] == "1031":
                    return Response(FBMsg.err_bad())
            except:
                if UserAuth.objects.filter(appid=request.user.appid, t_code=data['t_code'], is_delete=0).exists():
                    patch_name = UserAuth.objects.get(t_code=data['t_code']).name
                    if patch_name != data['name']:
                        if UserAuth.objects.filter(appid=request.user.appid, name=data['name'], is_delete=0).exists():
                            ret = FBMsg.wms_same()
                            ret['data'] = data
                            return Response(ret)
                    patch_data = UserAuth.objects.filter(appid=request.user.appid, t_code=data['t_code'],
                                                         is_delete=0).first()
                    if 'name' in data:
                        patch_data.name = data['name']
                    if 'aut1' in data:
                        if str(data['aut1']) == "1":
                            patch_data.aut1 = int(data['aut1'])
                        elif str(data['aut1']) == "0":
                            patch_data.aut1 = int(data['aut1'])
                    if 'aut2' in data:
                        if str(data['aut2']) == "1":
                            patch_data.aut2 = int(data['aut2'])
                        elif str(data['aut2']) == "0":
                            patch_data.aut2 = int(data['aut2'])
                    if 'aut3' in data:
                        if str(data['aut3']) == "1":
                            patch_data.aut3 = int(data['aut3'])
                        elif str(data['aut3']) == "0":
                            patch_data.aut3 = int(data['aut3'])
                    if 'aut4' in data:
                        if str(data['aut4']) == "1":
                            patch_data.aut4 = int(data['aut4'])
                        elif str(data['aut4']) == "0":
                            patch_data.aut4 = int(data['aut4'])
                    if 'aut5' in data:
                        if str(data['aut5']) == "1":
                            patch_data.aut5 = int(data['aut5'])
                        elif str(data['aut5']) == "0":
                            patch_data.aut5 = int(data['aut5'])
                    if 'aut6' in data:
                        if str(data['aut6']) == "1":
                            patch_data.aut6 = int(data['aut6'])
                        elif str(data['aut6']) == "0":
                            patch_data.aut6 = int(data['aut6'])
                    if 'aut7' in data:
                        if str(data['aut7']) == "1":
                            patch_data.aut7 = int(data['aut7'])
                        elif str(data['aut7']) == "0":
                            patch_data.aut7 = int(data['aut7'])
                    if 'aut8' in data:
                        if str(data['aut8']) == "1":
                            patch_data.aut8 = int(data['aut8'])
                        elif str(data['aut8']) == "0":
                            patch_data.aut8 = int(data['aut8'])
                    if 'aut9' in data:
                        if str(data['aut9']) == "1":
                            patch_data.aut9 = int(data['aut9'])
                        elif str(data['aut9']) == "0":
                            patch_data.aut9 = int(data['aut9'])
                    if 'aut10' in data:
                        if str(data['aut10']) == "1":
                            patch_data.aut10 = int(data['aut10'])
                        elif str(data['aut10']) == "0":
                            patch_data.aut10 = int(data['aut10'])
                    if 'aut11' in data:
                        if str(data['aut11']) == "1":
                            patch_data.aut11 = int(data['aut11'])
                        elif str(data['aut11']) == "0":
                            patch_data.aut11 = int(data['aut11'])
                    if 'aut12' in data:
                        if str(data['aut12']) == "1":
                            patch_data.aut12 = int(data['aut12'])
                        elif str(data['aut12']) == "0":
                            patch_data.aut12 = int(data['aut12'])
                    if 'aut13' in data:
                        if str(data['aut13']) == "1":
                            patch_data.aut13 = int(data['aut13'])
                        elif str(data['aut13']) == "0":
                            patch_data.aut13 = int(data['aut13'])
                    if 'aut14' in data:
                        if str(data['aut14']) == "1":
                            patch_data.aut14 = int(data['aut14'])
                        elif str(data['aut14']) == "0":
                            patch_data.aut14 = int(data['aut14'])
                    if 'aut15' in data:
                        if str(data['aut15']) == "1":
                            patch_data.aut15 = int(data['aut15'])
                        elif str(data['aut15']) == "0":
                            patch_data.aut15 = int(data['aut15'])
                    if 'aut15' in data:
                        if str(data['aut15']) == "1":
                            patch_data.aut15 = int(data['aut15'])
                        elif str(data['aut15']) == "0":
                            patch_data.aut15 = int(data['aut15'])
                    if 'aut15' in data:
                        if str(data['aut15']) == "1":
                            patch_data.aut15 = int(data['aut15'])
                        elif str(data['aut15']) == "0":
                            patch_data.aut15 = int(data['aut15'])
                    if 'aut16' in data:
                        if str(data['aut16']) == "1":
                            patch_data.aut16 = int(data['aut16'])
                        elif str(data['aut16']) == "0":
                            patch_data.aut16 = int(data['aut16'])
                    if 'aut17' in data:
                        if str(data['aut17']) == "1":
                            patch_data.aut17 = int(data['aut17'])
                        elif str(data['aut17']) == "0":
                            patch_data.aut17 = int(data['aut17'])
                    if 'aut18' in data:
                        if str(data['aut18']) == "1":
                            patch_data.aut18 = int(data['aut18'])
                        elif str(data['aut18']) == "0":
                            patch_data.aut18 = int(data['aut18'])
                    if 'aut19' in data:
                        if str(data['aut19']) == "1":
                            patch_data.aut19 = int(data['aut19'])
                        elif str(data['aut19']) == "0":
                            patch_data.aut19 = int(data['aut19'])
                    if 'aut20' in data:
                        if str(data['aut20']) == "1":
                            patch_data.aut20 = int(data['aut20'])
                        elif str(data['aut20']) == "0":
                            patch_data.aut20 = int(data['aut20'])
                    patch_data.save()
                    ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                        'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
                    ret = FBMsg.wms_ret()
                    ret['ip'] = ip
                    ret['data'] = data
                    return Response(ret)
                else:
                    ret = FBMsg.wms_err()
                    ret['data'] = data
                    return Response(ret)
        else:
            return Response(FBMsg.wms_vip())
    def delete(self, request, *args, **kwargs):
        vip_id = Users.objects.filter(appid=request.user.appid, developer=1, is_delete=0).first().vip
        vip_check = VipCheck.VipCheck(vip_id)
        if vip_check == "N":
            return Response(FBMsg.wms_vip())
        elif vip_check == "Y":
            data = DataSolve.datasolve(request)
            for i in range(len(data)):
                if UserAuth.objects.filter(appid=request.user.appid, t_code=data[i]['t_code'], is_delete=0).exists():
                    pass
                else:
                    ret = FBMsg.wms_err()
                    ret['data'] = data
                    return Response(ret)
            for j in range(len(data)):
                delete_data = UserAuth.objects.filter(appid=request.user.appid, t_code=data[j]['t_code'],
                                                      is_delete=0).first()
                delete_data.is_delete = 1
                delete_data.save()
                user_auth_change = Users.objects.filter(appid=request.user.appid, auth_name=delete_data.name,
                                                        is_delete=0)
                for k in range(len(user_auth_change)):
                    user_auth_change[k].auth_name = ''
                    user_auth_change[k].save()
            ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
            ret = FBMsg.wms_ret()
            ret['ip'] = ip
            ret['data'] = data
            return Response(ret)
        else:
            return Response(FBMsg.wms_vip())
