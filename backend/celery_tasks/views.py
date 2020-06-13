# -*- coding: utf-8 -*-
# author: itimor

from celery_tasks.serializers import *
from common.views import ModelViewSet, BulkModelMixin


class CrontabViewSet(BulkModelMixin):
    queryset = Crontab.objects.all()
    serializer_class = CrontabSerializer


class TaskScriptViewSet(BulkModelMixin):
    queryset = TaskScript.objects.all()
    serializer_class = TaskScriptSerializer


class PeriodicTaskViewSet(BulkModelMixin):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer
    search_fields = ['name']
    filter_fields = ['name']


class TaskResultViewSet(BulkModelMixin):
    queryset = TaskResult.objects.all()
    serializer_class = TaskResultSerializer
    filter_fields = ['task_name']

