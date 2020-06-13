# -*- coding: utf-8 -*-
# author: itimor


from django.conf.urls import url, include
from rest_framework import routers
from celery_tasks.views import CrontabViewSet, TaskScriptViewSet, PeriodicTaskViewSet, TaskResultViewSet

router = routers.DefaultRouter()

router.register(r'crontab', CrontabViewSet)
router.register(r'taskscript', TaskScriptViewSet)
router.register(r'task', PeriodicTaskViewSet)
router.register(r'taskresult', TaskResultViewSet)


urlpatterns = [
]

urlpatterns += router.urls
