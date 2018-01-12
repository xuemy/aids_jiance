from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.sites.models import Site
from django.db import models


class ExtendSite(models.Model):
    site = models.OneToOneField(Site, related_name='extend')
    logo = models.ImageField(upload_to='logo', null=True, blank=True)

    seo_title = models.CharField(max_length=200, verbose_name='首页标题', blank=True)
    seo_key = models.CharField(max_length=200, verbose_name='首页关键词', blank=True)
    seo_desc = models.CharField(max_length=255, verbose_name='首页页面描述', blank=True)

    analytics = models.TextField(max_length=40, blank=True, verbose_name='统计代码')
    zice = RichTextUploadingField(verbose_name='自测症状持续添加', blank=True)
    shiyong = RichTextUploadingField(verbose_name='试纸使用方法', blank=True)

    def __str__(self):
        return self.site.name

    class Meta:
        verbose_name = 'SIte 扩展'
        verbose_name_plural = 'SIte 扩展'


class Ad(models.Model):
    site = models.OneToOneField(Site, related_name='ad')
    ad1 = models.TextField()
    ad2 = models.TextField()
    ad3 = models.TextField()
    ad4 = models.TextField()
    ad5 = models.TextField()
    ad6 = models.TextField()

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = '广告'

    def __str__(self):
        return '页面广告'

class FriendLink(models.Model):
    site = models.ForeignKey(Site, related_name='friendlink', null=True)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    logo = models.ImageField(upload_to='friendlink/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
