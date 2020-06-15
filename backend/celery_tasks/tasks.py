# -*- coding: utf-8 -*-
# author: itimor

from celery import shared_task
from croniter import croniter
from django.utils import timezone
from datetime import datetime, timedelta
from celery_tasks.models import *
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import logging


@shared_task
def get_task():
    """
    获取所有任务脚本，并设置下次执行时间
    """
    now = timezone.now()
    # 前一天
    start = now - timedelta(hours=23, minutes=59, seconds=59)
    all_task = Task.objects.filter(status=True, start_time__lt=start, expire_time__gt=start)
    for task in all_task:
        logging.error(task.name)
        iter = croniter(task.cron, now)
        t = iter.get_next(datetime)
        logging.error(t)
        cron_obj, created = CrontabSchedule.objects.get_or_create(minute=t.minute, hour=t.hour, day_of_month=t.month, month_of_year=t.year)
        logging.error(cron_obj)
        PeriodicTask.objects.create(
            name=task.name,
            task='celery_tasks.tasks.run_task',
            args=task.args,
            enabled=True,
            one_off=True,
            crontab=cron_obj,
            start_time=t
        )
        task.save()


@shared_task
def run_task(name):
    print(name)
