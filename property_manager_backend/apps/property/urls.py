#from django.urls import path
#from . import views

#pp_name = 'property'  # Add namespace

#urlpatterns = [
#    # property app urls
#    path('', views.property_list, name='property-list'),
#]



from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet

router = DefaultRouter()
router.register("", PropertyViewSet, basename="property")

urlpatterns = router.urls
