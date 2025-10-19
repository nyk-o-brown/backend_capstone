from rest_framework import serializers
from .models import Property
from .models import Unit

class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = ["id", "name", "location", "photo", "photo_url", "owner", "created_at"]
        read_only_fields = ["id", "owner", "created_at", "photo_url"]

    def get_photo_url(self, obj):
        request = self.context.get("request")
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
