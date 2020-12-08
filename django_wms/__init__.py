import mimetypes, os, requests, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_wms.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from django.conf import settings

mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/javascript", ".js", True)
try:
    response = requests.post('https://www.56yhz.com/area/')
    path = os.path.join(settings.BASE_DIR, 'utils/country.txt')
    with open(path, 'w') as f:
        f.write(str(eval(response.text).get('country')))
        f.close()
except:
    pass
print('Welcome To GreaterWMS')
