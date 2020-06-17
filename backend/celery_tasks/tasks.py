# -*- coding: utf-8 -*-
# author: itimor

from celery import shared_task
from croniter import croniter
from django.utils import timezone
from datetime import datetime, timedelta
from celery_tasks.models import *
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from django.conf import settings


@shared_task
def get_task():
    """
    获取所有任务脚本，并执行
    """
    now = timezone.now()
    # 前一天
    start = now - timedelta(hours=23, minutes=59, seconds=59)
    all_task = Task.objects.filter(status=True, start_time__lt=start, expire_time__gt=start)
    for task in all_task:
        iter = croniter(task.cron, now)
        t = iter.get_next(datetime)
        cron_obj, created = CrontabSchedule.objects.get_or_create(minute=t.minute, hour=t.hour, day_of_month=t.month, month_of_year=t.year, timezone=settings.TIME_ZONE)
        args = [task.code_type]
        PeriodicTask.objects.create(
            name=task.name,
            task='celery_tasks.tasks.run_task',
            args=args + task.args.split(','),
            enabled=True,
            one_off=True,
            crontab=cron_obj,
            start_time=t
        )
        task.save()


@shared_task
def run_task(x, y):
    print(y)
