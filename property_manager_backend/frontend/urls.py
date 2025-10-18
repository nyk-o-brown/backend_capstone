from django.urls import path
from . import views

urlpatterns = [
    path('users-ui/', views.users_view, name='users_ui'),
    path('properties-ui/', views.properties_view, name='properties_ui'),
]
