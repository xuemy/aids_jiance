from django.contrib import admin
from .models import Article, ArticleCategory, ExtendSite


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author', 'publish', 'status', 'stick')
    list_filter = ('status', 'created', 'publish', 'author')
    # prepopulated_fields = {
    #     'slug': ('title',)
    # }
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    list_editable = ['stick', 'status']
    readonly_fields = ('slug',)

    fields = (
        ('category', 'status', 'stick', 'author'),
        ('name', 'slug'),
        'body','publish',
    )


admin.site.register(Article, ArticleAdmin)


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_nav')
    list_editable = ['is_nav']

admin.site.register(ArticleCategory, ArticleCategoryAdmin)



@admin.register(ExtendSite)
class ExtendSiteAdmin(admin.ModelAdmin):
    pass
