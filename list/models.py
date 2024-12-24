from django.db import models

class Tasks(models.Model):
    task=models.TextField(max_length=100)
    last_date=models.DateField()
    dead_line=models.TimeField()
# Create your models here.
