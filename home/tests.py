from django.test import TestCase, Client
from home import views
from django.urls import reverse
from .models import course, mark, student_detail, course_key, admin_key, grade, admin_detail, student_password



class StudentViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.sample_student = student_detail.objects.create(
            roll_no="R123",
            name="Alice",
            year="2",
            branch="CS",
            password="pass123"
        )

    def test_delete_student_view(self):
        """Test deleting a student successfully."""
        response = self.client.post(reverse('delete_student'), {'roll_no': 'R123'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('add_delete_student'))

    def test_add_delete_student_view(self):
        """Test add/delete student page loads successfully."""
        response = self.client.get(reverse('add_delete_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adddel_stu.html')