from userprofile.models import Users
from rest_framework.exceptions import APIException

class Authtication(object):
    def authenticate(self, request):
        if request.path == '/docs/':
            return (False, None)
        elif request.path == '/swagger/':
                return (False, None)
        else:
            token = request.META.get('HTTP_TOKEN').split('-language-')
            if token:
                if Users.objects.filter(openid__exact=str(token[0])).exists():
                    user = Users.objects.filter(openid__exact=str(token[0])).first()
                    return (token[1], user)
                else:
                    raise APIException({"detail": "User Does Not Exists"})
            else:
                raise APIException({"detail": "Please Add Token To Your Request Headers"})

    def authenticate_header(self, request):
        pass
