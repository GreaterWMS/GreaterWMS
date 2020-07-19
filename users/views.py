from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from utils import page
from utils.datasolve import DataSolve
from utils.fbmsg import FBMsg
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import datetime
from .schemas import UserListSchema

@method_decorator(csrf_exempt, name='dispatch')
class UserListAPI(APIView):
    '''
        get:
            获取用户列表
        patch:
            修改用户信息
    '''
    schema = UserListSchema()
    def get(self, request, *args, **kwargs):
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
            'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        sort = request._request.GET.get('sort', '-create_time')
        list = models.Users.objects.filter(appid=request.user.appid, developer=0, is_delete=0).order_by(sort)
        if request._request.GET.get('name', ''):
            list = list.filter(name__icontains=request._request.GET.get('name', '')).order_by(sort)
        if request._request.GET.get('nickname', ''):
            list = list.filter(nickname__icontains=request._request.GET.get('nickname', '')).order_by(sort)
        if request._request.GET.get('start_date_create', ''):
            try:
                start_date = request._request.GET.get('start_date_create', '')
                if request._request.GET.get('end_date_create', ''):
                    date_end = request._request.GET.get('end_date_create', '')
                    delta = datetime.timedelta(days=1)
                    date = [int(x) for x in date_end.split('-')]
                    old = datetime.datetime(date[0], date[1], date[2])
                    end_date = (old + delta).strftime('%Y-%m-%d')
                else:
                    today = datetime.date.today()
                    delta = datetime.timedelta(days=1)
                    end_date = (today + delta).strftime('%Y-%m-%d')
                list = list.filter(create_time__range=[start_date, end_date]).order_by(sort)
            except:
                pass
        if request._request.GET.get('start_date_update', ''):
            try:
                start_date = request._request.GET.get('start_date_update', '')
                if request._request.GET.get('end_date_update', ''):
                    date_end = request._request.GET.get('end_date_update', '')
                    delta = datetime.timedelta(days=1)
                    date = [int(x) for x in date_end.split('-')]
                    old = datetime.datetime(date[0], date[1], date[2])
                    end_date = (old + delta).strftime('%Y-%m-%d')
                else:
                    today = datetime.date.today()
                    delta = datetime.timedelta(days=1)
                    end_date = (today + delta).strftime('%Y-%m-%d')
                list = list.filter(last_update_time__range=[start_date, end_date]).order_by(sort)
            except:
                pass
        pg = page.MyPageNumberPagination()
        pg_list = pg.paginate_queryset(queryset=list, request=request, view=self)
        list_ser = serializers.UserListSerializers(pg_list, many=True)
        ret = FBMsg.ret()
        ret['ip'] = ip
        ret['data'] = list_ser.data
        return pg.get_paginated_response(ret)
    def patch(self, request, *args, **kwargs):
        if models.Users.objects.filter(openid=request.auth, appid=request.user.appid,
                                       developer=1, is_delete=0).exists():
            pass
        else:
            return Response(FBMsg.err_dev())
        data = DataSolve.datasolve(request)
        try:
            if data['code'] == "1031":
                return Response(FBMsg.err_bad())
        except:
            ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
            if models.Users.objects.filter(transaction_code=data['transaction_code'], developer=0,
                                                         is_delete=0).exists():
                patch_data = models.Users.objects.filter(transaction_code=data['transaction_code'], developer=0,
                                                         is_delete=0).first()
                patch_data.nickname = data['nickname']
                patch_data.save()
                ret = FBMsg.ret()
                ret['ip'] = ip
                ret['data'] = data
                return Response(ret)
            else:
                return Response(FBMsg.err_tc_empty())
    def delete(self, request, *args, **kwargs):
        if models.Users.objects.filter(openid=request.auth, appid=request.user.appid,
                                       developer=1, is_delete=0).exists():
            pass
        else:
            return Response(FBMsg.err_dev())
        data = request.data
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
            'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        for i in range(len(data)):
            if models.Users.objects.filter(transaction_code=data[i]['transaction_code'], developer=0,
                                                         is_delete=0).exists():
                pass
            else:
                return Response(FBMsg.err_tc_empty())
        for j in range(len(data)):
            delete_data = models.Users.objects.filter(transaction_code=data[j]['transaction_code'], developer=0,
                                                         is_delete=0).first()
            delete_data.is_delete = 1
            delete_data.save()
        ret = FBMsg.ret()
        ret['ip'] = ip
        ret['data'] = data
        return Response(ret)
