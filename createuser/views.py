from users import models
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.datasolve import DataSolve
from utils.fbmsg import FBMsg
from utils.md5 import Md5
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .schemas import UserCreateSchema

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateAPI(APIView):
    '''
        post:
            只有管理员的openid才可以创建用户
    '''
    schema = UserCreateSchema()
    def post(self, request, *args, **kwargs):
        if models.Users.objects.filter(openid=request.auth, appid=request.user.appid,
                                       developer=1, is_delete=0).exists():
            if models.Users.objects.filter(appid=request.user.appid, is_delete=0).count() >= 6:
                return Response(FBMsg.err_more_user())
        else:
            return Response(FBMsg.err_dev())
        data = DataSolve.datasolve(request)
        try:
            if data['code'] == "1031":
                return Response(FBMsg.err_bad())
        except:
            if models.Users.objects.filter(appid=request.user.appid, name=data['name'], is_delete=0).exists():
                return Response(FBMsg.err_user_same())
            else:
                ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                            'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
                if 'name' not in data:
                    return Response(FBMsg.err_user_name())
                else:
                    if data['name'] == '':
                        return Response(FBMsg.err_user_name())
                    else:
                        if 'nickname' not in data:
                            return Response(FBMsg.err_user_name())
                        else:
                            if data['nickname'] == '':
                                return Response(FBMsg.err_user_name())
                            else:
                                if 'password1' not in data:
                                    return Response(FBMsg.err_password1_empty())
                                else:
                                    if data['password1'] == '':
                                        return Response(FBMsg.err_password1_empty())
                                    else:
                                        if 'password2' not in data:
                                            return Response(FBMsg.err_password2_empty())
                                        else:
                                            if data['password2'] == '':
                                                return Response(FBMsg.err_password2_empty())
                                            else:
                                                if data['password1'] != data['password2']:
                                                    return Response(FBMsg.err_password_not_same())
                                                else:
                                                    transaction_code = Md5.md5(data['nickname'])
                                                    models.Users.objects.create(openid=Md5.md5(data['name']),
                                                                                appid=request.user.appid,
                                                                                transaction_code=transaction_code,
                                                                                name=data['name'],
                                                                                nickname=data['nickname'],
                                                                                password=data['password1'],
                                                                                ip=ip)
                                                    ret = FBMsg.ret()
                                                    ret['ip'] = ip
                                                    ret['data'] = data['name']
                                                    return Response(ret)
