from django.shortcuts import render
from .models import Destination


def feed(request):
     
    dests= Destination.objects.all()
    return render(request, "feed.html", {'dests':dests})