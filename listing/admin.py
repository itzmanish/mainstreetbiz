from django.contrib import admin
from .models import Listing, Business_Type, Area, Status
from import_export.admin import ImportExportModelAdmin


class ListingAdmin(ImportExportModelAdmin):
    list_display = ('listing_id', 'title', 'price',
                    'created_at', 'realtor', 'status', 'is_published', 'is_featured')
    list_display_links = ('title', 'listing_id', )
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('realtor', 'created_at', 'status',
                   'is_published', 'is_featured')
    list_editable = ('is_published', 'status', 'is_featured')
    search_fields = ('listing_id', 'title', )
    ordering = ('listing_id',)
    list_per_page = 10


class Business_TypeAdmin(ImportExportModelAdmin):
    list_display = ('business_type', 'business_type_slug', )
    prepopulated_fields = {'business_type_slug': ('business_type',)}
    search_fields = ('business_type', )


class AreaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'area', 'created_at')
    prepopulated_fields = {'area_slug': ('area',)}
    search_fields = ('area', )


admin.site.register(Listing, ListingAdmin)
admin.site.register(Business_Type, Business_TypeAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Status)
