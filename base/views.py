from django.shortcuts import render
from .models import Room


rooms = Room.objects.all()


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == pk:
            room = i

    context = {'room': room}
    return render(request, 'base/room.html', context)
