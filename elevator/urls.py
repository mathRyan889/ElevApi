from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElevatorModelViewSet, ManufacturerModelViewSet

router = DefaultRouter()
router.register('elevator', ElevatorModelViewSet)
router.register('manufacturer', ManufacturerModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
