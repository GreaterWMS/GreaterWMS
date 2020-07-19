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
from .serializers import ListSerializers, BinListSerializers
from django.conf import settings
import os, math, datetime, binset, property, stocklist, stockbinlist
import pandas as pd
from polist.models import ListModel, DetailModel
from users.models import Users

pathname = '入库单号'
pathlink = 'podetail'

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
        |   property_code   |  int    |  属性权限  |  N   |  接收一个int类型的数字 |
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
                                    "property_code": 1
                                    "create_name": 9,
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
        |   property_code   |   int   | 属性权限 |    Y |  接收任意一个int数字，但是服务器默认1为正常货物   |

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
        put:
            WMS----上传文件
        ---
        # 实现备注:
        **文件限制请看下面介绍，接口不支持测试**<br><br>
        # 参数信息
        |  请求参数    |  类型 |  说明   |  是否必填    |   附加信息 |
        | ---- | ---- | ---- | ---- | ---- |
        |   openid   |   string   | openid |    Y |   openid是必须的参数  |

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
                        格式仅支持xls和xlsx，大小为1M，超过限制上传不会成功
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
        |   name   |   string   | 数据名称 |    Y |   向服务器传字段name，来修改服务器的数据  |
        |   property_code   |   int   | 属性权限 |    Y |  接收任意一个int数字，但是服务器默认1为正常货物   |

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
                        'name': '1'
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
                    file_data = DetailModel.objects.filter(appid=request.user.appid, is_delete=0)
                    file_detail1 = []
                    file_detail2 = []
                    file_detail3 = []
                    file_detail4 = []
                    file_detail5 = []
                    filepath = os.path.join(settings.BASE_DIR, 'media/file/' + pathlink + '/' + request.user.appid + '.xlsx')
                    for i in range(len(file_data)):
                        file_detail1.append(file_data[i].name)
                        file_detail2.append(file_data[i].po_status)
                        file_detail3.append(file_data[i].create_name)
                        file_detail4.append(file_data[i].create_time.strftime("%Y-%m-%d %H:%M:%S"))
                        file_detail5.append(file_data[i].last_update_time.strftime("%Y-%m-%d %H:%M:%S"))
                    df = pd.DataFrame({pathname: file_detail1,
                                       '订单状态': file_detail2,
                                       '创建人': file_detail3,
                                       '创建时间': file_detail4,
                                       '最后更新时间': file_detail5})
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
                list = DetailModel.objects.filter(appid=request.user.appid, is_delete=0).order_by(sort)
                if request._request.GET.get('po_number', ''):
                    list = list.filter(name__icontains=request._request.GET.get('po_number', '')).order_by(sort)
                if request._request.GET.get('po_status', ''):
                    list = list.filter(po_status=int(request._request.GET.get('po_status', ''))).order_by(sort)
                if request._request.GET.get('supplier', ''):
                    list = list.filter(supplier__icontains=request._request.GET.get('supplier', '')).order_by(sort)
                if request._request.GET.get('sorted', ''):
                    list = list.filter(up_qty__gt=int(request._request.GET.get('sorted', ''))).order_by(sort)
                if request._request.GET.get('shortage', ''):
                    list = list.filter(shortage_qty__gt=int(request._request.GET.get('shortage', ''))).order_by(sort)
                if request._request.GET.get('damage', ''):
                    list = list.filter(damage_qty__gt=int(request._request.GET.get('damage', ''))).order_by(sort)
                if request._request.GET.get('more', ''):
                    list = list.filter(more_qty__gt=int(request._request.GET.get('more', ''))).order_by(sort)
                if request._request.GET.get('create_name', ''):
                    list = list.filter(create_name__icontains=request._request.GET.get('create_name', '')).order_by(sort)
                if request._request.GET.get('t_code', ''):
                    list = list.filter(t_code=request._request.GET.get('t_code', '')).order_by(sort)
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
                bin_list = binset.models.ListModel.objects.filter(appid=request.user.appid, is_delete=0).order_by('name')
                bin_list_ser = BinListSerializers(bin_list, many=True)
                ret = FBMsg.ret()
                ret['ip'] = ip
                ret['data'] = list_ser.data
                ret['totlepage'] = math.ceil(list.count()/int(max_page))
                ret['bin_list'] = bin_list_ser.data
                return pg.get_paginated_response(ret)
        else:
            return Response(FBMsg.wms_vip_get())
    def post(self, request, *args, **kwargs):
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
                create_name = Users.objects.filter(openid=request.auth, appid=request.user.appid, is_delete=0).first().name
                if ListModel.objects.filter(appid=request.user.appid, name=str(data[0]['po_number']), is_delete=0).exists():
                    supplier_data = ListModel.objects.filter(appid=request.user.appid, name=str(data[0]['po_number']), is_delete=0).first()
                    supplier_data.supplier = str(data[0]['supplier'])
                    supplier_data.save()
                    for i in range(len(data)):
                        DetailModel.objects.create(appid=request.user.appid, name=str(data[i]['po_number']),
                                                   goods_code=str(data[i]['goods_code']), goods_name=str(data[i]['goods_name']),
                                                   po_qty=int(data[i]['goods_qty']), create_name=create_name,
                                                   supplier=str(data[i]['supplier']), t_code=Md5.md5(str(data[i]['goods_name'])))
                        stock_list_data = stocklist.models.ListModel.objects.filter(appid=request.user.appid,
                                                                                    name=str(data[i]['goods_code']),
                                                                                    is_delete=0).first()
                        stock_list_data.pre_delivery_stock = stock_list_data.pre_delivery_stock + int(data[i]['goods_qty'])
                        stock_list_data.save()
                else:
                    ret = FBMsg.wms_po_empty()
                    ret['data'] = data
                    return Response(ret)
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
                ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                    'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
                po_data = DetailModel.objects.filter(appid=request.user.appid, t_code=str(data[0]['t_code']), is_delete=0).first().name
                po_status_data = ListModel.objects.filter(appid=request.user.appid, name=po_data, is_delete=0).first()
                if po_status_data.po_status == 3:
                    po_status_data.po_status = 4
                    po_status_data.save()
                for i in range(len(data)):
                    patch_data = DetailModel.objects.filter(appid=request.user.appid, t_code=str(data[i]['t_code']), is_delete=0).first()
                    patch_data.arrive_qty = int(data[i]['damage_qty']) + int(data[i]['actual_qty'])
                    more_qty = patch_data.arrive_qty - patch_data.po_qty
                    if more_qty <= 0:
                        patch_data.more_qty = 0
                    else:
                        patch_data.more_qty = more_qty
                    patch_data.damage_qty = int(data[i]['damage_qty'])
                    patch_data.damage_up_qty = int(data[i]['damage_qty'])
                    patch_data.actual_qty = int(data[i]['actual_qty'])
                    patch_data.actual_up_qty = int(data[i]['actual_qty'])
                    patch_data.up_qty = patch_data.arrive_qty
                    if int(data[i]['damage_qty']) + int(data[i]['actual_qty']) < patch_data.po_qty:
                        patch_data.shortage_qty = patch_data.po_qty - (int(data[i]['damage_qty']) + int(data[i]['actual_qty']))
                    else:
                        patch_data.shortage_qty = 0
                    patch_data.po_status = 4
                    stock_list_data = stocklist.models.ListModel.objects.filter(appid=request.user.appid,
                                                                                name=patch_data.goods_code,
                                                                                is_delete=0).first()
                    stock_list_data.pre_sort_stock = stock_list_data.pre_sort_stock - patch_data.arrive_qty
                    stock_list_data.sort_stock = stock_list_data.sort_stock + patch_data.arrive_qty
                    stock_list_data.save()
                    patch_data.save()
                ret = FBMsg.wms_ret()
                ret['ip'] = ip
                ret['data'] = data
                return Response(ret)
        else:
            return Response(FBMsg.wms_vip())

