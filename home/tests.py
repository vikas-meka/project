from django.test import TestCase, Client
from home import views
from django.urls import reverse
from .models import course, mark, student_detail, course_key, admin_key, grade, admin_detail, student_password

class StudentDetailModelTests(TestCase):
    """ Test cases for student_detail model """

    def setUp(self):
        self.student = student_detail.objects.create(
            roll_no='ST001', name='John Doe', year='3', branch='ECE', password='mypassword'
        )

    def test_student_creation(self):
        """ Test Case 2.1: Verify student creation """
        self.assertEqual(student_detail.objects.count(), 1)
        self.assertEqual(self.student.roll_no, 'ST001')

    def test_duplicate_roll_no(self):
        """ Test Case 2.2: Ensure unique roll_no """
        with self.assertRaises(Exception):
            student_detail.objects.create(roll_no='ST001')  # Duplicate roll number
    
    def test_student_string_representation(self):
        """ Test Case 2.3: Verify __str__ method """
        self.assertEqual(str(self.student), 'ST001')
    
