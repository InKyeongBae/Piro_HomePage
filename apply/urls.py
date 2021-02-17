from django.urls import path, include
from .views import *
app_name = 'apply'

urlpatterns = [
    path('main', main, name="main" ),
    path('application', apply, name="application")
]