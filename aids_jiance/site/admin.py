from django.contrib import admin
from .models import ExtendSite, FriendLink, Ad

@admin.register(ExtendSite)
class ExtendSiteAdmin(admin.ModelAdmin):
    pass

@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    pass

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    pass