from django.conf.urls import url
from . import views

urlpatterns = [
    # 全部文章列表
    url(regex=r'^$', view=views.AllArticleList.as_view(), name='category_list'),
    # 分类文章列表
    url(regex=r'^(?P<pk>\d+)/$', view=views.CategoryArticleList.as_view(), name='article_list'),
    # 文章详情页
    url(regex=r'^(?P<cid>\d+)_(?P<slug>\w+)$', view=views.ArticleDetailView.as_view(), name='article_detail')
]
