from django.contrib import admin
from .models import BuyersDirectoryPage, Register
from import_export.admin import ImportExportModelAdmin


@admin.register(BuyersDirectoryPage)
class BuyersDirectoryPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(Register)
class RegisterAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'phone', 'created_at')
    list_display_links = ('first_name',)
    list_filter = ('created_at',)
