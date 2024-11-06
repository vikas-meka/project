from django.test import TestCase, Client
from home import views
from django.urls import reverse
from .models import course, mark, student_detail, course_key, admin_key, grade, admin_detail, student_password

class CourseKeyModelTests(TestCase):
    """ Test cases for course_key model """

    def setUp(self):
        self.course_key = course_key.objects.create(key='key1', course='CS101', name='Data Structures')

    def test_course_key_creation(self):
        """ Test Case 6.1: Verify course key creation """
        self.assertEqual(course_key.objects.count(), 1)
        self.assertEqual(self.course_key.course, 'CS101')
    

    def test_update_entered_marks(self):
        """ Test Case 6.3: Update entered_marks """
        self.course_key.entered_marks = '60'
        self.course_key.save()
        self.assertEqual(self.course_key.entered_marks, '60')


