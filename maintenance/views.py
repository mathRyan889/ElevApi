from rest_framework import viewsets
from .models import Maintenance, ProviderCompany
from .serializers import MaintenanceModelSerializer, ProviderCompanyModelSerializer
from dj_rql.drf import RQLFilterBackend
from .filters import MaintenanceFilterClass, ProviderCompanyFilterClass


class MaintenanceModelViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = MaintenanceFilterClass


class ProviderCompanyModelViewSet(viewsets.ModelViewSet):
    queryset = ProviderCompany.objects.all()
    serializer_class = ProviderCompanyModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ProviderCompanyFilterClass
