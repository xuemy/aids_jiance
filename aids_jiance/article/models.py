import hashlib
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import force_bytes, force_str, force_text
from aids_jiance.users.models import User


def md5_slug(s):
    s = force_bytes(s)
    return hashlib.md5(s).hexdigest()[8:-8]


class ArticleCategory(models.Model):
    name = models.CharField(max_length=20)
    slug = models.TextField(max_length=16, editable=False, unique=True)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'

    def get_absolute_url(self):
        return reverse('article:article_list', args=[self.slug])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = md5_slug(self.name)
        super(ArticleCategory, self).save(force_insert=False, force_update=False, using=None,
                                          update_fields=None)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', '草稿'),
        ('published', '发布'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(ArticleCategory, related_name='article', verbose_name='文章分类')
    name = models.TextField(max_length=255, verbose_name='文章名')
    slug = models.TextField(max_length=16, editable=False, unique=True)
    author = models.ForeignKey(User, related_name='aritlce', verbose_name='作者')
    body = RichTextUploadingField(verbose_name='正文')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stick = models.BooleanField(verbose_name='是否置顶', default=False)

    class Meta:
        ordering = ('-publish',)
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.slug])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = md5_slug(self.name)
        super(Article, self).save(force_insert=False, force_update=False, using=None,
                                  update_fields=None)

    def __str__(self):
        return self.name

