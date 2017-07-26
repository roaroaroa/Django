#blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^post_list$', views.post_list ),
    url(r'^handling$', views.handling),
    url(r'^factor$',views.factor),
    url(r'^select/$', views.select), #'/' 의 유무??
    url(r'^writing$', views.writing),
    url(r'^search/$', views.search),
    url(r'^crawling_result_rice/$', views.crawling_result_rice),
    url(r'^crawling_result_water/$', views.crawling_result_water),
    url(r'^crawling_result_tissue/$', views.crawling_result_tissue),
    url(r'^new/$', views.post_new),
    url(r'^recommend/$', views.recommend),
    url(r'^recommend_result/$', views.recommend_result),
  
   
]