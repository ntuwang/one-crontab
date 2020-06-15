# -*- coding: utf-8 -*-
# author: itimor

from celery_tasks.models import *
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        extra_kwargs = {'action_time': {'read_only': True}}
        fields = '__all__'


class TaskLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskLog
        fields = '__all__'
