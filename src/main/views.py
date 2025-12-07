from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, f'You are logged in as {user.username}')
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist!')
    context = {}
    return render(request, 'main/login_register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
     ) # query upward to parent
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {"rooms": rooms, "topics": topics, 'room_count': room_count}
    return render(request, 'main/home.html', context)


def room_view(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'main/room.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def update_room_view(request, pk):
    room = Room.objects.get(id=pk)
    room_form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed here!")

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

@login_required(login_url='login')
def delete_room_view(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'main/delete.html', {'obj': room})