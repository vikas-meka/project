from django.test import TestCase, Client
from home import views
from django.urls import reverse
from .models import course, mark, student_detail, course_key, admin_key, grade, admin_detail, student_password

class MarkModelTests(TestCase):
    """ Test cases for mark model """

    def setUp(self):
        self.mark_entry = mark.objects.create(
            roll_no='ST001', course='CS101', ct1=20, ct2=25, end=50, internals=10, total=105, grade=4, score='A'
        )

    def test_mark_entry_creation(self):
        """ Test Case 3.1: Verify mark entry creation """
        self.assertEqual(mark.objects.count(), 1)
        self.assertEqual(self.mark_entry.course, 'CS101')
    
    def test_total_marks(self):
        """ Test Case 3.2: Verify total marks calculation """
        self.assertEqual(self.mark_entry.total, 105)
    
    def test_null_fields_in_mark_entry(self):
        """ Test Case 3.3: Allow null values for optional fields """
        mark_with_nulls = mark.objects.create(roll_no='ST002', course='CS102', total=70, grade=None)
        self.assertIsNone(mark_with_nulls.grade)

    def test_invalid_grade_type(self):
        """ Test Case 3.4: Grade must be an integer """
        with self.assertRaises(Exception):
            mark.objects.create(roll_no='ST003', course='CS103', grade='invalid')

