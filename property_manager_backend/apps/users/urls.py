from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # ✅ include is needed

urlpatterns = [
    path('users/', include('users.urls')),         # 🔗 routes to users app
    path('properties/', include('properties.urls'))  # 🔗 routes to properties app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
