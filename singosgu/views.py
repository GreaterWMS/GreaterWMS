from django.utils import timezone
from contact.models import Contact
from utils.md5 import Md5
from utils.fbmsg import FBMsg
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse
from rest_framework.views import APIView
from utils.fbmsg import FBMsg
from utils.md5 import Md5
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import re, json, random, datetime
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from users.models import Users
from notebook.models import NoteBook
from notebook.serializers import NoteBookEventSerializers, NoteBookSerializers

def index(request):
    context = {}
    apiurl = 'http://127.0.0.1:8000/'
    #apiurl = 'https://www.8838.info/'
    if request.user.id is not None:
        user = Users.objects.get(user_id=request.user.id)
        context['openid'] = user.openid
    else:
        pass
    context['contactapi'] = apiurl + "contact"
    context['loginapi'] = apiurl + "login"
    context['registerapi'] = apiurl + "register"
    context['captcha'] = apiurl + "captcha"
    return render(request, 'home.html', context)

@cache_page(60)
def captcha(request):
    foo = ['a', 'b']
    data = {}
    mode = random.choice(foo)
    if mode == 'a':
        num1 = random.randint(10, 20)
        num2 = random.randint(0, 10)
        nummode = "-"
        data['result'] = num1 - num2
    elif mode == 'b':
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        nummode = "+"
        data['result'] = num1 + num2
    data['num1'] = num1
    data['num2'] = num2
    data['nummode'] = nummode
    data['numrandom'] = random.randint(0, 20)
    while True:
        data['numrandom'] = random.randint(0, 20)
        if data['numrandom'] != data['result']:
            ret = FBMsg.ret()
            ret['data'] = data
            return JsonResponse(ret)

@method_decorator(csrf_exempt, name='dispatch')
def login(request):
    if request.method == "POST":
        postdata = json.loads(request.body.decode().replace("'", "\""))
        data = {
            "name": postdata.get("name", ''),
            "password": postdata.get("password", '')
        }
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
            'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        if Users.objects.filter(name=str(data['name']), password=str(data['password']), developer=1).exists():
            user = auth.authenticate(username=str(data['name']), password=str(data['password']))
            if user is None:
                err_ret = FBMsg.err_ret()
                err_ret['data'] = data
                return JsonResponse(err_ret)
            else:
                auth.login(request, user)
                user = Users.objects.get(name=str(data['name']), developer=1)
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
                data.pop('password', '')
                ret['ip'] = ip
                ret['data'] = data
                return JsonResponse(ret)
        else:
            err_ret = FBMsg.err_ret()
            err_ret['ip'] = ip
            err_ret['data'] = data
            return JsonResponse(err_ret)

