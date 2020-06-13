# -*- coding: utf-8 -*-
# author: itimor

from celery_tasks.serializers import *
from common.views import ModelViewSet, BulkModelMixin


class CrontabViewSet(BulkModelMixin):
    queryset = Crontab.objects.all()
    serializer_class = CrontabSerializer


class TaskViewSet(BulkModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class PeriodicTaskViewSet(BulkModelMixin):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer
    search_fields = ['name']
    filter_fields = ['name']
