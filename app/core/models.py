from typing import Any
from django.db import models
from django.core.validators import FileExtensionValidator

class PlayList(models.Model):
    name = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        pass    

    def __str__(self):
        return f"{self.name} - {self.pk}"

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='uploads/video_files', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    playlist = models.ForeignKey(PlayList, on_delete=models.SET_NULL, related_name='videos', null=True, blank=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.video_file.delete()
        super().delete(*args, **kwargs)
