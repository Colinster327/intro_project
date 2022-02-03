from http.client import HTTPResponse
from django.shortcuts import render
from .models import Brands
from django.http import HttpResponse

# Create your views here.

def display_brands(request):
    brands_list = Brands.objects.all()
    context = {'brands_list': brands_list}
    return render(request, 'vehicles/display_brands.html', context)

