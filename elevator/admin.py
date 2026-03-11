from django.contrib import admin
from .models import Elevator, Manufacturer


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'tel')
    search_fields = ('name', 'cnpj')


class ElevatorAdmin(admin.ModelAdmin):
    list_display = (
        'serial_number', 'manufacturer', 'responsible_technician', 'model',
        'capacity_kg', 'num_floors', 'installation_location',
        'installation_date', 'status', 'created_at', 'updated_at'
    )

    search_fields = ('serial_number', 'manufacturer', 'model')

    list_filter = ('status',)


admin.site.register(Elevator, ElevatorAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
