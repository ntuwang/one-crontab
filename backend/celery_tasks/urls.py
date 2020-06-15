# -*- coding: utf-8 -*-
# author: itimor


from django.conf.urls import url, include
from rest_framework import routers
from celery_tasks.views import TaskViewSet, TaskLogViewSet

router = routers.DefaultRouter()

router.register(r'task', TaskViewSet)
router.register(r'tasklog', TaskLogViewSet)

urlpatterns = [
]

urlpatterns += router.urls
