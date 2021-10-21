from rest_framework import serializers
from Clan.models import Clan, ClanMember


class ClanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clan
        fields = '__all__'


class ClanMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClanMember
        fields = '__all__'
