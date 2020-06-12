# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from django.db.models.signals import post_save
from django.dispatch import receiver
from common.models import BaseModel


class Crontab(models.Model):
    name = models.CharField(max_length=110, blank=True)
    cron = models.OneToOneField(CrontabSchedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'cron单位'
        verbose_name_plural = verbose_name


class Task(BaseModel):
    name = models.CharField(max_length=110, blank=True)
    code = models.CharField(max_length=32, unique=True, verbose_name='代码')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = verbose_name


@receiver(post_save, sender=CrontabSchedule)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Crontab.objects.create(user=instance)


@receiver(post_save, sender=CrontabSchedule)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
