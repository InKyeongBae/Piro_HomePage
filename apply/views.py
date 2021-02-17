from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Season, Image, Applicant
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .forms import ApplyForm

def main(request):

    try:
        season = Season.objects.order_by('-created_at').first()
    except ObjectDoesNotExist:
        msg = "모집 중인 기수가 없습니다"
        return redirect(reverse('interview:interview_list'))
    
    number = season.season_num
    img = season.poster
    now = timezone.now()
    print(now)
    if now<=season.doc_screening_end and now>=season.doc_screening_start:
        status = "doc"
        notify_date = None
    elif now<season.doc_result_start and now>season.doc_screening_end:
        status = "doc_result_waiting"
        notify_date = season.doc_result_start
    elif now>=season.doc_result_start and now<=season.doc_result_end:
        status = "doc_result"
        notify_date = None
    elif now>season.doc_result_end and now<season.final_result_open:
        status = "final_result_waiting"
        notify_date = season.final_result_open
    elif now>=season.final_result_open and now<=season.final_result_close:
        status = "final"
        notify_date = None
    else:
        msg = "지원 기간이 아닙니다!"
        return redirect(reverse('interview:interview_list'))

    print(img)

    ctx = {
        'number' : number,
        'img' : img,
        'status' : status,
        'notify_date' : notify_date,
    }
    return render(request, 'apply/apply_main.html', ctx)
    
def apply(request):
    try:
        season = Season.objects.order_by('-created_at').first()
    except ObjectDoesNotExist:
        msg = "모집 중인 기수가 없습니다"
        return redirect(reverse('interview:interview_list'))
    print("왔다")
    now = timezone.now()
    if now<=season.doc_screening_end and now>=season.doc_screening_start:
        print("여기도")
        if request.method == 'POST':
            form = ApplyForm(request.POST)

        else:
            form = ApplyForm()
            ctx ={
                'form':form,
            }
            return render(request, 'apply/application.html', ctx)
    else:
        msg = "지금은 지원 기간이 아닙니다!"
        return redirect(reverse('interview:interview_list'))