from rest_framework import serializers
from .models import Maintenance, ProviderCompany


class MaintenanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'


class ProviderCompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderCompany
        fields = '__all__'
