from django import forms
from apply.models import *

class ApplyForm(forms.ModelForm):
    
    class Meta:
        model = Applicant
        fields = ("participate_check", 
        "workshop_check", 
        "info_check", 
        "deposit_check", 
        "name", 
        "school", 
        "major", 
        "major_grade", 
        "sub_major", 
        "sub_major_semester",
        "address",
        "phone_number",
        "avail_meeting_time",
        "answer1",
        "answer2",
        "answer3",
        "answer4",
        "answer5",
        "code",
        "know_check")
        labels = {
            "participate_check":"일정 참여 여부", 
        "workshop_check":"워크샵 참여 여부", 
        "info_check" : "개인정보 이용동의", 
        "deposit_check" : "보증금 납부 동의", 
        "name" : "이름", 
        "school" : "학교", 
        "major" : "전공 학과", 
        "major_grade" : "학년", 
        "sub_major" : "부전공", 
        "sub_major_semester" : "부전공 이수 학기",
        "address" : "거주지",
        "phone_number" : "휴대폰 번호",
        "avail_meeting_time" : "면접 가능 시간대",
        "answer1":"",
        "answer2":"",
        "answer3":"",
        "answer4":"",
        "answer5":"",
        "code":"코드 입력란",
        "know_check":"피로그래밍 알게 된 경로",
        }

class ApplyConfirm(forms.Form):
    name = forms.CharField(max_length=15, label="이름")
    phone_number = forms.CharField(max_length=15, label="전화번호")

    def clean_phone_number(self):
        pn = self.cleaned_data.get('phone_number')
        tmplist = list(pn)
        print(tmplist)
        for i in tmplist:
            if i<'0' or i>'9':
                tmplist.remove(i)
        print(tmplist)
        pn = ''.join(tmplist)
        return pn

