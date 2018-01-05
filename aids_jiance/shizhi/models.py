from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class Shizhi(models.Model):
    name = models.CharField(max_length=200, verbose_name='试纸名称')
    slug = models.CharField(max_length=20, unique=True)
    bianhao = models.CharField(max_length=6, verbose_name='试纸编号', unique=True)
    cover = models.ImageField(verbose_name='封面图', upload_to='shizhi', null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = RichTextUploadingField(verbose_name='试纸介绍')

    seo_key = models.CharField(max_length=200, verbose_name='关键词', null=True, blank=True)
    seo_desc = models.CharField(max_length=255, verbose_name='页面描述', null=True, blank=True)

    is_taozhuang = models.BooleanField(default=False, verbose_name='是否是套装')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '试纸'
        verbose_name_plural = '试纸'

    def get_absolute_url(self):
        return reverse('shizhi_intro', args=[self.slug])

    def get_questions_url(self):
        return reverse('shizhi_questions', args=[self.slug])

class Questions(models.Model):
    shizhi = models.ForeignKey('Shizhi')
    name = models.CharField(max_length=200, verbose_name='问题')
    reply = RichTextUploadingField(verbose_name='答案')

    seo_key = models.CharField(max_length=200, verbose_name='关键词', null=True, blank=True)
    seo_desc = models.CharField(max_length=255, verbose_name='页面描述', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '问答'
        verbose_name_plural = '问答'

    def get_absolute_url(self):
        return reverse('shizhi_questions', args=[self.shizhi.slug])
