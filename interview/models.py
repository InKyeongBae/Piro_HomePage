from django.db import models

class Asking(models.Model) : 
    generation = models.IntegerField(default=0, null=True, blank=True, verbose_name="기수")
    question1 = models.CharField(max_length=155, null=True, blank=True, verbose_name="질문1")
    question2 = models.CharField(max_length=155, null=True, blank=True, verbose_name="질문2")
    question3 = models.CharField(max_length=155, null=True, blank=True, verbose_name="질문3")
    question4 = models.CharField(max_length=155, null=True, blank=True, verbose_name="질문4")

    def __str__(self):
        return '{}기 질문'.format(self.generation)


class Interviewee(models.Model) :
    MAJOR_CHOICES = {
        ('전공자','전공자'),
        ('비전공자','비전공자'),
        ('복수전공자','복수전공자')
    }

    generation = models.IntegerField(default=0, null=True, blank=True, verbose_name="기수")
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="이름")
    major = models.CharField(max_length=50, choices=MAJOR_CHOICES, blank=True, null=True, verbose_name="전공여부")
    intro = models.TextField(null=True, blank=True, verbose_name="썸네일용 간단한 소개")
    image = models.ImageField(null=True, blank=True, upload_to="interview", verbose_name="썸네일용 사진")

    
    class Meta:
        abstract = True

    def __str__(self):
        return '{}기 {}'.format(self.generation, self.name)


class Answer(Interviewee) :
    asking = models.ForeignKey(Asking, on_delete=models.CASCADE, related_name="asking")
    answer1 = models.TextField(null=True, blank=True, verbose_name="답변(내용) 1")
    answer2 = models.TextField(null=True, blank=True, verbose_name="답변(내용) 2")
    answer3 = models.TextField(null=True, blank=True, verbose_name="답변(내용) 3")
    answer4 = models.TextField(null=True, blank=True, verbose_name="답변(내용) 4")

    class Meta : 
        ordering = ['-generation']
    
    



    


