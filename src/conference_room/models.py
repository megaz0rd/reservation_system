from django.db import models


class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveSmallIntegerField()
    projector = models.BooleanField(default=False)
