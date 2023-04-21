from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)