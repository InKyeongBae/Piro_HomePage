from django.db import models

# Create your models here.
class MainDescImg(models.Model):
    first_img = models.ImageField(null=True, blank=True, upload_to="main", verbose_name="메인 사진 1")
    second_img = models.ImageField(null=True, blank=True, upload_to="main", verbose_name="메인 사진 2")
    third_img = models.ImageField(null=True, blank=True, upload_to="main", verbose_name="메인 사진 3")

    def __str__(self):
        return 'Main Page Desc Images'

class MainInterview(models.Model):
    interview = models.ForeignKey('interview.Answer', on_delete=models.CASCADE, related_name="main_interviews")

    def __str__(self):
        return 'Main Page Interviews - {}'.format(self.interview)