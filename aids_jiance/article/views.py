from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Article


def ArticleList(request, slug):
    return



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
