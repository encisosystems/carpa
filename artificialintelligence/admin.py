from artificialintelligence.models import ProcessedImage
from django.contrib import admin
from main.admin import BaseModelAdmin


@admin.register(ProcessedImage)
class ProcessedImageAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields ,)
        }),
        ('Data', {
            'fields': ('label', 'image', 'bunch')
        })
    )
    list_display = ('id', 'label', 'bunch', 'creation_date', 'update_date')
    list_editable = ('label', 'bunch')
    list_filter = ('creation_date',)
