import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from django.conf import settings

def Country_Data():
    with open(os.path.join(settings.BASE_DIR, 'utils/country.txt'), 'r') as f:
        data = f.read()
        return data
