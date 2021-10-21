from rest_framework import viewsets
from Clan.models import Clan, ClanMember
from Clan.serializers import ClanSerializer, ClanMemberSerializer


class ClanViewSet(viewsets.ModelViewSet):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer


class ClanMemberViewSet(viewsets.ModelViewSet):
    queryset = ClanMember.objects.all()
    serializer_class = ClanMemberSerializer