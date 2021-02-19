from django.shortcuts import render,redirect
from .models import *

def main_page(request):
    desc_img = MainDescImg.objects.first()
    print(desc_img.second_img)
    interviews = MainInterview.objects.all()[:4]
    ctx = {
        'desc_img':desc_img,
        'interviews':interviews,
    }
    return render(request,'main/main.html', ctx)