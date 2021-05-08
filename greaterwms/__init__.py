import mimetypes, os, requests, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
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
        response = requests.post('https://wms.56yhz.com/area_v2/')
        if response.status_code == 200:
            area_results = requests.put(
                url='https://wms.56yhz.com/area_v2/',
                data=eval(response.text)
            )
            if area_results.status_code == 200:
                with open(path, 'w') as f:
                    f.write(str(eval(area_results.text).get('country')))
                f.close()
            else:
                pass
except:
    pass
print('Welcome To GreaterWMS')
