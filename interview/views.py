from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import *
# Create your views here.
def non_major_interview(request) :
    
    return render(request,'interview/non_major_interview.html',data)

def major_interview(request) :
    interviewees = Answer.objects.filter(major = '전공자')
    data = {
        'interviewees' : interviewees,
    }
    return render(request,'interview/major_interview.html',data)

def double_major_interview(request) :
    
    return render(request,'interview/double_major_interview.html',data)


def interview_view(request, pk):
    interview = Answer.objects.filter(pk=pk)
    data={
        'interview' : interview,
    }
    return render(request, 'interview/interview_view.html',data )

