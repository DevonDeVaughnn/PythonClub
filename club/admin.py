from django.contrib import admin
from .models import Event, Meeting, MeetingMinutes, Resource

# Register your models here.
admin.site.register(Event)
admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(Resource)
