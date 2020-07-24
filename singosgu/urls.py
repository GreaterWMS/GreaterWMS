"""singosgu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPICodec
from django.views.generic import TemplateView

schema_view = get_schema_view(title='聚商汇--API接口文档', renderer_classes=[SwaggerUIRenderer, OpenAPICodec])

urlpatterns = [
path('admin/', admin.site.urls),
path('docs/', schema_view, name='docs'),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
path('login', views.login, name='login'),
re_path('^js/.*$', views.js, name='js'),
re_path('^css/.*$', views.css, name='css'),
re_path('^fonts/.*$', views.fonts, name='fonts'),
re_path('^statics/.*$', views.statics, name='statics'),
path('initialdata/', views.initialdata, name='initialdata'),
path('contact', views.contact, name='contact'),
path('register', views.register, name='register'),
path('authcheck', views.authcheck, name='authcheck'),
path('captcha', views.captcha, name='captcha'),
path('logout', views.logout, name='logout'),
path('', TemplateView.as_view(template_name="index.html")),
path('userlogin/', include('userlogin.urls')),
path('users/', include('users.urls')),
path('notebook/', include('notebook.urls')),
path('goods/', include('goods.urls')),
path('createuser/', include('createuser.urls')),
path('baseinfo/', include('baseinfo.urls')),
path('shipping/', include('shipping.urls')),
path('stockanalyst/', include('stockanalyst.urls')),
path('simorder/', include('simorder.urls')),
path('qrcodelist/', include('qrcodelist.urls')),
path('property/', include('property.urls')),
path('userauth/', include('userauth.urls')),
path('goodsunit/', include('goodsunit.urls')),
path('goodsspecs/', include('goodsspecs.urls')),
path('goodscity/', include('goodscity.urls')),
path('goodsshape/', include('goodsshape.urls')),
path('goodsbrand/', include('goodsbrand.urls')),
path('goodsclass/', include('goodsclass.urls')),
path('goodscolor/', include('goodscolor.urls')),
path('goodslist/', include('goodslist.urls')),
path('capitallist/', include('capitallist.urls')),
path('company/', include('company.urls')),
path('customer/', include('customer.urls')),
path('supplier/', include('supplier.urls')),
path('binsize/', include('binsize.urls')),
path('binset/', include('binset.urls')),
path('warehouseset/', include('warehouseset.urls')),
path('stafflist/', include('stafflist.urls')),
path('stocklist/', include('stocklist.urls')),
path('stockbinlist/', include('stockbinlist.urls')),
path('cyclecount/', include('cyclecount.urls')),
path('polist/', include('polist.urls')),
path('podetail/', include('podetail.urls')),
path('solist/', include('solist.urls')),
path('sodetail/', include('sodetail.urls')),
path('driverlist/', include('driverlist.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