@method_decorator(csrf_exempt, name='dispatch')
def register(request):
    postdata = json.loads(request.body.decode().replace("'", "\""))
    data = {
        "name": postdata.get("name", ''),
        "password1": postdata.get("password1", ''),
        "password2": postdata.get("password2", ''),
    }
    ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
        'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
    script_obj = re.findall(r'script', str(data), re.IGNORECASE)
    select_obj = re.findall(r'select', str(data), re.IGNORECASE)
    if script_obj:
        return JsonResponse(FBMsg.err_bad())
    elif select_obj:
        return JsonResponse(FBMsg.err_bad())
    else:
        if Users.objects.filter(name=str(data['name']), developer=1, is_delete=0).exists():
            err_user_same = FBMsg.err_user_same()
            err_user_same['ip'] = ip
            err_user_same['data'] = data['name']
            return JsonResponse(err_user_same)
        else:
            if Users.objects.filter(ip=ip).exists():
                if Users.objects.filter(ip=ip).count() > 2:
                    err_register_more = FBMsg.err_register_more()
                    err_register_more['ip'] = ip
                    err_register_more['data'] = data['name']
                    return JsonResponse(err_register_more)
                else:
                    if 'password1' not in data:
                        err_password1_empty = FBMsg.err_password1_empty()
                        err_password1_empty['ip'] = ip
                        err_password1_empty['data'] = data['name']
                        return JsonResponse(err_password1_empty)
                    else:
                        if str(data['password1']) == '':
                            err_password1_empty = FBMsg.err_password1_empty()
                            err_password1_empty['ip'] = ip
                            err_password1_empty['data'] = data['name']
                            return JsonResponse(err_password1_empty)
                        else:
                            if 'password2' not in data:
                                err_password2_empty = FBMsg.err_password2_empty()
                                err_password2_empty['ip'] = ip
                                err_password2_empty['data'] = data['name']
                                return JsonResponse(err_password2_empty)
                            else:
                                if str(data['password2']) == '':
                                    err_password2_empty = FBMsg.err_password2_empty()
                                    err_password2_empty['ip'] = ip
                                    err_password2_empty['data'] = data['name']
                                    return JsonResponse(err_password2_empty)
                                else:
                                    if str(data['password1']) != str(data['password2']):
                                        err_password_not_same = FBMsg.err_password_not_same()
                                        err_password_not_same['ip'] = ip
                                        err_password_not_same['data'] = data['name']
                                        return JsonResponse(err_password_not_same)
                                    else:
                                        transaction_code = Md5.md5(data['name'])
                                        user = User.objects.create_user(username=str(data['name']), password=str(data['password1']))
                                        Users.objects.create(user_id=user.id, name=user.username, password=str(data['password1']),
                                                             openid=transaction_code,
                                                             appid=Md5.md5(data['name'] + '1'),
                                                             transaction_code=Md5.md5(str(timezone.now())), developer=1,
                                                             ip=ip)
                                        auth.login(request, user)
                                        ret = FBMsg.ret()
                                        data['openid'] = transaction_code
                                        ret['ip'] = ip
                                        data.pop('password1', '')
                                        data.pop('password2', '')
                                        ret['data'] = data
                                        return JsonResponse(ret)
            else:
                if 'password1' not in data:
                    err_password1_empty = FBMsg.err_password1_empty()
                    err_password1_empty['ip'] = ip
                    err_password1_empty['data'] = data['name']
                    return JsonResponse(err_password1_empty)
                else:
                    if str(data['password1']) == '':
                        err_password1_empty = FBMsg.err_password1_empty()
                        err_password1_empty['ip'] = ip
                        err_password1_empty['data'] = data['name']
                        return JsonResponse(err_password1_empty)
                    else:
                        if 'password2' not in data:
                            err_password2_empty = FBMsg.err_password2_empty()
                            err_password2_empty['ip'] = ip
                            err_password2_empty['data'] = data['name']
                            return JsonResponse(err_password2_empty)
                        else:
                            if str(data['password2']) == '':
                                err_password2_empty = FBMsg.err_password2_empty()
                                err_password2_empty['ip'] = ip
                                err_password2_empty['data'] = data['name']
                                return JsonResponse(err_password2_empty)
                            else:
                                if str(data['password1']) != str(data['password2']):
                                    err_password_not_same = FBMsg.err_password_not_same()
                                    err_password_not_same['ip'] = ip
                                    err_password_not_same['data'] = data['name']
                                    return JsonResponse(err_password_not_same)
                                else:
                                    transaction_code = Md5.md5(data['name'])
                                    user = User.objects.create_user(username=str(data['name']),
                                                                    password=str(data['password1']))
                                    Users.objects.create(user_id=user.id, name=user.username,
                                                         password=str(data['password1']),
                                                         openid=transaction_code, appid=Md5.md5(data['name'] + '1'),
                                                         transaction_code=Md5.md5(str(timezone.now())),
                                                         developer=1, ip=ip)
                                    auth.login(request, user)
                                    ret = FBMsg.ret()
                                    ret['ip'] = ip
                                    data['openid'] = transaction_code
                                    data.pop('password1', '')
                                    data.pop('password2', '')
                                    ret['data'] = data
                                    return JsonResponse(ret)

@method_decorator(csrf_exempt, name='dispatch')
class Authcheck(APIView):
    authentication_classes = []
    throttle_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        data = request.data
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
            'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        if Users.objects.filter(openid=data['data'], is_delete=0).exists():
            ret = FBMsg.ret()
            ret['ip'] = ip
            ret['data'] = {
                "openid": Users.objects.filter(openid=data['data'], is_delete=0).first().openid
            }
            return JsonResponse(ret)
        else:
            err_ret = FBMsg.err_ret()
            return JsonResponse(err_ret)

