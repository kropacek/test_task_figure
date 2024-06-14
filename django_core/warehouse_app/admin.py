from django.contrib import admin

from .models import Truck, Warehouse


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ['board_number', 'model', 'max_load', 'current_load', 'overload_percentage', 'unload_coordinates',
                    'fe_percentage', 'sio2_percentage']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'volume_before_unload', 'volume_after_unload', 'sio2_percentage_before',
                    'sio2_percentage_after', 'fe_percentage_before', 'fe_percentage_after', 'polygon']

