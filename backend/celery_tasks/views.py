# -*- coding: utf-8 -*-
# author: itimor

from celery_tasks.serializers import *
from common.views import ModelViewSet, BulkModelMixin


class CrontabScheduleViewSet(BulkModelMixin):
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer


class PeriodicTaskViewSet(BulkModelMixin):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer
    search_fields = ['name']
    filter_fields = ['name']
