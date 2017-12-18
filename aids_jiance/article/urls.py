from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^c/(?P<slug>\w+)/$', view=views.ArticleList, name='article_list'),
    url(regex=r'^a/(?P<slug>\w+)/$', view=views.ArticleDetailView.as_view(), name='article_detail')
]
