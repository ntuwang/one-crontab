# -*- coding: utf-8 -*-
# author: itimor

from django_celery_beat.models import CrontabSchedule, PeriodicTask
from rest_framework import serializers
import timezone_field


class CrontabScheduleSerializer(serializers.ModelSerializer):
    timezone = serializers.ChoiceField(choices=['Asia/Shanghai', 'UTC'])

    class Meta:
        model = CrontabSchedule
        fields = '__all__'


class PeriodicTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = ['id', 'name', 'task', 'args', 'kwargs', 'enabled', 'last_run_at', 'total_run_count', 'crontab', 'one_off', 'start_time', 'expires']
