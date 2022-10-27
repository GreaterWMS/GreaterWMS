from django.urls import path
from . import views

urlpatterns = [
path(r'', views.CyclecountModeDayViewSet.as_view({"get": "list", "post": "create", 'put': 'update'}), name="cyclecount"),
path(r'cyclecountrecorder/', views.CyclecountModeAllViewSet.as_view({"get": "list"}), name="cyclecountrecorder"),
path(r'filecyclecountday/', views.FileDownloadView.as_view({"get": "list"}), name="filecyclecountday"),
path(r'filecyclecountall/', views.FileDownloadAllView.as_view({"get": "list"}), name="filecyclecountall"),

path(r'qtyrecorviewset/', views.QTYRecorderViewSet.as_view({"get": "list"}), name="qtyrecorviewset"),
path(r'getgoodscyclecount/', views.GetGoodsCyclecountViewSet.as_view({"get": "list"}), name="getgoodscyclecount"),
path(r'manualcyclecount/', views.ManualCyclecountViewSet.as_view({"post": "create", "get": "list"}), name="manualcyclecount"),
path(r'manualfilecyclecount/', views.ManualFileDownloadView.as_view({"get": "list"}), name="manualfilecyclecount"),
path(r'manualcyclecountrecorder/', views.ManualCyclecountRecorderViewSet.as_view({"get": "list"}), name="manualcyclecountrecorder")
]
