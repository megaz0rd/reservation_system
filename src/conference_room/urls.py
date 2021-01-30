"""Defines url patterns for conference_room app"""

from django.urls import path

from . import views

app_name = 'conference_room'

urlpatterns = [
    path('', views.index, name='index'),
]
