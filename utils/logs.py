from wms.models import Logs

class Logdrf(object):
    def logs(j, k, i, h):
        Logs.objects.create(openid=j, appid=k, log_transaction=i, log_code=h)