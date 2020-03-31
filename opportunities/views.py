from django.shortcuts import render
from .models import Post


def opportunities(request):
    posts= Post.objects.all()
    return render(request, "opportunities.html", {'posts': posts})

 
