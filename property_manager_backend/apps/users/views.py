from django.shortcuts import render
# users/views.py
##from django.http import HttpResponse
#############
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

#
from rest_framework.permissions import AllowAny
#def user_list(request):
#    return HttpResponse("User list")
#
#def user_detail(request, id):
#    return HttpResponse(f"User detail for ID {id}")
#
## Create your views here.
User = get_user_model()

class IsAdminOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    


 
    