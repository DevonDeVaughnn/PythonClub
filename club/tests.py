from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event


# Create your tests here.

class MeetingTest(TestCase):
    def setUp(self):
        self.type = Meeting(title="New Meeting")

    def test_typestring(self):
        self.assertEqual(str(self.type), "New Meeting")

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), "meeting")


class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type = MeetingMinutes(title="50 Minutes")

    def test_typestring(self):
        self.assertEqual(str(self.type), "50 Minutes")

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), "meetingminutes")


class ResourceTest(TestCase):
    def setUp(self):
        self.type = Resource(name="New Resource")

    def test_typestring(self):
        self.assertEqual(str(self.type), "New Resource")

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), "resource")


class EventTest(TestCase):
    def setUp(self):
        self.type = Event(title="New Event")

    def test_typestring(self):
        self.assertEqual(str(self.type), "New Event")

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), "event")
