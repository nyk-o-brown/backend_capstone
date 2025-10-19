#from django.shortcuts import render
#from django.http import HttpResponse

#def property_list(request):
#    return HttpResponse("List of properties")
## Property views go here


from rest_framework import viewsets, permissions
from .models import Property, Unit
from .serializers import PropertySerializer, UnitSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]  # allows GET to anonymous

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.AllowAny]