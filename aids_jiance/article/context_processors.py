from .models import ArticleCategory


def is_nav(request):
    return {
        'navs': ArticleCategory.objects.filter(is_nav=True).all(),
        'categorys': ArticleCategory.objects.all(),
    }
