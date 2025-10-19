from django.db import models
from django.conf import settings
##################################3
from django.contrib.auth import get_user_model

#class Property(models.Model):
#    description = models.TextField(blank=True)
#    price = models.DecimalField(max_digits=10, decimal_places=2)
#    address = models.CharField(max_length=255)
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)
#
#class PropertyImage(models.Model):
#    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
#    image = models.ImageField(upload_to='property_images/')

def property_image_path(instance, filename):
  return f"property/{instance.owner.id}/{filename}"


User = get_user_model()

class Property(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="property")
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=property_image_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    name = models.CharField(max_length=100)
    floor = models.CharField(max_length=20, blank=True)
    tenant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='rented_units')

    def __str__(self):
        return self.name

