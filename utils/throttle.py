from rest_framework.throttling import BaseThrottle
from throttle.models import ListModel
from utils.md5 import Md5
from django.utils import timezone

data = {}

class VisitThrottle(BaseThrottle):
    def allow_request(self, request, view):
        if request.path == '/docs/':
            return (False, None)
        elif request.path == '/swagger/':
            return (False, None)
        else:
            ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
                'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
            openid = request.auth.openid
            appid = request.auth.appid
            if request.method.lower() == "get":
                ntime = timezone.now()
                ctime = ntime - timezone.timedelta(seconds=1)
                throttle_ctimelist = ListModel.objects.filter(method="get", create_time__lte=ctime)
                for i in throttle_ctimelist:
                    i.delete()
                t_code = Md5.md5(ip)
                throttle_allocationlist = ListModel.objects.filter(openid=openid, appid=appid, ip=ip,
                                                                   method='get').order_by('id')
                throttle_count = throttle_allocationlist.count()
                if throttle_count == 0:
                    ListModel.objects.create(openid=openid, appid=appid, ip=ip, method="get", t_code=t_code)
                    return True
                else:
                    throttle_last_create_time = throttle_allocationlist.first().create_time
                    ListModel.objects.create(openid=openid, appid=appid, ip=ip, method="get", t_code=t_code)
                    allocation_seconds_balance = (ntime - throttle_last_create_time).seconds
                    data["visit_check"] = throttle_last_create_time
                    if allocation_seconds_balance >= 1:
                        return True
                    else:
                        if throttle_count >= 5:
                            return False
                        else:
                            return True
            elif request.method.lower() == "post":
                ntime = timezone.now()
                ctime = ntime - timezone.timedelta(seconds=1)
                throttle_ctimelist = ListModel.objects.filter(method="post", create_time__lte=ctime)
                for i in throttle_ctimelist:
                    i.delete()
                t_code = Md5.md5(ip)
                throttle_allocationlist = ListModel.objects.filter(openid=openid, appid=appid, ip=ip,
                                                                   method='post').order_by('id')
                throttle_count = throttle_allocationlist.count()
                if throttle_count == 0:
                    ListModel.objects.create(openid=openid, appid=appid, ip=ip, method="post", t_code=t_code)
                    return True
                else:
                    throttle_last_create_time = throttle_allocationlist.first().create_time
                    ListModel.objects.create(openid=openid, appid=appid, ip=ip, method="post", t_code=t_code)
                    allocation_seconds_balance = (ntime - throttle_last_create_time).seconds
                    data["visit_check"] = throttle_last_create_time
                    if allocation_seconds_balance >= 1:
                        return True
                    else:
                        if throttle_count >= 4:
                            return False
                        else:
                            return True
            elif request.method.lower() == "put":
                ntime = timezone.now()
                ctime = ntime - timezone.timedelta(seconds=1)
                throttle_ctimelist = ListModel.objects.filter(method="put", create_time__lte=ctime)
                for i in throttle_ctimelist:
                    i.delete()
                t_code = Md5.md5(ip)
                throttle_allocationlist = ListModel.objects.filter(openid=openid, appid=appid, ip=ip,
                                                                   method='put').order_by('id')
                throttle_count = throttle_allocationlist.count()
                if throttle_count == 0:
                    ListModel.objects.create(openid=openid, appid=appid, ip=ip, method="put", t_code=t_code)
                    return True
                else:
                    throttle_last_create_time = throttle_allocationlist.first().create_time
                    ListModel.objects.create(openid=openid, appid=appid, ip=ip, method="put", t_code=t_code)
                    allocation_seconds_balance = (ntime - throttle_last_create_time).seconds
                    data["visit_check"] = throttle_last_create_time
                    if allocation_seconds_balance >= 1:
                        return True
                    else:
                        if throttle_count >= 4:
                            return False
                        else:
                            return True
            elif request.method.lower() == "patch":
                ntime = timezone.now()
                ctime = ntime - timezone.timedelta(seconds=1)
                throttle_ctimelist = ListModel.objects.filter(method="patch", create_time__lte=ctime)
                for i in throttle_ctimelist:
                    i.delete()
                t_code = Md5.md5(ip)
                throttle_allocationlist = ListModel.objects.filter(openid=openid, appid=appid, ip=ip,
                                                                   method='patch').order_by('id')
                throttle_count = throttle_allocationlist.count()
                if throttle_count == 0:
                    ListModel.objects.create(openid=openid, appid=appid, ip=ip, method="patch", t_code=t_code)
                    return True
                else:
                    throttle_last_create_time = throttle_allocationlist.first().create_time
                    ListModel.objects.create(openid=openid, appid=appid, ip=ip, method="patch", t_code=t_code)
                    allocation_seconds_balance = (ntime - throttle_last_create_time).seconds
                    data["visit_check"] = throttle_last_create_time
                    if allocation_seconds_balance >= 1:
                        return True
                    else:
                        if throttle_count >= 4:
                            return False
                        else:
                            return True
            elif request.method.lower() == "delete":
                ntime = timezone.now()
                ctime = ntime - timezone.timedelta(seconds=1)
                throttle_ctimelist = ListModel.objects.filter(method="delete", create_time__lte=ctime)
                for i in throttle_ctimelist:
                    i.delete()
                t_code = Md5.md5(ip)
                throttle_allocationlist = ListModel.objects.filter(openid=openid, appid=appid, ip=ip,
                                                                   method='delete').order_by('id')
                throttle_count = throttle_allocationlist.count()
                if throttle_count == 0:
                    ListModel.objects.create(openid=openid, appid=appid, ip=ip, method="delete", t_code=t_code)
                    return True
                else:
                    throttle_last_create_time = throttle_allocationlist.first().create_time
                    ListModel.objects.create(openid=openid, appid=appid, ip=ip, method="delete", t_code=t_code)
                    allocation_seconds_balance = (ntime - throttle_last_create_time).seconds
                    data["visit_check"] = throttle_last_create_time
                    if allocation_seconds_balance >= 1:
                        return True
                    else:
                        if throttle_count >= 3:
                            return False
                        else:
                            return True
            else:
                return False

    def wait(self):
        ctime = timezone.now()
        wait_time = (ctime - data["visit_check"]).seconds
        balance_time = 1 - wait_time
        return balance_time
