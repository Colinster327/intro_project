from vehicles.models import Vehicles
from vehicles.serializers import VehiclesSerializer
from rest_framework import viewsets

# Create your views here.

class BrandsView(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer