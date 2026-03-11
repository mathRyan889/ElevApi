from rest_framework import serializers
from .models import Elevator, Manufacturer


class ElevatorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'


class ManufacturerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'
