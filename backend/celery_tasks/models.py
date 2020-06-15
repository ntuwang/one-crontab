# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from common.models import BaseModel

code_type = {
    'shell': 'shell',
    'python': 'python',
}


class Task(BaseModel):
    name = models.CharField('名字', max_length=20, unique=True)
    args = models.CharField('参数', max_length=20, blank=True)
    status = models.BooleanField('状态', default=True)
    is_one = models.BooleanField('仅执行一次', default=False)
    cron = models.CharField('cron表达式', max_length=20, blank=True)
    code_type = models.CharField('code类型', max_length=10, choices=tuple(code_type.items()), default='shell')
    code = models.TextField('脚本代码', blank=True)
    start_time = models.DateTimeField('开始时间', blank=True)
    expire_time = models.DateTimeField('到期时间', blank=True)
    action_time = models.DateTimeField('执行时间', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '任务脚本'
        verbose_name_plural = verbose_name


status_type = {
    'running': 'running',
    'success': 'success',
    'fail': 'fail',
}


class TaskLog(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    args = models.CharField('参数', max_length=20, blank=True)
    status = models.CharField('状态', max_length=10, choices=tuple(status_type.items()), default='running')
    log = models.TextField('日志', blank=True)
    start_time = models.DateTimeField('开始时间', auto_now_add=True)
    end_time = models.DateTimeField('结束时间', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '任务脚本'
        verbose_name_plural = verbose_name
