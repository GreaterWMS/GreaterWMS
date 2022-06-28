import re, datetime, os, urllib, json, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from chat.models import ListModel
from rest_framework.exceptions import APIException
from staff.models import ListModel as staff

CONECTINGS = {}

async def websocket_application(scope, receive, send):
    while True:
        event = await receive()
        if event['type'] == 'websocket.connect':
            await send({'type': 'websocket.accept'})
            query_string = scope.get('query_string', b'').decode()
            qs = urllib.parse.parse_qs(query_string)
            openid = qs.get('openid', [''])[0]
            sender = qs.get('sender', [''])[0] + '-' + openid
            CONECTINGS[sender] = send
        elif event['type'] == 'websocket.receive':
            query_string = scope.get('query_string', b'').decode()
            qs = urllib.parse.parse_qs(query_string)
            openid = qs.get('openid', [''])[0]
            sender = qs.get('sender', [''])[0]
            receiver = qs.get('receiver', [''])[0]
            if staff.objects.filter(openid=openid, staff_name=receiver).exists():
                sender_guy = sender + '-' + openid
                receiver_guy = receiver + '-' + openid
                ListModel.objects.create(sender=sender_guy, receiver=receiver_guy, detail=str(event['text']))
                text = {
                    "sender": sender,
                    "receiver": receiver,
                    "detail": str(event['text']),
                    "create_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "update_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                }
                send = CONECTINGS[sender_guy]
                if receiver_guy in CONECTINGS:
                    send = CONECTINGS[receiver_guy]
                    await send({
                        'type': 'websocket.send',
                        'text': str(text).replace('\'', '\"')
                    })
            else:
                raise APIException({"detail": "Can Not Send Message To Who Not Yours"})
        elif event['type'] == 'websocket.disconnect':
            try:
                query_string = scope.get('query_string', b'').decode()
                qs = urllib.parse.parse_qs(query_string)
                openid = qs.get('openid', [''])[0]
                sender = qs.get('sender', [''])[0] + '-' + openid
                CONECTINGS.pop(sender)
                break
            except:
                break
        else:
            pass

