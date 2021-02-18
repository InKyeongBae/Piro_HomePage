from django.db import models

class Asking(models.Model) : 
    generation = models.IntegerField(default=0, verbose_name="기수")
    question = models.TextField(null=True, blank=True)

class Answer(models.Model) :
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="이름")
    asking = models.ForeignKey(Asking, on_delete=models.CASCADE, null=True, related_name="answer",  verbose_name="질문")
    answer = models.TextField(null=True, blank=True)

class Interviewee(models.Model) :
    MAJOR_CHOICES = {
        ('major','전공자'),
        ('non_major','비전공자'),
        ('double_major','복수전공자')
    }

    generation = models.IntegerField(default=0,verbose_name="기수")
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="이름")
    major = models.CharField(max_length=50, choices=MAJOR_CHOICES, blank=True, null=True, verbose_name="전공여부")
    intro = models.TextField(null=True, blank=True, verbose_name="썸네일용 간단한 소개")
    image = models.ImageField(null=True, blank=True, upload_to="interview", verbose_name="썸네일용 사진")

    def __str__(self):
        return '{}기 {}'.format(self.generation, self.name)


