from django.test import TestCase, Client
from home import views
from django.urls import reverse
from .models import course, mark, student_detail, course_key, admin_key, grade, admin_detail, student_password



class CourseViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.sample_course = course.objects.create(
            username="teacher1",
            password="password123",
            course1="CS101",
            credits=3,
            year="1",
            branch="CS",
            name="Computer Science",
            teacher="Dr. Smith"
        )

    def test_add_delete_course_view(self):
        """Test add/delete course page loads successfully."""
        response = self.client.get(reverse('add_delete_course'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adddel_cou.html')
    
    def test_delete_course_view(self):
        """Test deleting a course."""
        response = self.client.post(reverse('delete_course'), {'course1': 'CS101'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('add_delete_course'))
