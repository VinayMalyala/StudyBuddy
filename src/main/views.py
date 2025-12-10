from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import User, Room, Topic, Message
from .forms import UserForm, MyUserCreationForm, RoomForm

# Create your views here.

def login_view(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are logged in as {user.username}')
                return redirect('home')
            else:
                messages.error(request, 'Username or Password does not exist!')
        except:
            messages.error(request, 'User does not exist!')
    context = {'page': page}
    return render(request, 'main/login_register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        register_form = MyUserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, f'User {user.username} is registered successfully.')
            return redirect('home')
        else:
            messages.error(request, 'An Unknown error occured. Try again later!')
    else:
        register_form = MyUserCreationForm()
    return render(request, 'main/login_register.html', {'register_form': register_form})

def home_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
     ) # query upward to parent
    topics = Topic.objects.all()[0:5]
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {"rooms": rooms, "topics": topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'main/home.html', context)


def room_view(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == "POST":
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'main/room.html', context)

def profile_view(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()

    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'main/profile.html', context)

@login_required(login_url='login')
def create_room_view(request):
    room_form = RoomForm()
    topics = Topic.objects.all()

    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description'),
        )
        messages.success(request, "Room created sucessfully!")
        return redirect('home')
   
    context = {'room_form': room_form, 'topics': topics}
    return render(request, "main/room_form.html", context)

@login_required(login_url='login')
def update_room_view(request, pk):
    room = Room.objects.get(id=pk)
    room_form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        messages.error(request, "You are not allowed here!")
        return redirect('home')

    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        messages.success(request, "Room updated sucessfully!")
        return redirect('home')
        

    context = {'room': room, 'room_form': room_form, 'topics': topics}
    return render(request, "main/room_form.html", context)

@login_required(login_url='login')
def delete_room_view(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        messages.error(request, "You are not allowed to this!")
        return redirect('home')
    
    if request.method == "POST":
        room.delete()
        messages.success(request, f"Room {room} deleted sucessfully!")
        return redirect('home')
    return render(request, 'main/delete.html', {'obj': room})

@login_required(login_url='login')
def delete_message_view(request, pk):
    message = Message.objects.get(id=pk)
    room = message.room

    if request.user != message.user:
        messages.error(request, "You are not allowed to this!")
        return redirect('home')
    
    if request.method == "POST":
        message.delete()
        messages.success(request, f"Message deleted sucessfully!")
        return redirect('room', pk=room.id)
    return render(request, 'main/delete.html', {'obj': message})

@login_required(login_url='login')
def update_user_view(request, pk=None):
    """
    Edit a user's profile. If `pk` is provided, ensure only the owner can edit their profile
    (same guard as update_room_view). If no `pk` provided, the logged-in user edits their own profile.
    """
    # Determine target user: either the requested pk or the logged-in user
    if pk:
        try:
            target_user = User.objects.get(id=pk)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist!')
            return redirect('home')

        # Block non-owners from editing another user's profile
        if request.user != target_user:
            messages.error(request, "You are not allowed here!")
            return redirect('home')
    else:
        target_user = request.user

    user_form = UserForm(instance=target_user)

    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES, instance=target_user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f"Profile updated sucessfully!")
            return redirect('profile', pk=target_user.id)

    return render(request, 'main/update-user.html', {'user_form': user_form})

def topics_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'main/topics.html', {'topics': topics})

def activity_view(request):
    room_messages = Message.objects.all()
    return render(request, 'main/activity.html', {'room_messages': room_messages})