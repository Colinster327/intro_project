from django.urls import path
from . import views

app_name = 'vehicles'

urlpatterns = [
    path('', views.display_brands, name = "index")
]