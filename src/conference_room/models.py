from django.db import models


class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveSmallIntegerField()
    projector = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE,
                             related_name='booking')
    date = models.DateField()
    comment = models.TextField()

    class Meta:
        unique_together = ('room', 'date')

    def __str__(self):
        return str(self.date)
