from django.db import models
from Clan.models import Clan


class Player(models.Model):
    name = models.CharField(max_length=32)
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE, related_name="clan")
    clan_leader = models.ForeignKey(Clan, on_delete=models.CASCADE, related_name="clan_leader")
    time_active = models.CharField(max_length=32)
    alias_one = models.CharField(max_length=32)
    alias_two = models.CharField(max_length=32)
    alias_three = models.CharField(max_length=32)
    alias_four = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"