from vehicles.views.brands import BrandsView
from vehicles.views.vehicles import VehiclesView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('brands', BrandsView, basename='brands')
router.register('vehicles', VehiclesView, basename='vehicles')