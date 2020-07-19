from users import models
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.datasolve import DataSolve
from utils.fbmsg import FBMsg
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .schemas import UserLoginSchema
import datetime
from notebook.models import NoteBook
from notebook.serializers import NoteBookEventSerializers, NoteBookSerializers

@method_decorator(csrf_exempt, name='dispatch')
class UserLoginAPI(APIView):
    '''
        post:
            用户登入
            可以接收一个json数据，也可以接收一个json数据组，但是不可以批量登入
            只有开发者账号的openid才可以发起用户登入请求
    '''
    schema = UserLoginSchema()
    def post(self, request, *args, **kwargs):
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
            if models.Users.objects.filter(appid=request.user.appid, name=data['name'], is_delete=0).exists():
                user = models.Users.objects.filter(appid=request.user.appid, name=data['name'], is_delete=0).first()
                if 'password' not in data:
                    return Response(FBMsg.err_psw())
                else:
                    if data['password'] == '':
                        return Response(FBMsg.err_psw())
                    else:
                        if user.password == data['password']:
                            today = datetime.date.today()
                            note_date = today.strftime('%Y-%m-%d')
                            today_note = NoteBook.objects.filter(openid=user.openid, note_day__gte=note_date,
                                                                 is_delete=0).order_by('note_day')[:30]
                            today_note_ser = NoteBookSerializers(today_note, many=True)
                            note_num = NoteBook.objects.filter(openid=user.openid, note_day=note_date,
                                                               progress=0,
                                                               is_delete=0).count()
                            delta = datetime.timedelta(days=90)
                            start_date = (today - delta).strftime('%Y-%m-%d')
                            end_date = (today + delta).strftime('%Y-%m-%d')
                            events = NoteBook.objects.filter(openid=user.openid,
                                                             note_day__range=[start_date, end_date]).order_by(
                                '-create_time')
                            events_ser = NoteBookEventSerializers(events, many=True)
                            ret = FBMsg.ret()
                            data.pop('name')
                            data.pop('password')
                            ret['ip'] = ip
                            ret['events'] = events_ser.data
                            ret['today_note'] = today_note_ser.data
                            ret['note_num'] = note_num
                            data['openid'] = user.openid
                            ret['data'] = data
                            return Response(ret)
                        else:
                            err_ret =  FBMsg.err_ret()
                            return Response(err_ret)
            else:
                return Response(FBMsg.err_auth())
