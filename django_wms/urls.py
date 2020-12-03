"""django_wms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView, TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.static import serve as static_serve
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
   openapi.Info(
       title="GreaterWMS--API Docs",
       default_version='v2.0.0',
       description=
       """
        openid:
            Openid is the only mark of your data group, You shoud add it to you request headers.token .
        """
       ,
       terms_of_service="https://www.56yhz.com/",
       license=openapi.License(name="Apache License 2.0"),
   ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='dist/spa/index.html')),
    path('asn/', include('asn.urls')),
    path('staff/', include('staff.urls')),
    path('binset/', include('binset.urls')),
    path('binsize/', include('binsize.urls')),
    path('binproperty/', include('binproperty.urls')),
    path('chat/', include('chat.urls')),
    path('capital/', include('capital.urls')),
    path('driver/', include('driver.urls')),
    path('inbound/', include('inbound.urls')),
    path('stock/', include('stock.urls')),
    path('outbound/', include('outbound.urls')),
    path('company/', include('company.urls')),
    path('supplier/', include('supplier.urls')),
    path('customer/', include('customer.urls')),
    path('warehouse/', include('warehouse.urls')),
    path('goods/', include('goods.urls')),
    path('goodsunit/', include('goodsunit.urls')),
    path('goodsclass/', include('goodsclass.urls')),
    path('goodscolor/', include('goodscolor.urls')),
    path('goodsbrand/', include('goodsbrand.urls')),
    path('goodsshape/', include('goodsshape.urls')),
    path('goodsspecs/', include('goodsspecs.urls')),
    path('goodsorigin/', include('goodsorigin.urls')),
    path('payment/', include('payment.urls')),
    path('login/', include('userlogin.urls')),
    path('register/', include('userregister.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=r'static/img/logo.png')),
    re_path(r'^favicon\.ico$', views.favicon, name='favicon'),
    re_path(r'^root.txt', views.root, name='root'),
    re_path('^css/.*$', views.css, name='css'),
    re_path('^js/.*$', views.js, name='js'),
    re_path('^statics/.*$', views.statics, name='statics'),
    re_path('^fonts/.*$', views.fonts, name='fonts'),
    re_path(r'^robots.txt', views.robots, name='robots'),
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    re_path(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [re_path(r'^silk/', include('silk.urls', namespace='silk'))]
