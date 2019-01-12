from django.contrib import admin
from .models import FeedUrl, FeedPost
# Register your models here.


@admin.register(FeedUrl)
class FeedUrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'site_url',)
    list_display_links = ('site_name',)


@admin.register(FeedPost)
class FeedPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'date')
    list_display_links = ('title',)
