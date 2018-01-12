from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Article, ArticleCategory


class CategoryArticleList(ListView):
    model = Article
    template_name = 'article/article_list.html'
    paginate_by = 15

    def get_queryset(self):
        category = get_object_or_404(ArticleCategory, pk=self.kwargs.get('pk'))
        setattr(self, 'category', category)
        return super(CategoryArticleList, self).get_queryset().filter(category=category)

    def get_context_data(self, **kwargs):
        context = super(CategoryArticleList, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'

    def get_object(self, queryset=None):
        cid = self.kwargs.get('cid')
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Article, category_id=cid, slug=slug)
        return obj

    def get(self, request, *args, **kwargs):
        response = super(ArticleDetailView, self).get(request, *args, **kwargs)
        self.object.add_views()
        return response


class AllArticleList(ListView):
    model = Article
    paginate_by = 20
    template_name = 'article/all_article_list.html'
