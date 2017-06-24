from django.conf.urls import include, url
from .views import *


urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^register/', Register.as_view(), name='register'),
    url(r'^user_setting/$', Settings.as_view(), name='settings_user'),


]

