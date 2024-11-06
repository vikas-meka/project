from django.test import TestCase, Client
from home import views
from django.urls import reverse
from .models import course, mark, student_detail, course_key, admin_key, grade, admin_detail, student_password

class AdminKeyModelTests(TestCase):
    """ Test cases for admin_key model """

    def setUp(self):
        self.admin_key = admin_key.objects.create(key='admin_key1', name='Admin 1')

    def test_admin_key_creation(self):
        """ Test Case 7.1: Verify admin key creation """
        self.assertEqual(admin_key.objects.count(), 1)
        self.assertEqual(self.admin_key.key, 'admin_key1')
    
    def test_admin_key_fields(self):
        """ Test Case 7.2: Check optional fields """
        self.assertIsNone(self.admin_key.entered_courses)
