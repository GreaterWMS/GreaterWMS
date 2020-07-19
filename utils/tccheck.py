from utils.fbmsg import FBMsg
from rest_framework.response import Response
from api import models

class TCCheck(object):
    def tccheck(d, g):
        data = d
        appid = g
        print(data, appid)
        if 'transaction_code' not in data:
            err_tc_empty = FBMsg.err_tc_empty()
            return Response(err_tc_empty)
        else:
            if data['transaction_code'] == '':
                err_tc_empty = FBMsg.err_tc_empty()
                return Response(err_tc_empty)
            else:
                if models.POList.objects.filter(appid=appid,
                                                transaction_code=data['transaction_code'],
                                                is_delete=0).exists():
                    pass
                else:
                    err_tc = FBMsg.err_tc()
                    return Response(err_tc)