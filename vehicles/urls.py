from django.urls import path
from .views import BrandsView

app_name = 'vehicles'

urlpatterns = [
    path('brands/', BrandsView.as_view({'get': 'list'}), name = "index")
]