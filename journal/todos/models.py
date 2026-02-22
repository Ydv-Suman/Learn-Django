from django.db import models
from django.utils.text import slugify

# Create your models here.


class Todos(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    todo_slug = models.SlugField(max_length=100, blank=True, default="", null=False)

    def save(self, *args, **kwargs):
        if self.title and not self.todo_slug:
            self.todo_slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title} {self.due_date} {self.is_complete}"