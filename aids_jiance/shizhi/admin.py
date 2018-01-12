from django.contrib import admin
from .models import Shizhi, Questions


@admin.register(Shizhi)
class ShizhiAdmin(admin.ModelAdmin):
    list_editable = ('is_taozhuang', )
    list_display = ('name', 'bianhao', 'is_taozhuang')


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    pass

