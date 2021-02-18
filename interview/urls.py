from django.urls import path, include
from .views import *
app_name = 'interview'

urlpatterns = [
    path('non_major/', non_major_interview, name="non_major_interview"),
    path('major/', major_interview, name="major_interview"),
    path('double_major/', double_major_interview, name="double_major_interview"),
    path('view/<int:pk>/',interview_view, name="interview_view")
]