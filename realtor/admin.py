from django.contrib import admin
from .models import Realtor, Disclaimer, LegalDisclaimer, PrivacyPolicy
# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'joined_at')
    list_filter = ('joined_at',)
    search_fields = ('name', 'email', 'id')
    list_display_links = ('id', 'name',)
    ordering = ('id',)


admin.site.register(Realtor, RealtorAdmin)
admin.site.register(Disclaimer)
admin.site.register(LegalDisclaimer)
admin.site.register(PrivacyPolicy)
