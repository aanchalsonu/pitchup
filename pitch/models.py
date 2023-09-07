from django.db import models
from django.contrib.auth.models import User

class Pitch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pitch_title = models.CharField(max_length=100)
    pitch_description = models.TextField()
    pitch_category = models.CharField(max_length=50)
    pitch_images = models.ImageField(upload_to='pitch_images/', blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pitch_title

class Image(models.Model):
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pitch_images/')

    def __str__(self):
        return f"Image for Pitch: {self.pitch.title}"
