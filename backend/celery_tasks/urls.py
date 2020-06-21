# -*- coding: utf-8 -*-
# author: itimor


from django.conf.urls import url, include
from rest_framework import routers
from celery_tasks.views import TaskViewSet, TaskLogViewSet, one_add

router = routers.DefaultRouter()

router.register(r'task', TaskViewSet)
router.register(r'tasklog', TaskLogViewSet)

urlpatterns = [
    url(r'^one_add/', one_add.as_view()),
]

urlpatterns += router.urls
