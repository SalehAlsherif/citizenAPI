from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CitizenViewSet
from django.contrib import admin
router = DefaultRouter()
router.register(r'citizens', CitizenViewSet)

urlpatterns = [
        path('admin/', admin.site.urls),  # ✅ This enables the admin panel
    path('', include(router.urls)),
    
]