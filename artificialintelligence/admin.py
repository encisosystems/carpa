from artificialintelligence.models import ProcessedImage
from django.contrib import admin
from main.admin import BaseModelAdmin


@admin.register(ProcessedImage)
class ProcessedImageAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': ('label', 'image', 'bunches'),
        }),
        ('Audit', {
            'fields': BaseModelAdmin.readonly_fields
        })
    )
    list_display = ('id', 'label', 'creation_date', 'update_date')
    list_filter = ('creation_date',)
