from django import forms

from .models import ConferenceRoom


class RoomForm(forms.ModelForm):
    class Meta:
        model = ConferenceRoom
        fields = ['name', 'capacity', 'projector']
        labels = {'name': 'Name',
                  'capacity': 'Capacity',
                  'projector': 'Projector?'}
