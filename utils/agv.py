import requests, os, django, random
from django.utils import timezone
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from tasklist.models import ListModel as ls


def orderTime():
    return random.randint(100000,999999)

def agvmove(from_bin, to_bin):
    orderid = str(timezone.now().strftime('%Y%m%d%H%M%S')) + str(orderTime())
    task_move = str(from_bin + ',' + to_bin)
    data = {
        "modelProcessCode": 'FJ',
        "priority": 6,
        "orderId": str(orderid),
        "formSystem": 'WMS',
        "taskOrderDetail": [
            {
                "taskPath": task_move,
            }
        ]
    }
    response = requests.post(url='http://137.12.129.143:7000/ics/taskOrder/addTask', json=data)
    if response.status_code == '200':
        ls.objects.create(tasklist=orderid,
                          mode=0,
                          from_bin=from_bin,
                          to_bin=to_bin)
        return 'success'
    else:
        return 'failed'

def agvreceive(from_bin, to_bin):
    orderid = str(timezone.now().strftime('%Y%m%d%H%M%S')) + str(orderTime())
    task_move = str(from_bin + ',' + to_bin)
    data = {
        "modelProcessCode": 'CK',
        "priority": 6,
        "orderId": str(orderid),
        "formSystem": 'WMS',
        "taskOrderDetail": [
            {
                "taskPath": task_move,
            }
        ]
    }
    response = requests.post(url='http://137.12.129.143:7000/ics/taskOrder/addTask', json=data)
    if response.status_code == '200':
        ls.objects.create(tasklist=orderid,
                          mode=1,
                          from_bin=from_bin,
                          to_bin=to_bin)
        return 'success'
    else:
        return 'failed'

def agvsend(from_bin, to_bin):
    orderid = str(timezone.now().strftime('%Y%m%d%H%M%S')) + str(orderTime())
    task_move = str(from_bin + ',' + to_bin)
    data = {
        "modelProcessCode": 'RK',
        "priority": 6,
        "orderId": str(orderid),
        "formSystem": 'WMS',
        "taskOrderDetail": [
            {
                "taskPath": task_move,
            }
        ]
    }
    response = requests.post(url='http://137.12.129.143:7000/ics/taskOrder/addTask', json=data)
    if response.status_code == '200':
        ls.objects.create(tasklist=orderid,
                    mode=2,
                    from_bin=from_bin,
                    to_bin=to_bin)
        return 'success'
    else:
        return 'failed'

def agvback(from_bin, to_bin):
    orderid = str(timezone.now().strftime('%Y%m%d%H%M%S')) + str(orderTime())
    task_move = str(from_bin + ',' + to_bin)
    data = {
        "modelProcessCode": 'Cancel',
        "priority": 6,
        "orderId": str(orderid),
        "formSystem": 'WMS',
        "taskOrderDetail": [
            {
                "taskPath": task_move,
            }
        ]
    }
    response = requests.post(url='http://137.12.129.143:7000/ics/taskOrder/addTask', json=data)
    if response.status_code == '200':
        ls.objects.create(tasklist=orderid,
                    mode=3,
                    from_bin=from_bin,
                    to_bin=to_bin)
        return 'success'
    else:
        return 'failed'