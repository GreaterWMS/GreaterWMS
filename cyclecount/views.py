from dateutil.relativedelta import relativedelta
from django.http import StreamingHttpResponse
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.settings import api_settings
from .files import FileRenderCN, FileRenderEN
from .models import CyclecountModeDayModel
from . import serializers
from utils.page import MyPageNumberPagination
from .page import CycleCountPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import Filter
from .filter import QTYRecorderListFilter
from rest_framework.exceptions import APIException
from .serializers import FileRenderSerializer, FileRenderAllSerializer
from .models import QTYRecorder
import datetime

class QTYRecorderViewSet(viewsets.ModelViewSet):
    """
        list:
            Response a data list（all）

    """

    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = QTYRecorderListFilter

    def get_queryset(self):
        if self.request.user:
            return QTYRecorder.objects.filter(openid=self.request.auth.openid)
        else:
            return QTYRecorder.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.QTYRecorderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

class CyclecountModeDayViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）

        list:
            Response a data list（all）

        create:
            Create a data line（post）

        delete:
            Delete a data line（delete)

        partial_update:
            Partial_update a data（patch：partial_update）

        update:
            Update a data（put：update）
    """
    pagination_class = None
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            cur_date = timezone.now()
            delt_date = relativedelta(days=1)
            if id is None:
                return CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid, cyclecount_status=0,
                                                             update_time__gte=str((cur_date -delt_date).date()) + ' 00:00:00',
                                                             update_time__lte=str((cur_date + delt_date).date()) + ' 00:00:00')
            else:
                return CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid, cyclecount_status=0,
                                                             update_time__gte=str((cur_date - delt_date).date()) + ' 00:00:00',
                                                             update_time__lte=str((cur_date + delt_date).date()) + ' 00:00:00', id=id)
        else:
            return CyclecountModeDayModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.CyclecountGetSerializer
        elif self.action in ['create']:
            return serializers.CyclecountPostSerializer
        elif self.action in ['update']:
            return serializers.CyclecountUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        for i in range(len(data)):
            CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid,
                                                  t_code=data[i]['t_code']).update(
                physical_inventory=data[i]['physical_inventory'], cyclecount_status=1,
                difference=data[i]['physical_inventory'] - data[i]['goods_qty'])
        return Response({"detail": "success"}, status=200)

    def update(self, request, *args, **kwargs):
        data = self.request.data
        for i in range(len(data)):
            scan_count_data = self.get_queryset().filter(openid=self.request.auth.openid,
                                                  t_code=data[i]['t_code']).first()
            scan_count_data.physical_inventory = scan_count_data.physical_inventory + data[i]['physical_inventory']
            scan_count_data.difference = data[i]['physical_inventory'] - data[i]['goods_qty']
            scan_count_data.cyclecount_status = 1
            scan_count_data.save()
        return Response({"detail": "success"}, status=200)

class CyclecountModeAllViewSet(viewsets.ModelViewSet):
    """
        list:
            Response a data list（get）
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            date_choice = self.request.GET.get('create_time', '')
            cur_time = timezone.now().date()
            if date_choice:
                if id is None:
                    return CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid, cyclecount_status=1,
                                                                 update_time__gte=str(date_choice) + ' 00:00:00',
                                                                 update_time__lte=str(date_choice) + ' 23:59:59')
                else:
                    return CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid, cyclecount_status=1,
                                                                 update_time__gte=str(date_choice) + ' 00:00:00',
                                                                 update_time__lte=str(date_choice) + ' 23:59:59',
                                                                 id=id)
            else:
                if id is None:
                    return CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid, cyclecount_status=1,
                                                                 update_time__gte=str(cur_time) + ' 00:00:00',
                                                                 update_time__lte=str(cur_time) + ' 23:59:59')
                else:
                    return CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid, cyclecount_status=1,
                                                                 update_time__gte=str(cur_time) + ' 00:00:00',
                                                                 update_time__lte=str(cur_time) + ' 23:59:59',
                                                                 id=id)
        else:
            return CyclecountModeDayModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.CyclecountGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)


class FileDownloadView(viewsets.ModelViewSet):
    renderer_classes = (FileRenderCN, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time"]
    filter_class = Filter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            cur_date = timezone.now()
            delt_date = relativedelta(days=1)
            if id is None:
                return CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid, cyclecount_status=0,
                                                             update_time__gte=str((cur_date -delt_date).date()) + ' 00:00:00')
            else:
                return CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid, cyclecount_status=0,
                                                             update_time__gte=str((cur_date -delt_date).date()) + ' 00:00:00', id=id)
        else:
            return CyclecountModeDayModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.FileRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def get_lang(self, data):
        lang = self.request.META.get('HTTP_LANGUAGE')
        if lang:
            if lang == 'zh-hans':
                return FileRenderCN().render(data)
            else:
                return FileRenderEN().render(data)
        else:
            return FileRenderEN().render(data)

    def list(self, request, *args, **kwargs):
        from datetime import datetime
        dt = datetime.now()
        data = (
            FileRenderSerializer(instance).data
            for instance in self.filter_queryset(self.get_queryset())
        )
        renderer = self.get_lang(data)
        response = StreamingHttpResponse(
            renderer,
            content_type="text/csv"
        )
        response['Content-Disposition'] = "attachment; filename='cyclecount_{}.csv'".format(str(dt.strftime('%Y%m%d%H%M%S%f')))
        return response

class FileDownloadAllView(viewsets.ModelViewSet):
    renderer_classes = (FileRenderCN, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time"]
    filter_class = Filter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
            id = self.get_project()
            if self.request.user:
                cur_date = timezone.now()
                delt_date = relativedelta(days=1)
                if id is None:
                    return CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid, cyclecount_status=1,
                                                                 update_time__gte=str((cur_date -delt_date).date()) + ' 00:00:00',
                                                                 update_time__lte=str((cur_date + delt_date).date()) + ' 23:59:59')
                else:
                    return CyclecountModeDayModel.objects.filter(openid=self.request.auth.openid, cyclecount_status=1,
                                                                 update_time__gte=str((cur_date - delt_date).date()) + ' 00:00:00',
                                                                 update_time__lte=str((cur_date + delt_date).date()) + ' 23:59:59', id=id)
            else:
                return CyclecountModeDayModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.FileRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def get_lang(self, data):
        lang = self.request.META.get('HTTP_LANGUAGE')
        if lang:
            if lang == 'zh-hans':
                return FileRenderCN().render(data)
            else:
                return FileRenderEN().render(data)
        else:
            return FileRenderEN().render(data)

    def list(self, request, *args, **kwargs):
        from datetime import datetime
        dt = datetime.now()
        data = (
            FileRenderAllSerializer(instance).data
            for instance in self.filter_queryset(self.get_queryset())
        )
        renderer = self.get_lang(data)
        response = StreamingHttpResponse(
            renderer,
            content_type="text/csv"
        )
        response['Content-Disposition'] = "attachment; filename='cyclecountall_{}.csv'".format(str(dt.strftime('%Y%m%d%H%M%S%f')))
        return response
