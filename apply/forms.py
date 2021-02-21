from django import forms
from apply.models import *

class ApplyForm(forms.ModelForm):

    GRADE = (
        ("1학년", "1학년"),
        ("2학년", "2학년"),
        ("3학년", "3학년"),
        ("4학년", "4학년"),
        ("5학년 이상", "5학년 이상"),
        ("졸업생", "졸업생"),
        ("대학원생", "대학원생"),
    )

    SEMESTER = (
        (1, "1학기"),
        (2, "2학기"),
        (3, "3학기"),
        (4, "4학기"),
        (5, "5학기"),
        (6, "6학기"),
    )

    YES_NO = (
        ("예", "예"),
        ("아니오", "아니오"),
    )

    AGREE_NOR = (
        ("동의", "동의"),
        ("비동의", "비동의"),
    )

    KNOW_ROOT = (
        ("sns", "피로그래밍 공식 SNS(예 - 페이스북, 인스타그램)"),
        ("cafe community", "네이버 카페/동아리 관련 커뮤니티(예 - 스펙업, 링커리어, 캠퍼스픽)"),
        ("everytime", "에브리타임"),
        ("friends", "지인의 소개"),
        ("others", "기타"),
    )
    participate_check = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect)
    workshop_check = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect)
    info_check = forms.ChoiceField(choices=AGREE_NOR, widget=forms.RadioSelect)
    know_check = forms.ChoiceField(choices=KNOW_ROOT, widget=forms.RadioSelect)
    deposit_check = forms.ChoiceField(choices=AGREE_NOR, widget=forms.RadioSelect)
    sub_major_semester = forms.ChoiceField(choices=SEMESTER, required=False, widget=forms.RadioSelect)
    major_grade = forms.ChoiceField(choices=GRADE, widget=forms.RadioSelect)
    sub_major = forms.CharField(required=False)
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
        # labels = {
        #     "participate_check":"일정 참여 여부", 
        # "workshop_check":"워크샵 참여 여부", 
        # "info_check" : "개인정보 이용동의", 
        # "deposit_check" : "보증금 납부 동의", 
        # "name" : "이름", 
        # "school" : "학교", 
        # "major" : "전공 학과", 
        # "major_grade" : "학년", 
        # "sub_major" : "부전공", 
        # "sub_major_semester" : "부전공 이수 학기",
        # "address" : "거주지",
        # "phone_number" : "휴대폰 번호",
        # "avail_meeting_time" : "면접 가능 시간대",
        # "answer1":"",
        # "answer2":"",
        # "answer3":"",
        # "answer4":"",
        # "answer5":"",
        # "code":"코드 입력란",
        # "know_check":"피로그래밍 알게 된 경로",
        # }
        # widgets={
        #     # 'participate_check':forms.RadioSelect,
        #     #'workshop_check':forms.RadioSelect,
        #     #'info_check':forms.RadioSelect,
        #     'major_grade':forms.RadioSelect,
        #     'sub_major_semester':forms.RadioSelect,
        #     'know_check':forms.RadioSelect,
        # }

    def clean_sub_major(self):
        sub_major = self.cleaned_data.get('sub_major')
        print(sub_major)
        if sub_major == '':
            print("claen 확인!")
            return ''
        else :
            print("raw 확인!")
            return sub_major
    
    def clean_sub_major_semester(self):
        semester = self.cleaned_data.get('sub_major_semester')
        print(semester)
        if semester == '':
            print("claen 확인!")
            return 0
        else :
            print("raw 확인!")
            return semester

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

