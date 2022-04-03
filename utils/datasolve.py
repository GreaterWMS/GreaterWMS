from userprofile.models import Users
import re, base64, json
from rest_framework.exceptions import APIException

def data_validate(data):
    script_obj = re.findall(r'script', str(data), re.IGNORECASE)
    select_obj = re.findall(r'select', str(data), re.IGNORECASE)
    if script_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    elif select_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    else:
        return data

def qty_0_data_validate(data):
    script_obj = re.findall(r'script', str(data), re.IGNORECASE)
    select_obj = re.findall(r'select', str(data), re.IGNORECASE)
    if script_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    elif select_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    else:
        if data > 0:
            return data
        else:
            raise APIException({'detail': 'Qty Must > 0'})

def qty_data_validate(data):
    script_obj = re.findall(r'script', str(data), re.IGNORECASE)
    select_obj = re.findall(r'select', str(data), re.IGNORECASE)
    if script_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    elif select_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    else:
        if data >= 0:
            return data
        else:
            raise APIException({'detail': 'Qty Must >= 0'})

def openid_validate(data):
    if Users.objects.filter(openid=data).exists():
        return data
    else:
        raise APIException({'detail': 'User does not exists'})

def appid_validate(data):
    if Users.objects.filter(appid=data).exists():
        return data
    else:
        raise APIException({'detail': 'User does not exists'})

def asn_data_validate(data):
    script_obj = re.findall(r'script', str(data), re.IGNORECASE)
    select_obj = re.findall(r'select', str(data), re.IGNORECASE)
    if script_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    elif select_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    else:
        asn_last_code = re.findall(r'\d+', str(data), re.IGNORECASE)
        if str(asn_last_code[0]) == '00000001':
            data = 'ASN' + '00000001'
        else:
            data = 'ASN' + str(int(asn_last_code[0]) + 1).zfill(8)
        return data

def dn_data_validate(data):
    script_obj = re.findall(r'script', str(data), re.IGNORECASE)
    select_obj = re.findall(r'select', str(data), re.IGNORECASE)
    if script_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    elif select_obj:
        raise APIException({'detail': 'Bad Data can‘not be store'})
    else:
        dn_last_code = re.findall(r'\d+', str(data), re.IGNORECASE)
        if str(dn_last_code[0]) == '00000001':
            data = 'DN' + '00000001'
        else:
            data = 'DN' + str(int(dn_last_code[0]) + 1).zfill(8)
        return data

def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)

def is_number(data):
    try:
        float(data)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(data)
        return True
    except (TypeError, ValueError):
        pass
    return False

def secret_bar_code(data):
    return base64.b64encode(str(data).encode()).decode()

def verify_bar_code(data):
    return json.loads(base64.b64decode(str(data).encode()).decode().replace('\'', '\"'))

def transportation_calculate(weight, volume, weight_fee, volume_fee, min_fee):
    weight_cost = weight * weight_fee
    volume_cost = volume * volume_fee
    max_ = (weight_cost if weight_cost > volume_cost else volume_cost) if (weight_cost if weight_cost > volume_cost
                                                                           else volume_cost) > min_fee else min_fee
    data = round(max_, 2)
    return data
