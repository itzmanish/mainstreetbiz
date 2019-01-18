from django.contrib import admin
from .models import BusinessListing, Business_Type, Area, Status, FeaturedListing, CompletedDeals, ImageUpload, ImageUploadFile, CommercialListing
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ImportExportMixin
from adminsortable.admin import SortableAdmin


@admin.register(BusinessListing)
class BusinessListingAdmin(ImportExportMixin, SortableAdmin):
    sortable_change_list_with_sort_link_template = 'admin/change_list_import_export_sortable.html'
    list_display = ('id', 'business', 'listing_id', 'asking_price',
                    'created_at', 'status', )
    list_display_links = ('business', 'listing_id', )
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'status',)
    # list_editable = ('is_published', 'is_sold', )
    search_fields = ('listing_id', 'business', )
    ordering = ('my_order',)
    list_per_page = 10


@admin.register(CommercialListing)
class CommercialListingAdmin(ImportExportMixin, SortableAdmin):
    sortable_change_list_with_sort_link_template = 'admin/change_list_import_export_sortable.html'
    list_display = ('id', 'business', 'listing_id', 'asking_price',
                    'created_at', 'status', )
    list_display_links = ('business', 'listing_id', )
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'status',)
    # list_editable = ('is_published', 'is_sold', )
    search_fields = ('listing_id', 'business', )
    ordering = ('my_order',)
    list_per_page = 10


class Business_TypeAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'business_type', )
    list_display_links = ('business_type',)

    search_fields = ('business_type', )


class AreaAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'area', 'created_at')
    list_display_links = ('area',)

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


admin.site.register(Business_Type, Business_TypeAdmin)
admin.site.register(Area, AreaAdmin)
