from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Season) 
class CustomSeasonAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Image)
class CustomImageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Applicant)
class CustomImageAdmin(admin.ModelAdmin):
    pass

