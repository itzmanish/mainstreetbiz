from django.contrib import admin
from .models import Document, FileUpload, DocumentUpload


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_at')
    list_display_links = ('title',)
    list_filter = ('uploaded_at',)


class UploadFileInline(admin.TabularInline):
    model = DocumentUpload


@admin.register(FileUpload)
class UploadImageAdmin(admin.ModelAdmin):
    inlines = [UploadFileInline, ]


admin.site.register(Document, DocumentAdmin)
