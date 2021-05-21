from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    Agenda = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "meeting"


class MeetingMinutes(models.Model):
    title = models.CharField(max_length=255)
    meetingid = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutestext = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "meetingminutes"


class Resource(models.Model):
    name = models.CharField(max_length=255)
    resourcetype = models.CharField(max_length=255)
    resourceurl = models.URLField(null=True, blank=True)
    dateentered = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "resource"


class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "event"
