from django.contrib.gis import admin
from django.contrib.admin import register
from harvests.models import (
    Bunch,
    CategoryBunch,
    BatchSource,
    BunchBatch
)
from main.admin import BaseModelAdmin


@register(Bunch)
class BunchAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': ('category', 'weight'),
        }),
        ('Audit', {
            'fields': BaseModelAdmin.readonly_fields
        })
    )
    list_display = ('id', 'category', 'creation_date', 'update_date')
    list_filter = ('category',)


@register(CategoryBunch)
class CategoryBunchAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': ('name', 'description'),
        }),
        ('Audit', {
            'fields': BaseModelAdmin.readonly_fields
        })
    )
    list_display = ('id', 'name', 'creation_date', 'update_date')


@register(BatchSource)
class BatchSourceAdmin(admin.OSMGeoAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': ('location', 'city'),
        }),
        ('Audit', {
            'fields': BaseModelAdmin.readonly_fields
        })
    )
    list_display = ('id', 'city', 'creation_date', 'update_date')
    list_filter = ('city', 'creation_date')
    default_lat = 454018.69011
    default_lon = -8191521.69263
    default_zoom = 17


@register(BunchBatch)
class BunchBatchAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': ('batch_source', 'bunch'),
        }),
        ('Audit', {
            'fields': BaseModelAdmin.readonly_fields
        })
    )
    raw_id_fields = ('batch_source', 'bunch')
    list_display = ('id', 'batch_source', 'bunch')
    list_filter = ('batch_source', 'bunch')
    list_display_links = list_display

