import jwt
import datetime
from jwt import exceptions
from django.conf import settings

JWT_SALT = "ds()udsjo@jlsdosjf)wjd_#(#)$"


def create_token(payload):
    headers = {
        "type": "jwt",
        "alg": "HS256"
    }
    payload['exp'] = datetime.datetime.utcnow()
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers)
    return result


def parse_payload(token):
    result = {"status": False, "data": None, "error": None}
    try:
        verified_payload = jwt.decode(token, JWT_SALT, algorithms="HS256", verify=True)
        result["status"] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'Token Expired'
    except jwt.DecodeError:
        result['error'] = 'Token Authentication Failed'
    except jwt.InvalidTokenError:
        result['error'] = 'Illegal Token'
    return result
