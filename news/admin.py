from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_At',)
    list_filter = ('created_At',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(News, NewsAdmin)
