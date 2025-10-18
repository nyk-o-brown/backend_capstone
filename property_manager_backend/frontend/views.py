#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests

def users_view(request):
    response = requests.get('http://127.0.0.1:8000/users/')
    users = response.json()
    return render(request, 'users.html', {'users': users})

def properties_view(request):
    response = requests.get('http://127.0.0.1:8000/property/')
    properties = response.json()
    return render(request, 'properties.html', {'properties': properties})
