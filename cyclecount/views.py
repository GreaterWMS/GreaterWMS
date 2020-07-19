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
import os, math, datetime, random, binset, goodslist, stockbinlist
import pandas as pd
from .models import ListModel
from users.models import Users

pathname = '库位名称'
pathlink = 'cyclecount'

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
        |   name   |   string   | 商品编码 |    N |   结果为模糊查询  |
        |   goods_name   |   string   | 商品名称 |    N |   结果为模糊查询  |
        |   goods_unit   |   string   | 商品单位 |    N |   结果为模糊查询  |
        |   goods_class   |   string   | 商品类别 |    N |   结果为模糊查询  |
        |   goods_spacs   |   string   | 商品规格 |    N |   结果为模糊查询  |
        |   goods_shape   |   string   | 商品形状 |    N |   结果为模糊查询  |
        |   goods_color   |   string   | 商品颜色 |    N |   结果为模糊查询  |
        |   goods_brand   |   string   | 商品品牌 |    N |   结果为模糊查询  |
        |   goods_city   |   string   | 商品产地 |    N |   结果为模糊查询  |
        |   goods_ood   |   int   | 保质期 |    N |   结果为模糊查询  |
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
        |   name   |   string   | 数据名称 |    N |   向服务器传字段name，来修改服务器的数据  |

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
                    file_data = stockbinlist.models.ListModel.objects.filter(appid=request.user.appid, is_delete=0).order_by('name')
                    file_detail1 = []
                    file_detail2 = []
                    file_detail3 = []
                    file_detail4 = []
                    file_detail5 = []
                    filepath = os.path.join(settings.BASE_DIR, 'media/file/' + pathlink + '/' + request.user.appid + '.xlsx')
                    for i in range(len(file_data)):
                        file_detail1.append(file_data[i].name)
                        file_detail2.append(file_data[i].goods_code)
                        file_detail3.append(file_data[i].goods_name)
                        file_detail4.append('')
                        file_detail5.append(file_data[i].t_code)
                    df = pd.DataFrame({pathname: file_detail1,
                                       '商品编码': file_detail2,
                                       '商品描述': file_detail3,
                                       '盘点用户名': file_detail4,
                                       '数据标识': file_detail5
                                       })
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
                    response['Content-Disposition'] = 'attachment;filename="cyclecountlist.xlsx"'
                    return response
                if str(request._request.GET.get('getfile', '')) == "2":
                    file_data = ListModel.objects.filter(appid=request.user.appid)
                    file_detail1 = []
                    file_detail2 = []
                    file_detail3 = []
                    file_detail4 = []
                    file_detail5 = []
                    file_detail6 = []
                    file_detail7 = []
                    file_detail8 = []
                    file_detail9 = []
                    filepath = os.path.join(settings.BASE_DIR, 'media/file/' + pathlink + '/' + request.user.appid + '.xlsx')
                    for i in range(len(file_data)):
                        file_detail1.append(file_data[i].name)
                        file_detail2.append(file_data[i].goods_code)
                        file_detail3.append(file_data[i].goods_name)
                        file_detail4.append(file_data[i].goods_qty)
                        file_detail5.append(file_data[i].cycle_count_balance)
                        file_detail6.append(file_data[i].staff)
                        file_detail7.append(file_data[i].inbound_time.strftime("%Y-%m-%d %H:%M:%S"))
                        file_detail8.append(file_data[i].create_time.strftime("%Y-%m-%d %H:%M:%S"))
                        file_detail9.append(file_data[i].last_update_time.strftime("%Y-%m-%d %H:%M:%S"))
                    df = pd.DataFrame({pathname: file_detail1,
                                       '商品编码': file_detail2,
                                       '商品描述': file_detail3,
                                       '盘点数量': file_detail4,
                                       '盘点差异': file_detail5,
                                       '盘点用户名': file_detail6,
                                       '入库时间': file_detail7,
                                       '创建时间': file_detail8,
                                       '最后更新时间': file_detail9
                                       })
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
                    response['Content-Disposition'] = 'attachment;filename="cyclecountresult.xlsx"'
                    return response
                else:
                    ret = FBMsg.wms_errfile()
                    return Response(ret)
            else:
                sort = request._request.GET.get('sort', 'name')
                max_page = request._request.GET.get('max_page', 100)
                list = ListModel.objects.filter(appid=request.user.appid).order_by(sort)
                if request._request.GET.get('name', ''):
                    list = list.filter(name__icontains=str(request._request.GET.get('name', ''))).order_by(sort)
                if request._request.GET.get('goods_code', ''):
                    list = list.filter(goods_code__icontains=str(request._request.GET.get('goods_code', ''))).order_by(sort)
                if request._request.GET.get('goods_name', ''):
                    list = list.filter(goods_name__icontains=str(request._request.GET.get('goods_name', ''))).order_by(sort)
                if request._request.GET.get('staff', ''):
                    if list.filter(staff=str(request._request.GET.get('staff', ''))).exists():
                        list = list.filter(staff=str(request._request.GET.get('staff', ''))).order_by(sort)
                    else:
                        return Response(FBMsg.wms_no_user())
                if request._request.GET.get('t_code', ''):
                    list = list.filter(t_code=str(request._request.GET.get('t_code', ''))).order_by(sort)
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
                if 'changedata' in data:
                    if str(data['changedata']) == '1':
                        if ListModel.objects.filter(appid=request.user.appid, t_code=str(data['t_code'])).exists():
                            patch_data = ListModel.objects.filter(appid=request.user.appid,
                                                                  t_code=str(data['t_code'])).first()
                            if 'goods_qty' in data:
                                patch_data.goods_qty = patch_data.goods_qty + int(data['goods_qty'])
                                patch_data.cycle_count_balance = patch_data.cycle_count_balance + int(data['goods_qty'])
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
                if 'postdata' in data:
                    if str(data['postdata']) == '1':
                        if binset.models.ListModel.objects.filter(appid=request.user.appid, name=str(data['name']),
                                                                  is_delete=0).exists():
                            if goodslist.models.ListModel.objects.filter(appid=request.user.appid,
                                                                                   name=str(data['goods_code']),
                                                                                   is_delete=0).exists():
                                goods_name = goodslist.models.ListModel.objects.filter(appid=request.user.appid,
                                                                                   name=str(data['goods_code']),
                                                                                   is_delete=0).first().goods_name
                            else:
                                goods_name = ''
                            ListModel.objects.create(appid=request.user.appid, name=str(data['name']),
                                                     goods_code=str(data['goods_code']), goods_name=goods_name,
                                                     goods_qty=int(data['goods_qty']), inbound_time=datetime.datetime.now(),
                                                     staff=str(data['staff']), cycle_count_balance=int(data['goods_qty']),
                                                     t_code=Md5.md5(str(data['name'])))
                            ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                                'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
                            ret = FBMsg.wms_ret()
                            ret['ip'] = ip
                            ret['data'] = data
                            return Response(ret)
                        else:
                            ret = FBMsg.wms_err()
                            ret['data'] = {
                                "库位不存在": str(data['name'])
                            }
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
                if ListModel.objects.filter(appid=request.user.appid, t_code=str(data['t_code'])).exists():
                    patch_data = ListModel.objects.filter(appid=request.user.appid, t_code=str(data['t_code'])).first()
                    if 'goods_qty' in data:
                        patch_data.goods_qty = patch_data.goods_qty + int(data['goods_qty'])
                        patch_data.cycle_count_balance = patch_data.cycle_count_balance + int(data['goods_qty'])
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
            delete_data = ListModel.objects.filter(appid=request.user.appid)
            for i in range(len(delete_data)):
                delete_data[i].delete()
            ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
            ret = FBMsg.wms_ret()
            ret['ip'] = ip
            return Response(ret)
        else:
            return Response(FBMsg.wms_vip())
    def put(self, request, format=None):
        global cyclecount_number
        file_obj = request.data['file']
        vip_id = Users.objects.filter(appid=request.user.appid, developer=1, is_delete=0).first().vip
        file_check = FileVipCheck.FileVipCheck(file_obj.size, vip_id)
        if file_check == "N":
            return Response(FBMsg.err_data())
        elif file_check == "Y":
            if os.path.exists(os.path.join(settings.BASE_DIR, 'media/upload/' + pathlink)):
                pass
            else:
                os.makedirs(os.path.join(settings.BASE_DIR, 'media/upload/' + pathlink))
            if file_obj.name.endswith('.xlsx'):
                filename = os.path.join(settings.BASE_DIR, 'media/upload/' + pathlink + '/' + request.user.appid + '.xlsx')
            elif file_obj.name.endswith('.xls'):
                filename = os.path.join(settings.BASE_DIR, 'media/upload/' + pathlink + '/' + request.user.appid + '.xls')
            else:
                return Response(FBMsg.err_data())
            with open(filename, 'wb+') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
                f.close()
            df = pd.read_excel(filename)
            if ListModel.objects.filter(appid=request.user.appid).exists():
                upload_data = ListModel.objects.filter(appid=request.user.appid)
                for i in range(len(upload_data)):
                    upload_data[i].delete()
            for index, row in df.iterrows():
                if str(row[pathname]) == '':
                    pass
                else:
                    if goodslist.models.ListModel.objects.filter(appid=request.user.appid, name=str(row['商品编码']),
                                                                 is_delete=0).exists():
                        pass
                    else:
                        ret = FBMsg.wms_err()
                        ret['data'] = {
                            "商品编码不存在": str(row['商品编码'])
                        }
                        return Response(ret)
                    if binset.models.ListModel.objects.filter(appid=request.user.appid, name=str(row[pathname]),
                                                                 is_delete=0).exists():
                        pass
                    else:
                        ret = FBMsg.wms_err()
                        ret['data'] = {
                            "库位不存在": str(row[pathname])
                        }
                        return Response(ret)
                    if Users.objects.filter(appid=request.user.appid, name=str(row['盘点用户名']),
                                                                 is_delete=0).exists():
                        pass
                    else:
                        ret = FBMsg.wms_err()
                        ret['data'] = {
                            "用户不存在": str(row['盘点用户名'])
                        }
                        return Response(ret)
                    if stockbinlist.models.ListModel.objects.filter(appid=request.user.appid, t_code=str(row['数据标识']),
                                                                    is_delete=0).exists():
                        cycle_count_data = stockbinlist.models.ListModel.objects.filter(appid=request.user.appid,
                                                                                        t_code=str(row['数据标识']),
                                                                                        is_delete=0).first()
                        ListModel.objects.create(appid=request.user.appid, name=str(row[pathname]), goods_code=str(row['商品编码']),
                                                 goods_name=str(row['商品描述']),
                                                 cycle_count_balance=0 - cycle_count_data.goods_qty, staff=str(row['盘点用户名']),
                                                 inbound_time=cycle_count_data.create_time,
                                                 t_code=Md5.md5(str(row[pathname])))
                    else:
                        ret = FBMsg.wms_err()
                        ret['data'] = {
                            "数据不存在": str(row[pathname])
                        }
                        return Response(ret)
            os.remove(filename)
            ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
            ret = FBMsg.wms_ret()
            ret['ip'] = ip
            return Response(ret)
        else:
            return Response(FBMsg.err_data())
