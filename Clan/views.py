from rest_framework.decorators import action
from rest_framework import permissions, viewsets
from Clan.models import Clan
from Clan.serializers import ClanSerializer


class ClanViewSet(viewsets.ModelViewSet):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer