from dj_rql.drf import RQLFilterBackend
from .permissions import ElevatorResponsiblePermission
from rest_framework import permissions
from .filters import ElevatorFilterClass, ManufacturerFilterClass
from rest_framework import viewsets
from .models import Elevator, Manufacturer
from .serializers import ElevatorModelSerializer, ManufacturerModelSerializer


class ElevatorModelViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ElevatorFilterClass
    permission_classes = [permissions.DjangoModelPermissions, ElevatorResponsiblePermission]


class ManufacturerModelViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ManufacturerFilterClass
