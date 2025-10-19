from django.urls import path
from . import views

urlpatterns = [
    path('users-ui/', views.users_view, name='users_ui'),
    path('properties-ui/', views.properties_view, name='properties_ui'),

    ####################################333
    path('add-user/', views.add_user, name='add_user'),
    path('edit-user/<int:pk>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:pk>/', views.delete_user, name='delete_user'),

    path('add-property/', views.add_property, name='add_property'),
    path('edit-property/<int:pk>/', views.edit_property, name='edit_property'),
    path('delete-property/<int:pk>/', views.delete_property, name='delete_property'),

    path('property/<int:pk>/users/', views.property_users_view, name='property_users'),

]
