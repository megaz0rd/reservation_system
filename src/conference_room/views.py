from django.shortcuts import redirect, render

from .forms import RoomForm


def index(request):
    return render(request, 'base.html')


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
