from django.shortcuts import render
from django.http import HttpResponse

def property_list(request):
    return HttpResponse("List of properties")
# Property views go here
