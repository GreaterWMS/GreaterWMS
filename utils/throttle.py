from rest_framework import exceptions
from rest_framework.throttling import BaseThrottle
from users.models import Users
from throttle.models import Throttle
from utils.md5 import Md5
from django.utils import timezone

data = {}

class VisitThrottle(BaseThrottle):
    def allow_request(self, request, view):
        if request.path == "/docs/":
            return True
        else:
            if request.method == "GET":
                openid = request.auth
                if Users.objects.filter(openid=openid, is_delete=0).exists():
                    user = Users.objects.get(openid=openid)
                    ip = request.META.get('REMOTE_ADDR')
                    transaction_code = Md5.md5(openid + ip)
                    ctime = timezone.now() - timezone.timedelta(seconds=86400)
                    throttle_ctimelist = Throttle.objects.filter(mode="get", throttle_create_time__lte=ctime)
                    for i in throttle_ctimelist:
                        i.delete()
                    throttle_allocationlist = Throttle.objects.filter(mode="get", appid=user.appid).order_by('throttle_create_time')
                    Throttle.objects.create(openid=user.openid, appid=user.appid, ip_address=ip, mode="get", transaction_code=transaction_code)
                    throttle_data = Throttle.objects.get(transaction_code=transaction_code)
                    allocation_seconds_balance = (throttle_data.throttle_create_time - throttle_allocationlist.first().throttle_create_time).seconds
                    data["visit_check"] = throttle_allocationlist.first().throttle_create_time
                    if user.vip == 0:
                        if allocation_seconds_balance >= 86400:
                            throttle_allocationlist.first().delete()
                            return True
                        else:
                            if throttle_allocationlist.count() <= 100000:
                                return True
                            else:
                                throttle_data.delete()
                                return False
                    elif user.vip == 1:
                        if allocation_seconds_balance >= 86400:
                            throttle_allocationlist.first().delete()
                            return True
                        else:
                            if throttle_allocationlist.count() <= 1000:
                                return True
                            else:
                                throttle_data.delete()
                                return False
                    elif user.vip == 2:
                        if allocation_seconds_balance >= 86400:
                            throttle_allocationlist.first().delete()
                            return True
                        else:
                            if throttle_allocationlist.count() <= 5000:
                                return True
                            else:
                                throttle_data.delete()
                                return False
                    elif user.vip == 3:
                        if allocation_seconds_balance >= 86400:
                            throttle_allocationlist.first().delete()
                            return True
                        else:
                            if throttle_allocationlist.count() <= 20000:
                                return True
                            else:
                                throttle_data.delete()
                                return False
                    elif user.vip == 9:
                        return True
                    else:
                        return False
                else:
                    return False
            elif request.method == "POST":
                return True
            elif request.method == "PATCH":
                return True
            elif request.method == "DELETE":
                return True
            elif request.method == "PUT":
                return True
            else:
                return True

    def wait(self):
        ctime = timezone.now()
        wait_time = (ctime - data["visit_check"]).seconds
        balance_time = 1 - wait_time
        return balance_time
