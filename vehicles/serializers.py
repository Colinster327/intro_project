from rest_framework import serializers
from .models import Brands, Vehicles

class VehiclesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = ['name']

class BrandsSerializer(serializers.ModelSerializer):
    vehicles = VehiclesSerializer(many=True)

    class Meta:
        model = Brands
        fields = ['name', 'vehicles']