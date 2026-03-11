from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaintenanceModelViewSet, ProviderCompanyModelViewSet

router = DefaultRouter()
router.register('maintenance', MaintenanceModelViewSet)
router.register('provider-companies', ProviderCompanyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
