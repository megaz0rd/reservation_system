from datetime import date

from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView

from .models import Booking, ConferenceRoom
from .forms import BookingForm, RoomForm


class RoomList(ListView):
    model = ConferenceRoom
    template_name = 'base.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        return context


class SearchRoom(RoomList):
    template_name = 'search_room.html'

    def get_queryset(self):
        data = self.request.GET
        name = data.get('name', '')
        min_capacity = data.get('min_capacity', '')
        projector = data.get('projector')

        if name != '':
            return ConferenceRoom.objects.filter(name__icontains=name)
        elif min_capacity != '':
            return ConferenceRoom.objects.filter(capacity__gte=min_capacity)
        elif projector == 'on':
            return ConferenceRoom.objects.filter(projector=1)


def add_room(request):
    if request.method != 'POST':
        form = RoomForm()
    else:
        form = RoomForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conference_room:index')

    context = {
        'form': form
    }
    return render(request, 'add_room.html', context)


def room_detail(request, id):
    room = get_object_or_404(ConferenceRoom, pk=id)
    booking = room.booking.filter(date__gte=date.today()).order_by('date')

    context = {
        'room': room,
        'booking': booking,
    }
    return render(request, 'room_detail.html', context)


def edit_room(request, id):
    room = get_object_or_404(ConferenceRoom, pk=id)
    if request.method != 'POST':
        form = RoomForm(instance=room)
    else:
        form = RoomForm(instance=room, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conference_room:index')

    context = {
        'room': room, 'form': form
    }
    return render(request, 'edit_room.html', context)


def delete_room(request, id):
    '''

    Delete object with confirm

    '''
    room = get_object_or_404(ConferenceRoom, pk=id)
    if request.method == 'POST':
        room.delete()
        return redirect('conference_room:index')

    context = {
        'room': room
    }
    return render(request, 'delete_room.html', context)


def book_room(request, id):
    room = get_object_or_404(ConferenceRoom, pk=id)
    booking = room.booking.filter(date__gte=date.today()).order_by('date')
    initial_data = {
        'room': room.id
    }
    if request.method != 'POST':
        form = BookingForm(initial=initial_data)
    else:
        form = BookingForm(initial=initial_data, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conference_room:index')

    context = {
        'room': room, 'form': form, 'booking': booking,
    }
    return render(request, 'book_room.html', context)
