from django.contrib import admin
from .models import Article, ArticleCategory


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',  'publish', 'status', 'stick')
    list_filter = ('status', 'created', 'publish', )
    # prepopulated_fields = {
    #     'slug': ('title',)
    # }
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    list_editable = ['stick', 'status']
    readonly_fields = ('slug',)

    # fields = (
    #     ('category', 'status', 'stick', 'author'),
    #     ('name', 'slug'),
    #     'body','publish',
    # )
    fieldsets = (
        ('基本设置', {
            'fields': ('category', 'status', 'stick', )
        }),
        ('文章设置', {
            'fields': ('slug', 'name', 'body', 'publish')
        }),
        ('SEO设置', {
            'fields': ('seo_key', 'seo_desc')
        })
    )




class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_nav')
    list_editable = ['is_nav']

admin.site.register(ArticleCategory, ArticleCategoryAdmin)




