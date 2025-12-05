from django.shortcuts import render

# Create your views here.

rooms = [
    {"id": 1, "name": "Python Room"},
    {"id": 2, "name": "Django Room"},
    {"id": 3, "name": "Java Room"},
]

def home_view(request):
    context = {"rooms": rooms}
    return render(request, 'main/home.html', context)


def room_view(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'main/room.html', context)