from __future__ import absolute_import
import os

from celery import Celery
from django.conf import settings

# устанавливаем settings модуль для приложения celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataBase_Walmart.settings')

# создаем celery-приложение
app = Celery('DataBase_Walmart')

# используем установки django-проекта в celery-приложении
app.config_from_object('django.conf:settings')

# автоопределение задач из django-проекта
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)