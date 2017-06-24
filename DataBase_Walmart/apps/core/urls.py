from django.conf.urls import url

from DataBase_Walmart.apps.core import views

urlpatterns = [
    url(r'^way_items/$', views.way_items, name='way_items'),
    url(r'^onlinejson/$', views.onlinejson, name='onlinejson'),
    url(r'^delete_items/$', views.delete_items, name='delete_items'),
    url(r'^data_import/$', views.data_import, name='data_import'),
    url(r'^csv_list/$', views.csv_list, name='csv_list'),

]