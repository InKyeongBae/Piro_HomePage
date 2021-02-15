from django import forms
from interview.models import *

class AskingForm(forms.ModelForm):
    
    class Meta:
        model = Asking
        fields = ("generation", "question")
        labels = {
            'generation': '기수',
            'question' : '질문',
        }

class IntervieweeForm(forms.ModelForm):

    class Meta:
        model = Interviewee
        fields = ("generation", "name", "major", "image","intro")
        labels = {
            'generation': '기수',
            'name': '이름',
            'major': '전공자/비전공자/복수전공자',
            'intro': '한 줄 소개',
            'image': '사진',
        }
