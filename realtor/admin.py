from django.contrib import admin
from .models import Realtor, Disclaimer, LegalDisclaimer, PrivacyPolicy
# Register your models here.


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'joined_at')
    list_display_links = ('name',)
    list_filter = ('joined_at',)
    search_fields = ('name', 'email', 'id')
    list_display_links = ('id', 'name',)
    ordering = ('id',)


@admin.register(Disclaimer)
class DisclaimerAdmin(admin.ModelAdmin):
    list_display = ('id', 'disclaimer')
    list_display_links = ('disclaimer',)


@admin.register(LegalDisclaimer)
class LegalDisclaimerAdmin(admin.ModelAdmin):
    list_display = ('id', 'legal_disclaimer', 'created_at')
    list_display_links = ('legal_disclaimer',)


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'privacy_policy', 'created_at')
    list_display_links = ('privacy_policy', )
