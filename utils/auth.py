from rest_framework import exceptions
from users.models import Users
from utils.fbmsg import FBMsg
import re

class Authtication(object):
    def authenticate(self, request):
        if request.path == "/docs/":
            return ('docs', 'ok')
        else:
            openid = request._request.GET.get('openid', '')
            if Users.objects.filter(openid=openid, is_delete=0).exists():
                user = Users.objects.filter(openid=openid, is_delete=0).first()
                return (user, openid)
            else:
                raise exceptions.AuthenticationFailed(FBMsg.err_auth())
    #     userid = request._request.user.id
    #     if userid is None:
    #         openid = request._request.GET.get('token', '')
    #         if Users.objects.filter(openid=openid, is_delete=0).exists():
    #             token_obj = Users.objects.filter(openid=openid, is_delete=0).first()
    #             return (token_obj, openid)
    #         else:
    #             raise exceptions.AuthenticationFailed(FBMsg.err_auth())
    #     else:
    #         token_obj = Users.objects.filter(user_id=userid, is_delete=0).first()
    #         return (token_obj, token_obj.openid)

        # if Userprofile.objects.filter(token=token, is_delete=0).exists():
        #     referer = request.META.get('HTTP_REFERER', '')
        #     referer_obj = re.findall(r'https://www.56yhz.com/', str(referer), re.IGNORECASE)
        #     if not referer_obj:
        #         token_obj = Userprofile.objects.filter(token=token, is_delete=0).first()
        #         return (token_obj.user, token_obj.openid)
        #     else:
        #         raise exceptions.AuthenticationFailed(FBMsg.error_referer)


    def authenticate_header(self, request):
        pass
