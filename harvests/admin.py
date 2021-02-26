from django.contrib.gis import admin
from django.contrib.admin import register
from harvests.models import Bunch, BunchBatch, CategoryBunch, Harvester
from main.admin import BaseModelAdmin


@register(Bunch)
class BunchAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields,)
        }),
        ('Bunch', {
            'fields': ('category', 'weight')
        })
    )
    list_display = ('id', 'category', 'weight', 'creation_date')
    list_editable = ('category', 'weight')
    list_filter = ('category', 'creation_date')


@register(CategoryBunch)
class CategoryBunchAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields + ('is_active',),)
        }),
        ('Category', {
            'fields': ('name', 'description')
        })
    )
    list_display = ('id', 'name', 'creation_date', 'is_active')
    list_editable = ('name', 'is_active')
    list_filter = ('creation_date',)


@register(Harvester)
class HarvesterAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields,)
        }),
        ('Person', {
            'fields': ('name', 'address', 'email', 'phone', 'web')
        })
    )
    list_display = ('id', 'name', 'address', 'email', 'phone', 'creation_date')
    list_editable = ('name', 'address', 'email', 'phone')
    list_filter = ('creation_date',)


@register(BunchBatch)
class BunchBatchAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields + ('is_active',),)
        }),
        ('Batch', {
            'fields': ('delivery_time', 'bunches', 'notes')
        }),
        ('Source', {
            'fields': (('parcel', 'vehicle'), 'harvesters')
        })
    )
    filter_horizontal = ('bunches', 'harvesters')
    list_display = ('id', 'parcel', 'vehicle', 'delivery_time', 'is_active')
    list_editable = ('parcel', 'vehicle', 'is_active')
    list_filter = ('creation_date', 'delivery_time')

