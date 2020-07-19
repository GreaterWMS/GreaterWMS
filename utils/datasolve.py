from utils.fbmsg import FBMsg
import re

class DataSolve(object):
    def datasolve(d):
        data = d.data
        script_obj = re.findall(r'script', str(data), re.IGNORECASE)
        select_obj = re.findall(r'select', str(data), re.IGNORECASE)
        if script_obj:
            return FBMsg.err_bad()
        elif select_obj:
            return FBMsg.err_bad()
        else:
            type_obj_dict = re.findall(r'dict', str(type(data)), re.IGNORECASE)
            type_obj_list = re.findall(r'list', str(type(data)), re.IGNORECASE)
            if len(type_obj_dict) > 0:
                if 'data' in data:
                    data = data['data']
                    return data
                else:
                    return data
            elif len(type_obj_list) > 0:
                return data
            else:
                return FBMsg.err_bad()
