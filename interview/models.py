from django.db import models

class Asking(models.Model) : 
    generation = models.IntegerField(default=0)
    question = models.TextField(null=True, blank=True)

class Answer(models.Model) :
    generation = models.IntegerField(default=0)
    name = models.CharField(max_length=50, null=True, blank=True)
    asking = models.ForeignKey(Asking, on_delete=models.CASCADE, null=True, related_name="answer")
    answer = models.TextField(null=True, blank=True)

class Interviewee(models.Model) :
    MAJOR_CHOICES = {
        ('major','전공자'),
        ('non_major','비전공자'),
        ('double_major','복수전공자')
    }

    generation = models.IntegerField(default=0)
    name = models.CharField(max_length=50, null=True, blank=True)
    major = models.CharField(max_length=50, choices=MAJOR_CHOICES, blank=True, null=True, verbose_name='is_major')
    intro = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="interview")

    def __str__(self):
        return '{}기 {}'.format(self.generation, self.name)


