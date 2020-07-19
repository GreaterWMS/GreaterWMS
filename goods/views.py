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
from .serializers import ListSerializers
from django.conf import settings
import os, math
import pandas as pd
from .models import GoodsModel
from users.models import Users
from django.utils import timezone

@method_decorator(csrf_exempt, name='dispatch')
class ListAPI(APIView):
    '''
        get:
            获取用户列表
    '''
    schema = ListSchema()
    def get(self, request, *args, **kwargs):
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
            'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        sort = request._request.GET.get('sort', '-create_time')
        max_page = request._request.GET.get('max_page', 100)
        list = GoodsModel.objects.filter(appid=request.user.appid).order_by(sort)
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
class GoodsAPI(APIView):
    '''
        post:
            新增用户
            可以接收一个json数据，也可以接收一个json数据组，但是不可以批量登入
            只有开发者账号的openid才可以发起用户登入请求
    '''
    # schema = BaseInfoSchema()
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
            filename = os.path.join(settings.BASE_DIR, 'media/goods/' + request.auth + '.xlsx')
        elif file_obj.name.endswith('.xls'):
            filename = os.path.join(settings.BASE_DIR, 'media/goods/' + request.auth + '.xls')
        else:
            return Response(FBMsg.err_data())
        with open(filename, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
            f.close()
        df = pd.read_excel(filename)
        if GoodsModel.objects.filter(appid=request.user.appid).exists():
            goods_data = GoodsModel.objects.filter(appid=request.user.appid)
            for i in range(len(goods_data)):
                goods_data[i].delete()
        for index, row in df.iterrows():
            if int(row['现有库存']) <= 0:
                on_hand_stock = 0
            else:
                on_hand_stock = int(row['现有库存'])
            GoodsModel.objects.create(appid=request.user.appid,
                                         goods_code=str(row['商品编号']),
                                         on_hand_stock=on_hand_stock)
        os.remove(filename)
        return Response(FBMsg.ret())

@method_decorator(csrf_exempt, name='dispatch')
class ExampleAPI(APIView):
    authentication_classes = []
    throttle_classes = []
    permission_classes = []
    def get(self, request, *args, **kwargs):
        filepath = os.path.join(settings.BASE_DIR, 'media/goods/goods.xlsx')
        file = open(filepath, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="goods.xlsx"'
        return response
