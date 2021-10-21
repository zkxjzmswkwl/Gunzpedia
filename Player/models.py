from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=32)
    time_active = models.CharField(max_length=32)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    alias_one = models.CharField(max_length=32, blank=True, null=True)
    alias_two = models.CharField(max_length=32, blank=True, null=True)
    alias_three = models.CharField(max_length=32, blank=True, null=True)
    alias_four = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"