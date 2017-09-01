#coding:utf8
from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index ,name='index'),
    url(r'^(?P<qid>\d+)/$', views.detail ,name='detail'), # 投票详情页（包括投票选项）
    url(r'^results/(?P<qid>\d+)/$', views.resuls ,name='results'), # 投票结果
    url(r'^votes/(?P<qid>\d+)/$', views.vote ,name='votes'), # 投票操作
]
