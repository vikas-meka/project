from django.test import TestCase, Client
from home import views
from django.urls import reverse
from .models import course, mark, student_detail, course_key, admin_key, grade, admin_detail, student_password

class CourseModelTests(TestCase):
    """ Test cases related to the course model """

    def setUp(self):
        # Setting up a course instance for testing
        self.course = course.objects.create(
            username='course_user1', password='password123', course1='CS101',
            credits=3, year='2', branch='CSE', name='Data Structures', teacher='Prof. Smith'
        )

    def test_course_creation(self):
        """ Test Case 1.1: Verify course creation """
        self.assertEqual(course.objects.count(), 1)
        self.assertEqual(self.course.course1, 'CS101')
    
    def test_course_primary_key_uniqueness(self):
        """ Test Case 1.2: Ensure unique primary key for course """
        with self.assertRaises(Exception):
            course.objects.create(course1='CS101')  # Duplicate primary key
    
    def test_course_string_representation(self):
        """ Test Case 1.3: Verify __str__ representation """
        self.assertEqual(str(self.course), 'course_user1')

    def test_course_with_null_optional_fields(self):
        """ Test Case 1.4: Create a course with null optional fields """
        course_with_nulls = course.objects.create(
            username='course_user2', course1='CS102', credits=None, year=None, branch=None
        )
        self.assertIsNone(course_with_nulls.credits)
