from django.db import models

# Create your models here.

class DailyTrack(models.Model):
    date = models.DateField();
    title = models.CharField(max_length=100, null=False)
    descrpition = models.CharField(max_length=2000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'daily_track'
        ordering = ['-date']
        
    def __str__(self):
        return f"{self.title} {self.date}"