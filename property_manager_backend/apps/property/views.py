#from django.shortcuts import render
#from django.http import HttpResponse

#def property_list(request):
#    return HttpResponse("List of properties")
## Property views go here


from rest_framework import viewsets, permissions
from .models import Property
from .serializers import PropertySerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.select_related("owner").all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
