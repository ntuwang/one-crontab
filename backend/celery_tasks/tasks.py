# -*- coding: utf-8 -*-
# author: itimor

from celery import shared_task


@shared_task
def django_sum(x, y):
    s = x + y
    print(s)
    return s


@shared_task
def django_max(x, y):
    print(x)
    if x > y:
        return x
    else:
        return y
