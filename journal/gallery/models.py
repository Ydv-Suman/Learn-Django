from email.policy import default
from django.db import models

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
