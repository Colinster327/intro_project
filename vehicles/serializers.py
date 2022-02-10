from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from rest_framework import serializers
from .models import Brands, Vehicles

class VehiclesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = "__all__"

class BrandsSerializer(serializers.ModelSerializer):
    vehicles = VehiclesSerializer(read_only=True, many=True)

    class Meta:
        model = Brands
        fields = "__all__"