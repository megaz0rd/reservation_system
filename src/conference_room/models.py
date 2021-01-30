from django.db import models


class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveSmallIntegerField()
    projector = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Booking(models.Model):
    room_id = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE,
                                related_name='booking')
    date = models.DateTimeField()
    comment = models.TextField()

    class Meta:
        unique_together = ('room_id', 'date')

    def __str__(self):
        return self.date
