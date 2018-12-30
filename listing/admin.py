from django.contrib import admin
from .models import Listing, Business_Type, Area, Status, FeaturedListing, CompletedDeals, ImageUpload, ImageUploadFile
from import_export.admin import ImportExportModelAdmin


class ListingAdmin(ImportExportModelAdmin):
    fields = ('Type', 'realtor', 'status', 'title', 'listing_id', 'area', 'business_type', 'description', 'price', 'finance',
              'image_main', 'image_1', 'image_2', 'image_3', 'image_4', 'disclaimer', 'is_published', 'is_sold', 'slug')
    list_display = ('id', 'title', 'listing_id', 'price', 'is_sold',
                    'created_at', 'realtor', 'status', 'is_published',)
    list_display_links = ('title', 'listing_id', )
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('realtor', 'created_at', 'status', 'is_sold',
                   'is_published',)
    list_editable = ('is_published', 'is_sold', )
    search_fields = ('listing_id', 'title', )
    ordering = ('listing_id',)
    list_per_page = 10


class Business_TypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'business_type', 'business_type_slug', )
    list_display_links = ('business_type',)
    prepopulated_fields = {'business_type_slug': ('business_type',)}
    search_fields = ('business_type', )


class AreaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'area', 'created_at')
    list_display_links = ('area',)
    prepopulated_fields = {'area_slug': ('area',)}
    search_fields = ('area', )


@admin.register(FeaturedListing)
class FeaturedListingAdmin(ImportExportModelAdmin):
    list_display = ('title', 'image', 'created_at')
    search_fields = ('title', )

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 3:
            return False
        else:
            return True


@admin.register(CompletedDeals)
class CompletedDealsAdmin(ImportExportModelAdmin):
    fields = ('Type', 'title', 'area',
              'subtitle', 'served_as', 'completion')
    list_display = ('id', 'title', 'area', 'Type', 'completion')
    list_display_links = ('title',)
    search_fields = ('title',)


class UploadImageFileInline(admin.TabularInline):
    model = ImageUploadFile


@admin.register(ImageUpload)
class UploadImageAdmin(admin.ModelAdmin):
    inlines = [UploadImageFileInline, ]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at')
    list_display_links = ('status',)


admin.site.register(Listing, ListingAdmin)
admin.site.register(Business_Type, Business_TypeAdmin)
admin.site.register(Area, AreaAdmin)
