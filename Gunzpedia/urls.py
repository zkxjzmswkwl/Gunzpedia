from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# Apps
from Clan.views import ClanViewSet, ClanMemberViewSet
from Player.views import PlayerViewSet

router = routers.DefaultRouter()
router.register(r'clans', ClanViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'clan_members', ClanMemberViewSet)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/', include(router.urls))
]
