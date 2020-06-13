# -*- coding: utf-8 -*-
# author: itimor

from django.core.management.base import BaseCommand, CommandError
from systems.models import *
from systems.menus import init_menu


class Command(BaseCommand):
    help = '初始化工作流'

    def handle(self, *args, **options):
        topmenu = Menu.objects.get(name='top', code='top')
        self.stdout.write(self.style.SUCCESS('############ 初始化任务菜单 ###########'))
        celerymenu = Menu.objects.create(name='任务管理', code='celery_task', curl='/celery_task', icon='celery_task', sequence=4, type=1,
                                         parent_id=topmenu.id)
        menumodel = Menu.objects.create(name='cron配置', code='crontab', curl='/crontab', icon='crontab', sequence=10, type=2,
                                        parent_id=celerymenu.id)
        init_menu(menumodel)
        menumodel = Menu.objects.create(name='任务脚本', code='taskscript', curl='/taskscript', icon='taskscript', sequence=20, type=2,
                                        parent_id=celerymenu.id)
        init_menu(menumodel)
        menumodel = Menu.objects.create(name='任务', code='task', curl='/task', icon='task', sequence=30, type=2,
                                        parent_id=celerymenu.id)
        init_menu(menumodel)
        menumodel = Menu.objects.create(name='任务结果', code='taskresult', curl='/taskresult', icon='taskresult', sequence=40, type=2,
                                        parent_id=celerymenu.id)
        init_menu(menumodel)
        self.stdout.write(self.style.SUCCESS('初始化完成'))
