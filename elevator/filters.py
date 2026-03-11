from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Elevator, Manufacturer


class ElevatorFilterClass(AutoRQLFilterClass):
    MODEL = Elevator


class ManufacturerFilterClass(AutoRQLFilterClass):
    MODEL = Manufacturer
