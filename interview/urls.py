from django.urls import path, include
from .views import *
app_name = 'interview'

urlpatterns = [
    path('interviewee/create/', interviewee_create, name="devtool_create" ),
    path('', interview_list, name="interview_list"),
]