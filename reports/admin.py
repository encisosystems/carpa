from django.contrib import admin
from django.contrib.admin import register

# Register your models here.
from main.admin import BaseModelAdmin
from reports.models import Report


@register(Report)
class ReportAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields,)
        }),
        ('Report', {
            'fields': ('date', 'bunchBatch', 'block', 'lot')
        })
    )
    list_display = ('id', 'bunchBatch', 'block', 'lot', 'creation_date', 'update_date')
    list_filter = ('creation_date', 'is_active',) 
