from dj_rql.filter_cls import AutoRQLFilterClass
from .models import ProviderCompany, Maintenance


class ProviderCompanyFilterClass(AutoRQLFilterClass):
    MODEL = ProviderCompany


class MaintenanceFilterClass(AutoRQLFilterClass):
    MODEL = Maintenance
