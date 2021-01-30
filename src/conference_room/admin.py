from django.contrib import admin

from .models import Booking, ConferenceRoom

admin.site.register(ConferenceRoom)
admin.site.register(Booking)
