# -*- coding: utf-8 -*-
# author: itimor

from celery import shared_task


@shared_task
def django_sum(x, y):
    s = x + y
    return s


@shared_task
def django_max(x, y):
    if x > y:
        return x
    else:
        return y
