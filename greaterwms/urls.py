from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.views import serve
from django.views.static import serve as static_serve
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from utils.apitag import api_tags
from . import views

from drf_yasg.generators import OpenAPISchemaGenerator

class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
  def get_schema(self, request=None, public=False):
    """Generate a :class:`.Swagger` object with custom tags"""
    swagger = super().get_schema(request, public)
    swagger.tags = api_tags(request.META.get("HTTP_ACCEPT_LANGUAGE", ''))
    return swagger

schema_view = get_schema_view(
    openapi.Info(
       title="GreaterWMS--API Docs",
       default_version='v2.1.25',
       description=
       """
        openid:
            Openid is the only mark of your data group, You should add it to you request headers.token .
        """
       ,
       terms_of_service="https://www.56yhz.com/",
       license=openapi.License(name="APLv2"),
    ),
    public=True,
    generator_class=CustomOpenAPISchemaGenerator,
    permission_classes=(permissions.AllowAny, ),
)

def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='dist/spa/index.html')),
    path('myip/', views.myip, name='myip'),
    path('asn/', include('asn.urls')),
    path('dn/', include('dn.urls')),
    path('staff/', include('staff.urls')),
    path('binset/', include('binset.urls')),
    path('binsize/', include('binsize.urls')),
    path('binproperty/', include('binproperty.urls')),
    path('chat/', include('chat.urls')),
    path('capital/', include('capital.urls')),
    path('driver/', include('driver.urls')),
    path('stock/', include('stock.urls')),
    path('company/', include('company.urls')),
    path('cyclecount/', include('cyclecount.urls')),
    path('dashboard/', include('dashboard.urls')),
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
    path('scanner/', include('scanner.urls')),
    path('shopid/', include('shopid.urls')),
    path('payment/', include('payment.urls')),
    path('login/', include('userlogin.urls')),
    path('register/', include('userregister.urls')),
    path('uploadfile/', include('uploadfile.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^favicon\.ico$', views.favicon, name='favicon'),
    re_path('^css/.*$', views.css, name='css'),
    re_path('^js/.*$', views.js, name='js'),
    re_path('^statics/.*$', views.statics, name='statics'),
    re_path('^fonts/.*$', views.fonts, name='fonts'),
    re_path(r'^robots.txt', views.robots, name='robots'),
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    re_path(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += [re_path(r'^silk/', include('silk.urls', namespace='silk'))]
