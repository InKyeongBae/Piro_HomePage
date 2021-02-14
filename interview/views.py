from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.
def interview_list(request):
    return HttpResponse('인터뷰이 등록 성공')

def interviewee_create(request):
    if request.method == 'POST':
        form = IntervieweeForm(request.POST, request.FILES) 
        if form.is_valid():  
            post = form.save()  
            return redirect('interview:interview_list') #추후 mainpage로 수정
    else:  
        form = IntervieweeForm()
        ctx = {'form': form}
        return render(request, 'interview/intervieweeform.html', ctx)
