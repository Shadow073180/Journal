from django.db import models
from datetime import datetime


# Create your models here.

class Journal(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    
    

    def __str__(self):
        return self.name

class Entry(models.Model):
    entry_text = models.TextField()
    date_time = models.DateTimeField(default=datetime.now)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='entries', null=True)
