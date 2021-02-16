from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Season) #데코레이터가 바로 위에 위치해야 작동한다!
class CustomSeasonAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Image)
class CustomImageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Applicant)
class CustomImageAdmin(admin.ModelAdmin):
    pass

