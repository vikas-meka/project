from django.test import TestCase, Client
from home import views
from django.urls import reverse
from .models import course, mark, student_detail, course_key, admin_key, grade, admin_detail, student_password



class AuthenticationTests(TestCase):
    """ Test cases for admin and student authentication views """

    def setUp(self):
        self.admin = admin_detail.objects.create(username='vikas', password='vikas_meka')
        self.student_password = student_password.objects.create(username='211199', password='211199')
        self.student_detail = student_detail.objects.create(
            roll_no='211199', name='Test User', year='3', branch='CSE', password='211199')

    def test_admin_login(self):
        """ Test Case 4.1: Admin login with correct credentials """
        response = self.client.post(reverse('admin_login'), {'username': 'vikas', 'password': 'vikas_meka'})
        self.assertEqual(response.status_code, 200)
    
    def test_student_login(self):
        """ Test Case 4.2: Student login with correct credentials """
        response = self.client.post(reverse('student'), {'username': '211140', 'password': '211140'})
        self.assertEqual(response.status_code, 302)
    
    def test_invalid_login(self):
        """ Test Case 4.3: Invalid login credentials """
        response = self.client.post(('loginUser'), {'username': 'invalid', 'password': 'pass'})
        self.assertEqual(response.status_code, 404)
    
    def test_logout(self):
        """ Test Case 4.4: Ensure logout functionality """
        self.client.login(username='vikas', password='vikas_meka')
        response = self.client.get(reverse('admin_logout'))
        self.assertEqual(response.status_code, 302)

    def test_login_view_post_invalid(self):
        """Test login functionality with invalid credentials."""        
        response = self.client.post(reverse('admin_login'), {'username': 'vikas', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin_login'))
        follow_response = self.client.get(reverse('admin_login'))
        messages_list = list(follow_response.context['messages'])
        self.assertTrue(any("Incorrect credentials" in str(msg) for msg in messages_list))