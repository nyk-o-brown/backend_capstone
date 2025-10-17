#from django.conf import settings
#from django.conf.urls.static import static
#from django.urls import path, include  # ✅ include is needed
#from . import views

#urlpatterns = [
#        path('', views.user_list, name='user-list'),
#        path('<int:id>/', views.user_detail, name='user-detail'),
#]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register("", UserViewSet, basename="user")

urlpatterns = router.urls
