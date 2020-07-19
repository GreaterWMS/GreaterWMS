from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.datasolve import DataSolve
from utils.md5 import Md5
from utils.fbmsg import FBMsg
from utils import page
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from . import serializers, models, schemas
from django.contrib import auth
import re, datetime
from users.models import Users

@method_decorator(csrf_exempt, name='dispatch')
class NoteBook(APIView):
    """
        get:
            获得备忘录列表
        post:
            创建一个开发者账号账号
            一个ip只能创建2个开发者账号
    """
    schema = schemas.NoteBook()
    def get(self, request, *args, **kwargs):
        sort = request._request.GET.get('sort', 'note_day')
        start_date = request._request.GET.get('note_day', '')
        date_detail = start_date.split('/')
        search_day = datetime.datetime(int(date_detail[0]), int(date_detail[1]), int(date_detail[2]))
        search_day = search_day.strftime('%Y-%m-%d')
        list = models.NoteBook.objects.filter(note_day__gte=search_day, openid=request.auth,
                                              is_delete=0).order_by(sort, '-create_time')
        if request._request.GET.get('id', ''):
            list = list.filter(pk=request._request.GET.get('id', '')).order_by(sort)
        pg = page.MyPageNumberPagination()
        pg_list = pg.paginate_queryset(queryset=list, request=request, view=self)
        list_ser = serializers.NoteBookSerializers(pg_list, many=True)
        ret = FBMsg.ret()
        ret['data'] = list_ser.data
        return pg.get_paginated_response(ret)
    def post(self, request, *args, **kwargs):
        data = DataSolve.datasolve(request)
        try:
            if data['code'] == "1031":
                return Response(FBMsg.err_bad())
        except:
            ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
            note_day = data['note_day'].split('/')
            note_day = datetime.datetime(int(note_day[0]), int(note_day[1]), int(note_day[2]))
            note_day = note_day.strftime('%Y-%m-%d')
            models.NoteBook.objects.create(openid=request.auth, icon='close', icon_color='light-blue-10',
                                           title=data['title'], note_day=note_day, desc=data['desc'])
            ret = FBMsg.ret()
            ret['ip'] = ip
            ret['data'] = data
            return Response(ret)

    def patch(self, request, *args, **kwargs):
        data = DataSolve.datasolve(request)
        try:
            if data['code'] == "1031":
                return Response(FBMsg.err_bad())
        except:
            ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
            if models.NoteBook.objects.filter(openid=request.auth, id=data['id']).exists():
                if 'progress' in data:
                    progress_data = models.NoteBook.objects.get(id=data['id'])
                    progress_data.icon = 'check'
                    progress_data.icon_color = 'green'
                    progress_data.progress = 1
                    progress_data.save()
                    ret = FBMsg.ret()
                    ret['ip'] = ip
                    ret['data'] = data
                    return Response(ret)
                elif 'desc' in data:
                    progress_data = models.NoteBook.objects.get(id=data['id'])
                    progress_data.desc = data['desc']
                    progress_data.save()
                    ret = FBMsg.ret()
                    ret['ip'] = ip
                    ret['data'] = data
                    return Response(ret)

    def delete(self, request, *args, **kwargs):
        data = DataSolve.datasolve(request)
        try:
            if data['code'] == "1031":
                return Response(FBMsg.err_bad())
        except:
            ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
            if models.NoteBook.objects.filter(openid=request.auth, id=data['id']).exists():
                delete_data = models.NoteBook.objects.get(id=data['id'])
                delete_data.is_delete = 1
                delete_data.save()
                ret = FBMsg.ret()
                ret['ip'] = ip
                ret['data'] = delete_data.title
                return Response(ret)

@method_decorator(csrf_exempt, name='dispatch')
class NoteBookNumber(APIView):
    """
        get:
            获得备忘录数字
    """
    schema = schemas.NoteBook()
    def get(self, request, *args, **kwargs):
        start_date = request._request.GET.get('note_day', '')
        date_detail = start_date.split('/')
        search_day = datetime.datetime(int(date_detail[0]), int(date_detail[1]), int(date_detail[2]))
        search_day = search_day.strftime('%Y-%m-%d')
        list = models.NoteBook.objects.filter(openid=request.auth, note_day=search_day, progress=0, is_delete=0).count()
        ret = FBMsg.ret()
        ret['data'] = list
        return Response(ret)

@method_decorator(csrf_exempt, name='dispatch')
class NoteBookEvent(APIView):
    """
        post:
            获得Events标记
    """
    schema = schemas.NoteBook()
    def post(self, request, *args, **kwargs):
        today = datetime.date.today()
        delta = datetime.timedelta(days=90)
        start_date = (today - delta).strftime('%Y-%m-%d')
        end_date = (today + delta).strftime('%Y-%m-%d')
        list = models.NoteBook.objects.filter(note_day__range=[start_date, end_date], is_delete=0).order_by('-create_time')
        list_ser = serializers.NoteBookEventSerializers(list, many=True)
        ret = FBMsg.ret()
        ret['data'] = list_ser.data
        return Response(ret)
