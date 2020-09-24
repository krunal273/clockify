from django.db import models
from django.utils import timezone

# Create your models here.


class Tracker(models.Model):
    title = models.CharField(max_length=50)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
