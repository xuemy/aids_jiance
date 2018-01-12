from .models import ArticleCategory, Article
from django.utils import timezone

def is_nav(request):
    return {
        'navs': ArticleCategory.objects.filter(is_nav=True).all(),
        'categorys': ArticleCategory.objects.all(),
        'year':timezone.now().year,
        'sticks': Article.get_stick(),
    }
