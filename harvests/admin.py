from django.contrib.gis import admin
from django.contrib.admin import register
from harvests.models import Bunch, CategoryBunch, Harvester
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
    list_display = ('id', 'category', 'creation_date', 'update_date')
    list_filter = ('category', 'creation_date')


@register(CategoryBunch)
class CategoryBunchAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields + ('is_active',),)
        }),
        ('Category', {
            'fields': ('name', 'description',)
        })
    )
    list_display = ('id', 'name', 'creation_date', 'update_date')
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
    list_display = ('id', 'name', 'creation_date', 'update_date')
    list_filter = ('creation_date', 'is_active')
