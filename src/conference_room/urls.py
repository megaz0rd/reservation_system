"""Defines url patterns for conference_room app"""

from django.urls import path

from . import views

app_name = 'conference_room'

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('new/', views.add_room, name='add-room'),
    path('<int:id>/', views.room_detail, name='room-detail'),
    path('modify/<int:id>/', views.edit_room, name='edit-room'),
    path('delete/<int:id>/', views.delete_room, name='delete-room', ),
    path('reserve/<int:id>/', views.book_room, name='book-room'),
]
