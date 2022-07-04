from django.contrib import admin
from linebotApp import *
from linebotApp.models import HH
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.


class HHAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'number', 'price', 'text',)
    list_filter = ('number', 'price')
    search_fields = ('number',)
    ordering = ('id',)


admin.site.register(HH, HHAdmin)
