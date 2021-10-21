from django.db import models
from Player.models import Player


class Clan(models.Model):
    name = models.CharField(max_length=32, unique=True)
    leader = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    tourny_won = models.BooleanField(default=False)
    time_active = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class ClanMember(models.Model):
    member = models.ForeignKey(Player, on_delete=models.CASCADE)
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.name}"