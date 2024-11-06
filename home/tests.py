from django.test import TestCase, Client
from home import views
from django.urls import reverse
from .models import course, mark, student_detail, course_key, admin_key, grade, admin_detail, student_password

class GradeModelTests(TestCase):
    """ Test cases for grade model """

    def setUp(self):
        self.grade_entry = grade.objects.create(roll_no='ST001', cgpa='8.5')

    def test_grade_entry_creation(self):
        """ Test Case 5.1: Verify grade entry creation """
        self.assertEqual(grade.objects.count(), 1)
        self.assertEqual(self.grade_entry.cgpa, '8.5')
    
    def test_grade_string_representation(self):
        """ Test Case 5.3: Verify __str__ representation """
        self.assertEqual(str(self.grade_entry), 'ST001')


