from vehicles.views import BrandsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('brands', BrandsView, basename='brands')