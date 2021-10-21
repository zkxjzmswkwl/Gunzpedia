from django.db import models


class Clan(models.Model):
    name = models.CharField(max_length=32)
    tourny_won = models.BooleanField(default=False)
    time_active = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}, lead by {self.leader.name}"