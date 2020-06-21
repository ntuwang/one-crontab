# -*- coding: utf-8 -*-
# author: itimor

from celery_tasks.serializers import *
from common.views import ModelViewSet, BulkModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from celery_tasks.tasks import add


class TaskViewSet(BulkModelMixin):
    queryset = Task.objects.all().order_by("id")
    serializer_class = TaskSerializer
    filter_fields = ['name']


class TaskLogViewSet(BulkModelMixin):
    queryset = TaskLog.objects.all().order_by("id")
    serializer_class = TaskLogSerializer
    filter_fields = ['task']


class add(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': "success"}
        add.delay(1, 2)
        return Response(ret)
