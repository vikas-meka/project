from django.test import TestCase, Client
from home import views
from django.urls import reverse
from .models import course, mark, student_detail, course_key, admin_key, grade, admin_detail, student_password

class StudentPasswordModelTests(TestCase):
    """ Test cases for student_password model """

    def setUp(self):
        self.student_password = student_password.objects.create(username='student1', password='pass1')

    def test_student_password_creation(self):
        """ Test Case 8.1: Verify creation of student_password entry """
        self.assertEqual(student_password.objects.count(), 1)
    
    def test_student_password_retrieval(self):
        """ Test Case 8.3: Retrieve password entry """
        entry = student_password.objects.get(username='student1')
        self.assertEqual(entry.password, 'pass1')

