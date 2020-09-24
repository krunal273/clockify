from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=50)
    startTime = models.DateTimeField(default=datetime.now())
    endTime = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    totalTime = models.IntegerField(default=0)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
