from django.shortcuts import render, redirect

from .models import Room
from .forms import RoomForm

# Create your views here.

def home_view(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, 'main/home.html', context)


def room_view(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'main/room.html', context)

def create_room_view(request):
    if request.method == "POST":
        try:
            room_form = RoomForm(request.POST)
            if room_form.is_valid():
                room_form.save()
                return redirect('home')

        except Exception as e:
            pass

    elif request.method == "GET":
        room_form = RoomForm()
    context = {'room_form': room_form}
    return render(request, "main/room_form.html", context)

def update_room_view(request, pk):
    room = Room.objects.get(id=pk)
    room_form = RoomForm(instance=room)

    if request.method == "POST":
        try:
            room_form = RoomForm(request.POST, instance=room)
            if room_form.is_valid():
                room_form.save()
                return redirect('home')
        except Exception as e:
            pass

    context = {'room_form': room_form}
    return render(request, "main/room_form.html", context)

def delete_room_view(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'main/delete.html', {'obj': room})