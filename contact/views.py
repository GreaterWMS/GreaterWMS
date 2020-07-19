from django.shortcuts import render, redirect
from userprofile.models import Userprofile

apiurl = "http://127.0.0.1:8000/"

def contact(request):
    context = {}
    if Userprofile.objects.filter(user_id=request.user.id).exists():
        user = Userprofile.objects.get(user_id=request.user.id)
        context['openid'] = user.openid
    else:
        pass
    context['api'] = apiurl + "indexapi/"
    return render(request, 'contact.html', context)