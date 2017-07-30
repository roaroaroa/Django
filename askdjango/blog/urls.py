#blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^factor$',views.factor),
    url(r'^select/$', views.select), #'/' 의 유무??
    url(r'^writing/$', views.writing),
    url(r'^search/$', views.search),
    url(r'^crawling_result/$', views.crawling_result),
    url(r'^new/$', views.post_new), #건의사항
    url(r'^recommend/$', views.recommend),
    url(r'^recommend_result/$', views.recommend_result),
    url(r'^board/$', views.board),
    url(r'^board_writing_form/$', views.board_writing_form),
    url(r'^viewboard/$', views.viewboard),
    url(r'^listPageWork/$', views.listPageWork), #자유게시판 [1],[2].. 
    url(r'^listPageWork1/$', views.listPageWork1), #검색한 결과의 페이지에서 [1],[2]..
    url(r'^searchWithSubject/$', views.searchWithSubject),


    
  
   
]