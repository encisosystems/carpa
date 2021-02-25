from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from main.admin import BaseModelAdmin
from sources.models import Parcel, ParcelOwner, Driver, Vehicle


@admin.register(ParcelOwner)
class ParcelOwnerAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields,)
        }),
        ('Person', {
            'fields': (('first_name', 'last_name',),)
        }),
        ('Address', {
            'fields': ('organization', 'address_1', 'address_2',)
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'website',)
        })
    )
    list_display = ('id', 'first_name', 'last_name', 'address_1', 'email',)
    list_filter = ('creation_date',)


@admin.register(Parcel)
class ParcelAdmin(gis_admin.OSMGeoAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields + ('is_active',),)
        }),
        ('Parcel information', {
            'fields': ('name', 'owner',),
        }),
        ('Physical information', {
            'fields': ('location', 'extension',),
        })
    )
    list_display = ('id', 'name', 'owner', 'extension',)
    list_filter = ('creation_date',)
    default_lat = 459132.20787
    default_lon = -8195052.12787
    default_zoom = 15


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields,)
        }),
        ('Driver', {
            'fields': ('name', 'address', 'email', 'phone', 'web')
        }),
    )
    list_display = ('id', 'name', 'creation_date', 'update_date')
    list_filter = ('creation_date',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': ('enrollment', 'modelVehicle', 'brand', 'driver'),
        }),
        ('Audit', {
            'fields': BaseModelAdmin.readonly_fields
        })
    )
    list_display = ('id', 'enrollment', 'modelVehicle', 'brand',
                    'driver', 'creation_date', 'update_date')
    list_filter = ('enrollment', 'modelVehicle',
                   'brand', 'driver', 'creation_date')
