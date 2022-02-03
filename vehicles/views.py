from http.client import HTTPResponse
from django.shortcuts import render
from .models import Brands
from .serializers import BrandsSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

def display_brands(request):
    brands_list = Brands.objects.all()
    context = {'brands_list': brands_list}
    return render(request, 'vehicles/display_brands.html', context)


class BrandsView(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
