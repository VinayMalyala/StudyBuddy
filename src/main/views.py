from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse("This is the home page")

def room_view(request):
    return HttpResponse("This is the room page")