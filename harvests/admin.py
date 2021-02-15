from django.contrib import admin
from harvests.models import Bunch, CategoryBunch, BatchSource
from main.admin import BaseModelAdmin


@admin.register(Bunch)
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
    list_display = ('id', 'category', 'creation_date', 'update_date' )
    list_filter = ('category',)


@admin.register(CategoryBunch)
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


@admin.register(BatchSource)
class BatchSourceAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': ('location', 'city'),
        }),
        ('Audit', {
            'fields': BaseModelAdmin.readonly_fields
        })
    )
    list_display = ('id', 'city', 'creation_date', 'update_date' )
    list_filter = ('city', 'creation_date')
