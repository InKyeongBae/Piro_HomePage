from django.shortcuts import render,redirect

def main_page(request):
    return render(request,'main/main.html',{})