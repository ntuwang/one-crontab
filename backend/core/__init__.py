from __future__ import absolute_import, unicode_literals
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
# import pymysql
#
# pymysql.install_as_MySQLdb()

# 如果有用到celery,开启下面注释
from celery_tasks.celery import celery_app
__all__ = ['celery_app']