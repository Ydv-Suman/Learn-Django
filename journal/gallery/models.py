import uuid
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=100, blank=True)
    excerpt = models.CharField(max_length=1000, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_slug = models.SlugField(max_length=100, blank=True, default="", null=False)

    class Meta:
        ordering = ["-updated_at"]
 
    def save(self, *args, **kwargs):
        if not self.image_slug or not self.image_slug.strip():
            self.image_slug = (slugify(self.caption) if self.caption else "") or str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)
