import hashlib
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

from django.contrib.sites.models import Site
from django.db import models
# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import force_bytes, force_str, force_text



def md5_slug(s):
    s = force_bytes(s)
    return hashlib.md5(s).hexdigest()[8:-8]


class ArticleCategory(models.Model):
    name = models.CharField(max_length=20)
    slug = models.TextField(max_length=16, editable=False, unique=True)
    is_nav = models.BooleanField(verbose_name='是否在nav显示', default=False)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'

    def get_absolute_url(self):
        return reverse('article:article_list', args=[self.id])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
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
    name = models.CharField(max_length=255, verbose_name='文章名')
    slug = models.TextField(max_length=16, editable=False, unique=True)

    # author = models.ForeignKey(User, related_name='aritlce', verbose_name='作者')

    body = RichTextUploadingField(verbose_name='正文')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stick = models.BooleanField(verbose_name='是否置顶', default=False)
    views = models.PositiveIntegerField(default=5268, verbose_name='阅读统计量')

    seo_key = models.CharField(max_length=200, verbose_name='关键词', null=True, blank=True)
    seo_desc = models.CharField(max_length=255, verbose_name='页面描述', null=True, blank=True)
    class Meta:
        ordering = ('-publish',)
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.category.id, self.slug])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = md5_slug(self.name)
        super(Article, self).save(force_insert=False, force_update=False, using=None,
                                  update_fields=None)

    def add_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.name


class ExtendSite(models.Model):
    site = models.OneToOneField(Site, related_name='extend')
    logo = models.ImageField(upload_to='logo', null=True, blank=True)

    seo_title = models.CharField(max_length=200, verbose_name='首页标题', blank=True)
    seo_key = models.CharField(max_length=200, verbose_name='首页关键词', blank=True)
    seo_desc = models.CharField(max_length=255, verbose_name='首页页面描述',  blank=True)

    baidu_analytics = models.CharField(max_length=40, blank=True, verbose_name='百度统计ID')
    google_analytics = models.CharField(max_length=40, blank=True, verbose_name='Google统计ID')

    def __str__(self):
        return self.site.name

    class Meta:
        verbose_name = 'SIte 扩展'
        verbose_name_plural = 'SIte 扩展'

