# -*- coding: utf-8 -*-
# author: itimor


from django.conf.urls import url, include
from rest_framework import routers
from celery_tasks.views import CrontabScheduleViewSet, PeriodicTaskViewSet

router = routers.DefaultRouter()

router.register(r'crontab', CrontabScheduleViewSet)
router.register(r'task', PeriodicTaskViewSet)


urlpatterns = [
]

urlpatterns += router.urls
