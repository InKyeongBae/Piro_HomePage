from django.db import models

# Create your models here.
class Photo(models.Model) :
    
    generation = models.IntegerField(default=0, null=True, blank=True, verbose_name="기수")
    image = models.ImageField(null=True, blank=True, upload_to="gallery", verbose_name="사진")
    description = models.TextField(null=True, blank=True, verbose_name="설명")

    def __str__(self):
        return '{}.{}'.format(self.pk, self.description)

    class Meta : 
        ordering = ['-generation']