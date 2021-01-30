from django.shortcuts import redirect, render
from django.views.generic import ListView

from .models import ConferenceRoom
from .forms import RoomForm


class index(ListView):
    model = ConferenceRoom
    template_name = 'base.html'
    context_object_name = 'rooms'



def add_room(request):
    if request.method != 'POST':
        form = RoomForm()
    else:
        form = RoomForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('conference_room:index')

    context = {'form': form}
    return render(request, 'add_room.html', context)

def room_detail(request, id):
    rooms = ConferenceRoom.objects.get(pk=id)
    context = {
        'rooms': rooms
    }
    return render(request, 'room_detail.html', context)