@method_decorator(csrf_exempt, name='dispatch')
class UpAPI(APIView):
    '''
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
        |   property_code   |   int   | 属性权限 |    Y |  接收任意一个int数字，但是服务器默认1为正常货物   |

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
    def post(self, request, *args, **kwargs):
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
                if DetailModel.objects.filter(appid=request.user.appid, t_code=str(data[0]['t_code']), is_delete=0).exists():
                    up_data = DetailModel.objects.filter(t_code=str(data[0]['t_code'])).first()
                    bin_data = binset.models.ListModel.objects.filter(appid=request.user.appid, name=str(data[0]['bin']),
                                                                          is_delete=0).first()
                    property_data = property.models.ListModel.objects.filter(appid=request.user.appid,
                                                                             name=bin_data.bin_property).first()
                    up_data.up_qty = up_data.up_qty - int(data[0]['finish_qty'])
                    goods_stock = stocklist.models.ListModel.objects.filter(appid=request.user.appid,
                                                                            name=up_data.goods_code,
                                                                            goods_name=up_data.goods_name,
                                                                            ).first()
                    if property_data.property_code == 1:
                        up_data.actual_up_qty = up_data.actual_up_qty - int(data[0]['finish_qty'])
                        goods_stock.onhand_stock = goods_stock.onhand_stock + int(data[0]['finish_qty'])
                        goods_stock.can_order_stock = goods_stock.can_order_stock + int(data[0]['finish_qty'])
                        goods_stock.sort_stock = goods_stock.sort_stock - int(data[0]['finish_qty'])
                        if up_data.up_qty > 0:
                            if up_data.actual_up_qty >= 0:
                                up_data.save()
                                goods_stock.save()
                                bin_data.bin_empty = 1
                                bin_data.save()
                                stockbinlist.models.ListModel.objects.create(appid=request.user.appid, name=str(data[0]['bin']),
                                                                             goods_code=up_data.goods_code,
                                                                             goods_name=up_data.goods_name,
                                                                             goods_qty=int(data[0]['finish_qty']),
                                                                             can_order_stock=int(data[0]['finish_qty']),
                                                                             bin_property=bin_data.bin_property,
                                                                             bin_size=bin_data.bin_size,
                                                                             po_name=up_data.name,
                                                                             t_code=Md5.md5(data[0]['t_code']))
                            else:
                                ret = FBMsg.wms_po_qty_up_more()
                                ret['data'] = data
                                return Response(ret)
                        elif up_data.up_qty == 0:
                            if up_data.actual_up_qty >= 0:
                                up_data.save()
                                goods_stock.save()
                                bin_data.bin_empty = 1
                                bin_data.save()
                                stockbinlist.models.ListModel.objects.create(appid=request.user.appid,
                                                                             name=str(data[0]['bin']),
                                                                             goods_code=up_data.goods_code,
                                                                             goods_name=up_data.goods_name,
                                                                             goods_qty=int(data[0]['finish_qty']),
                                                                             can_order_stock=int(data[0]['finish_qty']),
                                                                             bin_property=bin_data.bin_property,
                                                                             bin_size=bin_data.bin_size,
                                                                             po_name=up_data.name,
                                                                             t_code=Md5.md5(data[0]['t_code']))
                                if DetailModel.objects.filter(appid=request.user.appid, name=up_data.name, up_qty__gt=0,
                                                              is_delete=0).exists():
                                    pass
                                else:
                                    po_detail_status = DetailModel.objects.filter(appid=request.user.appid, name=up_data.name,
                                                                                  is_delete=0)
                                    po_list_status = ListModel.objects.filter(appid=request.user.appid, name=up_data.name,
                                                                                  is_delete=0).first()
                                    for i in range(len(po_detail_status)):
                                        po_detail_status[i].po_status = 5
                                        po_detail_status[i].save()
                                    po_list_status.po_status = 5
                                    po_list_status.save()
                            else:
                                ret = FBMsg.wms_po_qty_up_more()
                                ret['data'] = data
                                return Response(ret)
                        else:
                            ret = FBMsg.wms_po_qty_all_up_more()
                            ret['data'] = data
                            return Response(ret)
                    elif property_data.property_code == 4:
                        up_data.damage_up_qty = up_data.damage_up_qty - int(data[0]['finish_qty'])
                        goods_stock.damage_stock = goods_stock.damage_stock + int(data[0]['finish_qty'])
                        if up_data.up_qty > 0:
                            if up_data.damage_up_qty >= 0:
                                up_data.save()
                                goods_stock.save()
                                bin_data.bin_empty = 1
                                bin_data.save()
                                stockbinlist.models.ListModel.objects.create(appid=request.user.appid, name=str(data[0]['bin']),
                                                                             goods_code=up_data.goods_code,
                                                                             goods_name=up_data.goods_name,
                                                                             goods_qty=int(data[0]['finish_qty']),
                                                                             bin_property=bin_data.bin_property,
                                                                             bin_size=bin_data.bin_size,
                                                                             po_name=up_data.name,
                                                                             t_code=Md5.md5(data[0]['t_code']))
                            else:
                                ret = FBMsg.wms_po_qty_dup_more()
                                ret['data'] = data
                                return Response(ret)
                        elif up_data.up_qty == 0:
                            if up_data.damage_up_qty >= 0:
                                up_data.save()
                                goods_stock.save()
                                bin_data.bin_empty = 1
                                bin_data.save()
                                stockbinlist.models.ListModel.objects.create(appid=request.user.appid,
                                                                             name=str(data[0]['bin']),
                                                                             goods_code=up_data.goods_code,
                                                                             goods_name=up_data.goods_name,
                                                                             goods_qty=int(data[0]['finish_qty']),
                                                                             bin_property=bin_data.bin_property,
                                                                             bin_size=bin_data.bin_size,
                                                                             po_name=up_data.name,
                                                                             t_code=Md5.md5(data[0]['t_code']))
                                if DetailModel.objects.filter(appid=request.user.appid, name=up_data.name, up_qty__gt=0,
                                                              is_delete=0).exists():
                                    pass
                                else:
                                    po_detail_status = DetailModel.objects.filter(appid=request.user.appid, name=up_data.name,
                                                                                  is_delete=0)
                                    po_list_status = ListModel.objects.filter(appid=request.user.appid, name=up_data.name,
                                                                                  is_delete=0).first()
                                    for i in range(len(po_detail_status)):
                                        po_detail_status[i].po_status = 5
                                        po_detail_status[i].save()
                                    po_list_status.po_status = 5
                                    po_list_status.save()
                            else:
                                ret = FBMsg.wms_po_qty_dup_more()
                                ret['data'] = data
                                return Response(ret)
                        else:
                            ret = FBMsg.wms_po_qty_all_up_more()
                            ret['data'] = data
                            return Response(ret)
                else:
                    ret = FBMsg.wms_po_empty()
                    ret['data'] = data
                    return Response(ret)
                ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                    'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
                ret = FBMsg.wms_ret()
                ret['ip'] = ip
                ret['data'] = data
                return Response(ret)
        else:
            return Response(FBMsg.wms_vip())
