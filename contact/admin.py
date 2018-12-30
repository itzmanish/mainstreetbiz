from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin


@admin.register(models.ContactModel)
class ContactModelAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'listing_title', 'sent_at',)
    list_display_links = ('name',)
    list_filter = ('sent_at', )
    list_display_links = ('id', 'name',)


@admin.register(models.ContactSelling)
class ContactSellingAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'sent_at',)
    list_display_links = ('name',)
    list_filter = ('sent_at', )
    list_display_links = ('id', 'name',)


@admin.register(models.Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'sent_at',)
    list_display_links = ('name',)
    list_filter = ('sent_at', )
    list_display_links = ('id', 'name',)
