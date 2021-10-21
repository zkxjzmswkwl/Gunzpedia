from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# Apps
from Clan.views import ClanViewSet


router = routers.DefaultRouter()
router.register(r'clans', ClanViewSet)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/', include(router.urls))
]
