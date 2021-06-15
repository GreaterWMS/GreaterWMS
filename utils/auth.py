from userprofile.models import Users
from rest_framework.exceptions import APIException

class Authtication(object):
    def authenticate(self, request):
        if request.path in ['/docs/', '/swagger/']:
            return (False, None)
        else:
            token = request.META.get('HTTP_TOKEN')
            if token:
                if Users.objects.filter(openid__exact=str(token)).exists():
                    user = Users.objects.filter(openid__exact=str(token)).first()
                    return (True, user)
                else:
                    raise APIException({"detail": "User Does Not Exists"})
            else:
                raise APIException({"detail": "Please Add Token To Your Request Headers"})

    def authenticate_header(self, request):
        pass
