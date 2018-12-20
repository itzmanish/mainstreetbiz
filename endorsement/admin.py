from django.contrib import admin
from .models import Clients


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location',
                    'business_involved_in', 'created_at')
    list_display_links = ('name',)
    list_filter = ('created_at',)


admin.site.register(Clients, ClientsAdmin)
