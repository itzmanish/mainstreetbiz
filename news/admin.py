from django.contrib import admin
from .models import News, ImageUpload, ImageUploadFile


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_At',)
    list_display_links = ('title',)
    list_filter = ('created_At',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class UploadImageFileInline(admin.TabularInline):
    model = ImageUploadFile


@admin.register(ImageUpload)
class UploadImageAdmin(admin.ModelAdmin):
    inlines = [UploadImageFileInline, ]


admin.site.register(News, NewsAdmin)
