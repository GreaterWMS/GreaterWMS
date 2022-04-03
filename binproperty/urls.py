from django.urls import path
from . import views

urlpatterns = [
path(r'', views.APIViewSet.as_view({"get": "list"}), name="binproperty")
]
