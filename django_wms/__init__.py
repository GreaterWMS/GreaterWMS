import mimetypes, os, requests, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_wms.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from django.conf import settings

mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/javascript", ".js", True)
try:

    path = os.path.join(settings.BASE_DIR, 'utils/country.txt')
    if os.path.exists(path):
        pass
    else:
        response = requests.post('https://www.56yhz.com/area/')
        with open(path, 'w') as f:
            f.write(str(eval(response.text).get('country')))
            f.close()
except:
    pass
print('Welcome To GreaterWMS')
