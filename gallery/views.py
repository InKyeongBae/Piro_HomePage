from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import *
# Create your views here.


def gallery_view(request) :
    photos = Photo.objects.all()
    data = {
        'photos' : photos,
    }
    return render(request,'gallery/gallery_view.html',data)