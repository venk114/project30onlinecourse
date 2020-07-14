from django.db import models
import datetime

class ScheduleNewClass(models.Model):
    Name = models.CharField(unique=True,max_length=50)
    Faculty = models.CharField(max_length=50)
    Date = models.DateField(default=datetime.date(2020,1,1))
    Time = models.TimeField(default=datetime.time(2,30,5))
    Fee =  models.FloatField()
    Duration = models.IntegerField()
