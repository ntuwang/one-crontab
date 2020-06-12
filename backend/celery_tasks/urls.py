# -*- coding: utf-8 -*-
# author: itimor


from django.conf.urls import url, include
from rest_framework import routers
from celery_tasks.views import CrontabScheduleViewSet, CrontabViewSet, TaskViewSet, PeriodicTaskViewSet

router = routers.DefaultRouter()

router.register(r'crontabschedule', CrontabScheduleViewSet)
router.register(r'crontab', CrontabViewSet)
router.register(r'task', TaskViewSet)
router.register(r'periodictask', PeriodicTaskViewSet)


urlpatterns = [
]

urlpatterns += router.urls
