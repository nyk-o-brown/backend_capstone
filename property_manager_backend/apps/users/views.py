from django.shortcuts import render
# users/views.py
from django.http import HttpResponse

def user_list(request):
    return HttpResponse("User list")

def user_detail(request, id):
    return HttpResponse(f"User detail for ID {id}")

# Create your views here.
