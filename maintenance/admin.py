from django.contrib import admin
from .models import Maintenance, ProviderCompany


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('elevator', 'type', 'status', 'responsible_technician', 'provider_company')
    list_filter = ('type', 'status', 'provider_company')
    search_fields = ('elevator__name', 'responsible_technician__username', 'provider_company__name')


class ProviderCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'tel')
    search_fields = ('name', 'cnpj')


admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(ProviderCompany, ProviderCompanyAdmin)
