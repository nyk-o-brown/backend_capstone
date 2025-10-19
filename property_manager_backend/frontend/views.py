#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
#################################################3
from django.shortcuts import render, redirect, get_object_or_404
from apps.users.forms import UserForm
from apps.property.forms import PropertyForm
from django.contrib.auth import get_user_model
from apps.property.models import Property

User = get_user_model()

def users_view(request):
    response = requests.get('http://127.0.0.1:8000/users/')
    users = response.json()
    return render(request, 'users.html', {'users': users})

def properties_view(request):
    response = requests.get('http://127.0.0.1:8000/property/')
    properties = response.json()
    return render(request, 'properties.html', {'properties': properties})



################################################33
def add_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('users_ui')
    return render(request, 'add_user.html', {'form': form})

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('users_ui')
    return render(request, 'edit_user.html', {'form': form})

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users_ui')

# PROPERTIES
def add_property(request):
    form = PropertyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        prop = form.save(commit=False)
        prop.owner = request.user  # or assign manually
        prop.save()
        return redirect('properties_ui')
    return render(request, 'add_property.html', {'form': form})

def edit_property(request, pk):
    prop = get_object_or_404(Property, pk=pk)
    form = PropertyForm(request.POST or None, request.FILES or None, instance=prop)
    if form.is_valid():
        form.save()
        return redirect('properties_ui')
    return render(request, 'edit_property.html', {'form': form})

def delete_property(request, pk):
    prop = get_object_or_404(Property, pk=pk)
    prop.delete()
    return redirect('properties_ui')

def property_users_view(request, pk):
    property = get_object_or_404(Property, pk=pk)
    units = property.units.select_related('tenant')
    return render(request, 'property_users.html', {'property': property, 'units': units})
