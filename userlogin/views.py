from django.http import JsonResponse
from userprofile.models import Users
from userprofile import serializers
from utils.fbmsg import FBMsg
from utils.md5 import Md5
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
import json
from userprofile.models import Users

def login(request, *args, **kwargs):
    post_data = json.loads(request.body.decode())
    data = {
        "name": post_data.get('name'),
        "password": post_data.get('password'),
    }
    ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
        'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
    if User.objects.filter(username=str(data['name'])).exists():
        user = auth.authenticate(username=str(data['name']), password=str(data['password']))
        if user is None:
            err_ret = FBMsg.err_ret()
            err_ret['data'] = data
            return JsonResponse(err_ret)
        else:
            auth.login(request, user)
            user_detail = Users.objects.filter(user_id=user.id).first()
            data = {
                "name": data['name'],
                'openid': user_detail.openid
            }
            ret = FBMsg.ret()
            ret['ip'] = ip
            ret['data'] = data
            return JsonResponse(ret)
    else:
        err_ret = FBMsg.err_ret()
        err_ret['ip'] = ip
        err_ret['data'] = data
        return JsonResponse(err_ret)
