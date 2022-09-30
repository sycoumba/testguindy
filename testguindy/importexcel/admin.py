from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Categories
# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
     
    