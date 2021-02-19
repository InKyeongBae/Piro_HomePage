from django.urls import path, include
from .views import *

app_name = 'gallery'

urlpatterns = [
    path('', gallery_view, name="gallery_view"),
    
]