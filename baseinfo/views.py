from rest_framework.views import APIView
from rest_framework.response import Response
from utils.datasolve import DataSolve
from utils.page import MyPageNumberPagination
from utils.fbmsg import FBMsg
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .schemas import ListSchema, baseinfoSchema
from .serializers import ListSerializers
from django.conf import settings
import os, math
import pandas as pd
from .models import BaseInfoModel
from users.models import Users
from django.utils import timezone

@method_decorator(csrf_exempt, name='dispatch')
class ListAPI(APIView):
    '''
        get:
            获取基础信息列表
        ---
        # 实现备注:
        **获取基础信息列表**<br><br>
        # 参数信息
        |  请求参数    |  类型 |  说明   |  是否必填    |   附加信息 |
        | ---- | ---- | ---- | ---- | ---- |
        |   openid   |   string   | openid |    Y |   openid是必须的参数  |
        |   goods_code   |   string   | 项目名称 |    N |   商品编码会被模糊查询  |
        |   page   |  int    |   页数  |  N  |  显示哪一页的数据  |
        |   max_page   |  int    |  每页数据条数  |  N   |  max_page在0~1000之间，默认为100 |
        |   sort   |  string    |  排序  |  N   |  请求的数据进行排序 |

        |  响应参数    |  类型 |  说明    |
        | ---- | ---- | ---- |
        |   count   |   int   | 总共多少条  |
        |   next   |   string   | 下一页链接  |
        |   previous   |   string   | 上一页链接  |
        |   results   |   string   | 返回的信息结果 |
        |   code   |   int   | 响应结果码  |
        |   msg   |  string    |   响应结果信息  |
        |   ip   |  string    |   请求发起的ip  |
        |   data   |  JSON    |  返回数据   |
        |   totlepage   |  int    |  一共多少页   |

        ## 响应code说明
        |  Code    |  Description    |
        | ---- | ---- |
        |   200   |   成功   |
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
                                    "goods_code": "A522",
                                    "sup_product_day": 9,
                                    "sup_intransit": 8,
                                    "loading_inspect": 2,
                                    "create_time": "2020-05-20 10:59:30"
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
    schema = ListSchema()
    def get(self, request, *args, **kwargs):
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
            'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        sort = request._request.GET.get('sort', '-create_time')
        max_page = request._request.GET.get('max_page', 100)
        list = BaseInfoModel.objects.filter(appid=request.user.appid).order_by(sort)
        if request._request.GET.get('goods_code', ''):
            list = list.filter(goods_code__icontains=request._request.GET.get('goods_code', '')).order_by(sort)
        pg = MyPageNumberPagination()
        pg_list = pg.paginate_queryset(queryset=list, request=request, view=self)
        list_ser = ListSerializers(pg_list, many=True)
        ret = FBMsg.ret()
        ret['ip'] = ip
        ret['data'] = list_ser.data
        ret['totlepage'] = math.ceil(list.count()/int(max_page))
        return pg.get_paginated_response(ret)

@method_decorator(csrf_exempt, name='dispatch')
class BaseInfoAPI(APIView):
    '''
        post:
            上传基础信息列表
        ---
        # 实现备注:
        **不提供调试**<br><br>

        ## 响应code说明
        |  Code    |  Description    |
        | ---- | ---- |
        |   200   |   成功   |
    '''
    schema = baseinfoSchema()
    parser_classes = [MultiPartParser, ]
    def post(self, request, format=None):
        file_obj = request.data['file']
        vip_id = Users.objects.get(appid=request.user.appid, developer=1, is_delete=0).vip
        if vip_id == 0:
            if file_obj.size >= 102400:
                return Response(FBMsg.err_data())
        elif vip_id == 4:
            if file_obj.size >= 102400:
                return Response(FBMsg.err_data())
        if file_obj.name.endswith('.xlsx'):
            filename = os.path.join(settings.BASE_DIR, 'media/baseinfo/' + request.auth + '.xlsx')
        elif file_obj.name.endswith('.xls'):
            filename = os.path.join(settings.BASE_DIR, 'media/baseinfo/' + request.auth + '.xls')
        else:
            return Response(FBMsg.err_data())
        with open(filename, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
            f.close()
        df = pd.read_excel(filename)
        if BaseInfoModel.objects.filter(appid=request.user.appid).exists():
            baseinfo_data = BaseInfoModel.objects.filter(appid=request.user.appid)
            for i in range(len(baseinfo_data)):
                baseinfo_data[i].delete()
        for index, row in df.iterrows():
            BaseInfoModel.objects.create(appid=request.user.appid,
                                         goods_code=str(row['商品编号']),
                                         sup_product_day=int(row['供应商生产周期(天)']),
                                         sup_intransit=int(row['供应商送货在途时间(天)']),
                                         loading_inspect=int(row['到货卸货和检验时间(天)']),
                                         total_leadtime=int(row['供应商生产周期(天)']) + int(row['供应商送货在途时间(天)']) +
                                                        int(row['到货卸货和检验时间(天)']))
        os.remove(filename)
        return Response(FBMsg.ret())

@method_decorator(csrf_exempt, name='dispatch')
class ExampleAPI(APIView):
    '''
        get:
            下载基本信息的上传模板
        ---
    '''
    authentication_classes = []
    throttle_classes = []
    permission_classes = []
    def get(self, request, *args, **kwargs):
        filepath = os.path.join(settings.BASE_DIR, 'media/baseinfo/baseinfo.xlsx')
        file = open(filepath, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="baseinfo.xlsx"'
        return response
