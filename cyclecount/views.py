import traceback
from dateutil.relativedelta import relativedelta
from django.http import StreamingHttpResponse
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.settings import api_settings
from .files import FileRenderCN, FileRenderEN
from .models import CyclecountModeDayModel
from . import serializers
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import Filter
from .filter import ManualFilter
from .filter import QTYRecorderListFilter
from .serializers import FileRenderSerializer, FileRenderAllSerializer
from .models import QTYRecorder
from .models import ManualCyclecountModeModel
from userprofile.models import Users
from stock.views import StockBinViewSet
from utils.md5 import Md5
from staff.models import ListModel as staff

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

class GetGoodsCyclecountViewSet(StockBinViewSet):
    """
        list:
            Response a data list（get）
    """
    pagination_class = None

    def list(self, request, *args, **kwargs):
        staff_name = staff.objects.filter(openid=self.request.auth.openid, id=self.request.META.get('HTTP_OPERATOR')).first().staff_name
        queryset = self.filter_queryset(self.get_queryset())
        goods_code = self.request.GET.get('goods_code', '')
        for i in queryset:
            if (d:=ManualCyclecountModeModel.objects.filter(cyclecount_status=0, bin_name=i.bin_name, goods_code=goods_code)).exists():
                d.delete()
            data = {
                'openid': self.request.auth.openid,
                'creater': staff_name,
                'cyclecount_status': 0,
                'bin_name': i.bin_name,
                'goods_code': goods_code,
                'goods_qty': i.goods_qty,
                'physical_inventory': 0,
                'difference': 0,
                't_code': Md5.md5(goods_code)
            }
            serializer = serializers.ManualCyclecountPostSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        queryset = ManualCyclecountModeModel.objects.filter(goods_code=goods_code, cyclecount_status=0)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = serializers.ManualCyclecountGetSerializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = serializers.ManualCyclecountGetSerializer(instance=queryset, many=True)
        return Response(serializer.data)

class ManualCyclecountViewSet(viewsets.ModelViewSet):
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
    filter_class = ManualFilter

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
            u = Users.objects.filter(vip=9).first()
            if u is None:
                superopenid = None
            else:
                superopenid = u.openid
            query_dict = {
                'cyclecount_status': 0,
                'update_time__gte': str((cur_date - delt_date).date()) + ' 00:00:00',
                'update_time__lte': str((cur_date + delt_date).date()) + ' 00:00:00'
            }
            if self.request.auth.openid != superopenid:
                query_dict['openid'] = self.request.auth.openid
            if id is not None:
                query_dict['id'] = id
            return ManualCyclecountModeModel.objects.filter(**query_dict)
        else:
            return ManualCyclecountModeModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.ManualCyclecountGetSerializer
        elif self.action in ['create']:
            return serializers.ManualCyclecountModeModel
        elif self.action in ['update']:
            return serializers.ManualCyclecountUpdateSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        for i in range(len(data)):
            ManualCyclecountModeModel.objects.filter(openid=self.request.auth.openid, t_code=data[i]['t_code']).update(
                physical_inventory=data[i]['physical_inventory'],
                cyclecount_status=1,
                difference=data[i]['physical_inventory'] - data[i]['goods_qty']
            )
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

class ManualCyclecountRecorderViewSet(viewsets.ModelViewSet):
    """
        list:
            Response a data list（get）
    """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = ManualFilter

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
            u = Users.objects.filter(vip=9).first()
            if u is None:
                superopenid = None
            else:
                superopenid = u.openid
            query_dict = {
                'cyclecount_status': 1
            }
            if self.request.auth.openid != superopenid:
                query_dict['openid'] = self.request.auth.openid
            if date_choice:
                query_dict['update_time__gte'] = str(date_choice) + ' 00:00:00'
                query_dict['update_time__lte'] = str(date_choice) + ' 23:59:59'
            else:
                query_dict['update_time__gte'] = str(cur_time) + ' 00:00:00'
                query_dict['update_time__lte'] = str(cur_time) + ' 23:59:59'
            if id is not None:
                query_dict['id'] = id
            return ManualCyclecountModeModel.objects.filter(**query_dict)
        else:
            return ManualCyclecountModeModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.ManualCyclecountGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

class ManualFileDownloadView(viewsets.ModelViewSet):
    renderer_classes = (FileRenderCN, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time"]
    filter_class = ManualFilter

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
            u = Users.objects.filter(vip=9).first()
            if u is None:
                superopenid = None
            else:
                superopenid = u.openid
            query_dict = {
                'cyclecount_status': 0,
                'update_time__gte': str((cur_date - delt_date).date()) + ' 00:00:00'
            }
            if self.request.auth.openid != superopenid:
                query_dict['openid'] = self.request.auth.openid
            if id is not None:
                query_dict['id'] = id
            return ManualCyclecountModeModel.objects.filter(**query_dict)
        else:
            return ManualCyclecountModeModel.objects.none()

    def get_serializer_class(self):
        if self.action in ['list']:
            return serializers.ManualFileRenderSerializer
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
            serializers.ManualFileRenderSerializer(instance).data
            for instance in self.filter_queryset(self.get_queryset())
        )
        renderer = self.get_lang(data)
        response = StreamingHttpResponse(
            renderer,
            content_type="text/csv"
        )
        response['Content-Disposition'] = "attachment; filename='manualcyclecount_{}.csv'".format(str(dt.strftime('%Y%m%d%H%M%S%f')))
        return response
