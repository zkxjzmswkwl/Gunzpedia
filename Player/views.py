from rest_framework import viewsets
from Player.serializers import PlayerSerializer
from Player.models import Player


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
