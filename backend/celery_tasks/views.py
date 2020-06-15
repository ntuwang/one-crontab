# -*- coding: utf-8 -*-
# author: itimor

from celery_tasks.serializers import *
from common.views import ModelViewSet, BulkModelMixin


class TaskViewSet(BulkModelMixin):
    queryset = Task.objects.all().order_by("id")
    serializer_class = TaskSerializer
    filter_fields = ['name']


class TaskLogViewSet(BulkModelMixin):
    queryset = TaskLog.objects.all().order_by("id")
    serializer_class = TaskLogSerializer
    filter_fields = ['task']
