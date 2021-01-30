import datetime

from django import forms

from .models import Booking, ConferenceRoom


class RoomForm(forms.ModelForm):
    class Meta:
        model = ConferenceRoom
        fields = ['name', 'capacity', 'projector']
        labels = {
            'capacity': 'Num of seats',
            'projector': 'Projector?',
        }


class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Booking
        fields = ['room', 'date', 'comment']
        widgets = {
            'room': forms.HiddenInput(),
            'date': forms.SelectDateWidget(),
            'comment': forms.Textarea(attrs={'placeholder': 'Your comment '
                                                            'here...',
                                             'rows': 20,
                                             'cols': 50})
        }
        labels = {
            'date': '',
            'comment': '',
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date
