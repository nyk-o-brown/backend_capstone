from django.urls import path
from . import views

#pp_name = 'property'  # Add namespace

urlpatterns = [
    # property app urls
    path('', views.property_list, name='property-list'),
]
