from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^$', view=views.CategoryList.as_view(), name='category_list'),
    url(regex=r'^(?P<pk>\d+)/$', view=views.ArticleList.as_view(), name='article_list'),
    url(regex=r'^(?P<cid>\d+)_(?P<slug>\w+)$', view=views.ArticleDetailView.as_view(), name='article_detail')
]
