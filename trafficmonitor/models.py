
# Create your models here.

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

    