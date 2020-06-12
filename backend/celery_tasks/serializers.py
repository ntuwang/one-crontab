# -*- coding: utf-8 -*-
# author: itimor

from celery_tasks.models import *
from rest_framework import serializers


class CrontabScheduleSerializer(serializers.ModelSerializer):
    timezone = serializers.ChoiceField(choices=['Asia/Shanghai', 'UTC'])

    class Meta:
        model = CrontabSchedule
        fields = '__all__'


class CrontabSerializer(serializers.ModelSerializer):
    cron = CrontabScheduleSerializer(required=True)

    class Meta:
        model = Crontab
        fields = ['id', 'name', 'cron']

    def create(self, validated_data):
        name = validated_data.pop('name')
        cron = validated_data.pop('cron')
        print(cron)
        cron_data = CrontabScheduleSerializer.create(CrontabScheduleSerializer(), validated_data=cron)
        print(cron_data)
        crontab, created = Crontab.objects.create(cron=cron_data, name=name)
        return crontab


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class PeriodicTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = ['id', 'name', 'task', 'args', 'kwargs', 'enabled', 'last_run_at', 'total_run_count', 'crontab', 'one_off', 'start_time', 'expires']
