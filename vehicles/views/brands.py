from vehicles.models import Brands
from vehicles.serializers import BrandsSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class BrandsView(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer