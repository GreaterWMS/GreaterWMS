import os, qrcode, json
from django.conf import settings
from . import models
from django.http import JsonResponse

def qrcodelist(request):
    context = {}
    text = json.loads(request.body.decode())['data']
    if models.QrCodeList.objects.filter(text=str(text)).exists():
        qr_data = models.QrCodeList.objects.get(text=str(text))
        context['img'] = qr_data.text_img
        return JsonResponse(context)
    else:
        qrcode_data = str(text)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qrcode_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        path = "media/qr_code/" + qrcode_data + ".png"
        imgpath = os.path.join(settings.BASE_DIR, path)
        img.save(imgpath)
        models.QrCodeList.objects.create(text=str(text), text_img="https://scmapi.56yhz.com/" + path)
        context['img'] = "https://scmapi.56yhz.com/" + path
        return JsonResponse(context)