@method_decorator(csrf_exempt, name='dispatch')
class Initialdata(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        data = {
            "openid": request.auth,
            "authid": data.get('authid', '')
        }
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
            'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        if (data['authid']) == '':
            err_authid = FBMsg.err_authid()
            err_authid['ip'] = ip
            return JsonResponse(err_authid)
        else:
            if (data['openid']) == '':
                if Users.objects.filter(openid=data['authid'], is_delete=0).exists():
                    err_openid = FBMsg.err_openid()
                    err_openid['ip'] = ip
                    err_openid['data'] = {
                        'authid': Users.objects.filter(openid=data['authid'], is_delete=0).first().openid,
                    }
                    return JsonResponse(err_openid)
                else:
                    err_auth = FBMsg.err_auth()
                    err_auth['ip'] = ip
                    return JsonResponse(err_auth)
            else:
                if Users.objects.filter(openid=data['authid'], is_delete=0).exists():
                    if Users.objects.filter(openid=data['openid'], is_delete=0).exists():
                        admin = Users.objects.filter(openid=data['authid']).first()
                        user = Users.objects.filter(openid=data['openid']).first()
                        if user.appid == admin.appid:
                            today = datetime.date.today()
                            note_date = today.strftime('%Y-%m-%d')
                            today_note = NoteBook.objects.filter(openid=data['openid'], note_day__gte=note_date,
                                                                 is_delete=0).order_by('note_day')[:30]
                            today_note_ser = NoteBookSerializers(today_note, many=True)
                            note_num = NoteBook.objects.filter(openid=data['openid'], note_day=note_date, progress=0,
                                                                  is_delete=0).count()
                            delta = datetime.timedelta(days=90)
                            start_date = (today - delta).strftime('%Y-%m-%d')
                            end_date = (today + delta).strftime('%Y-%m-%d')
                            events = NoteBook.objects.filter(openid=data['openid'], note_day__range=[start_date, end_date]).order_by(
                                '-create_time')
                            events_ser = NoteBookEventSerializers(events, many=True)
                            ret_auth = FBMsg.ret_auth()
                            ret_auth['ip'] = ip
                            ret_auth['events'] = events_ser.data
                            ret_auth['today_note'] = today_note_ser.data
                            ret_auth['note_num'] = note_num
                            ret_auth['data'] = {
                                'authid': Users.objects.filter(openid=data['authid'], is_delete=0).first().openid,
                                "openid": Users.objects.filter(openid=data['openid'], is_delete=0).first().openid
                            }
                            return JsonResponse(ret_auth)
                        else:
                            err_auth_open = FBMsg.err_auth_open()
                            err_auth_open['ip'] = ip
                            return JsonResponse(err_auth_open)
                    else:
                        err_openid = FBMsg.err_openid()
                        err_openid['ip'] = ip
                        err_openid['data'] = {
                            'authid': Users.objects.filter(openid=data['authid'], is_delete=0).first().openid,
                        }
                        return JsonResponse(err_openid)
                else:
                    err_auth = FBMsg.err_auth()
                    err_auth['ip'] = ip
                    return JsonResponse(err_auth)

@method_decorator(csrf_exempt, name='dispatch')
class Contact(APIView):
    permission_classes = []
    authentication_classes = []
    throttle_classes = []
    def post(self, request, *args, **kwargs):
        postdata = request.data
        data = {
            "name": postdata.get('name', ''),
            "mobile": postdata.get('mobile', ''),
            "comments": postdata.get('comments', ''),
            "openid": postdata.get('openid', '')
        }
        script_obj = re.findall(r'script', str(data), re.IGNORECASE)
        select_obj = re.findall(r'select', str(data), re.IGNORECASE)
        if script_obj:
            return JsonResponse(FBMsg.err_bad())
        elif select_obj:
            return JsonResponse(FBMsg.err_bad())
        else:
            ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
            if 'name' not in data:
                err_contact_name = FBMsg.err_contact_name()
                return JsonResponse(err_contact_name)
            else:
                if data['name'] == '':
                    err_contact_name = FBMsg.err_contact_name()
                    return JsonResponse(err_contact_name)
                else:
                    if 'mobile' not in data:
                        err_contact_mobile = FBMsg.err_contact_mobile()
                        return JsonResponse(err_contact_mobile)
                    else:
                        if data['mobile'] == '':
                            err_contact_mobile = FBMsg.err_contact_mobile()
                            return JsonResponse(err_contact_mobile)
                        else:
                            if 'comments' not in data:
                                err_contact_comments = FBMsg.err_contact_comments()
                                return JsonResponse(err_contact_comments)
                            else:
                                if data['comments'] == '':
                                    err_contact_comments = FBMsg.err_contact_comments()
                                    return JsonResponse(err_contact_comments)
                                else:
                                    Contact.objects.create(name=data['name'], mobile=data['mobile'], comments=data['comments'],
                                                           openid=data['openid'], ip=ip)
                                    ret = FBMsg.ret()
                                    ret['ip'] = ip
                                    ret['data'] = data
                                    return JsonResponse(ret)

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

from django.http import StreamingHttpResponse
from django.conf import settings # 你的设置
from wsgiref.util import FileWrapper
import mimetypes
def js(request):
    path = settings.BASE_DIR + request.path_info
    content_type, encoding = mimetypes.guess_type(path)
    resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
    resp['Cache-Control'] = "max-age=864000000000"
    # 静态文件最好加上这句让浏览器缓存，不然会重复请求
    return resp
def css(request):
    path = settings.BASE_DIR + request.path_info
    content_type, encoding = mimetypes.guess_type(path)
    resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
    resp['Cache-Control'] = "max-age=864000000000"
    # 静态文件最好加上这句让浏览器缓存，不然会重复请求
    return resp
def fonts(request):
    path = settings.BASE_DIR + request.path_info
    content_type, encoding = mimetypes.guess_type(path)
    resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
    resp['Cache-Control'] = "max-age=864000000000"
    # 静态文件最好加上这句让浏览器缓存，不然会重复请求
    return resp
def statics(request):
    path = settings.BASE_DIR + request.path_info
    content_type, encoding = mimetypes.guess_type(path)
    resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
    resp['Cache-Control'] = "max-age=864000000000"
    # 静态文件最好加上这句让浏览器缓存，不然会重复请求
    return resp

