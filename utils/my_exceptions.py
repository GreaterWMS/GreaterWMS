from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.db import DatabaseError

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        response = Response(response.data)
    else:
        if isinstance(exc, DatabaseError):
            pass
            # response = Response({'detail': 'Database Error'})
        else:
            pass
            # response = Response({'detail': 'Other Error'})
    return response
