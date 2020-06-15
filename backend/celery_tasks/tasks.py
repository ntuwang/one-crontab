# -*- coding: utf-8 -*-
# author: itimor

from celery import shared_task
from croniter import croniter
from django.utils import timezone
from datetime import datetime, timedelta
from celery.schedules import crontab
from celery_tasks.models import *
from celery_tasks.celery import celery_app


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
        iter = croniter(task.cron, now)
        task.action_time = iter.get_next(datetime)
        task.save()


@shared_task
def get_action_task():
    """
    获取当前需要执行的任务脚本并执行
    """
    now = timezone.now()
    all_task = Task.objects.filter(status=True, action_time=now)
    for task in all_task:
        print(task.name, task.code, task.args)
        celery_app.conf.update(
            CELERYBEAT_SCHEDULE={
                task.name: {
                    'task': 'celery_tasks.tasks.run_task',
                    'schedule': crontab(hour=4, minute=30, day_of_week=1),
                }
            }
        )


@shared_task
def run_task(name):
    print(name)
