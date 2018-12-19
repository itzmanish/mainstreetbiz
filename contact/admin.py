from django.contrib import admin
from . import models


@admin.register(models.ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'listing_title', 'sent_at',)
    list_filter = ('sent_at', )
    list_display_links = ('id', 'name',)


@admin.register(models.ContactSelling)
class ContactSellingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'sent_at',)
    list_filter = ('sent_at', )
    list_display_links = ('id', 'name',)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'sent_at',)
    list_filter = ('sent_at', )
    list_display_links = ('id', 'name',)
