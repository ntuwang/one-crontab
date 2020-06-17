# -*- coding: utf-8 -*-
# author: itimor

import subprocess
from celery import shared_task
from croniter import croniter
from datetime import datetime, timedelta
import pytz
from django.conf import settings
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from celery_tasks.models import *
from utils.index import gen_time_pid


@shared_task
def get_task():
    """
    获取所有任务脚本，并执行
    """
    now = datetime.now()
    # 前一天
    # tz = pytz.timezone(settings.TIME_ZONE)
    tz = pytz.timezone('UTC')
    local_date = tz.localize(now)
    start = local_date - timedelta(hours=23, minutes=59, seconds=59)
    all_task = Task.objects.filter(status=True, start_time__lt=start, expire_time__gt=start)
    for task in all_task:
        iter = croniter(task.cron, local_date)
        t = iter.get_next(datetime)
        cron_obj, created = CrontabSchedule.objects.get_or_create(
            minute=t.minute, hour=t.hour, day_of_month=t.month,
            defaults={"month_of_year": t.year}
        )
        kwargs = dict()
        kwargs['type'] = task.code_type
        kwargs['code'] = task.code
        kwargs['args'] = task.args
        PeriodicTask.objects.update_or_create(
            name=task.name,
            defaults={
                "task": 'celery_tasks.tasks.run_task',
                "kwargs": kwargs,
                "enabled": True,
                "one_off": True,
                "crontab": cron_obj,
                "start_time": t,
                "expire_seconds": 60
            }
        )
        task.save()


@shared_task
def run_task(**kwargs):
    script_type = kwargs['type']
    script_code = kwargs['code']
    script_args = kwargs['args']
    script_name = "/tmp/" + gen_time_pid(type)
    with open(script_name, 'w') as fn:
        fn.read(script_code)

    if script_type == 'shell':
        r = subprocess.check_output(["basn", script_name, script_args], shell=True)
    elif script_type == 'python':
        r = subprocess.check_output(["python", script_name, script_args], shell=True)
    else:
        r = 'error'
    return r
