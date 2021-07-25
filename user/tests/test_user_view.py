"""Test user views"""
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.test import TestCase

class UserViewTest(TestCase):
    """Testing user view"""

    def test_user_template_used(self):
        """Test user view"""

        self.client.get('/user/home/')

        self.assertTemplateUsed('user.html')

    def test_user_html_status(self):
        """Test user view"""

        response = self.client.get('/user/home/')

        self.assertEqual(response.status_code, 200)
    
    def test_user_page_shows_User_home(self):

        response = self.client.get('/user/home/')

        self.assertIn(
            b'User home',
            response.content
        )

    def test_user_form_is_present(self):

        response = self.client.get('/user/login/')

        self.assertIn(
            b'<input',
            response.content
        )

    def test_user_can_login(self):

        response = self.client.get('/user/login/')
        user = User.objects.create_user(
            'test',
            'test@mailtest.com',
            'testpassword'
        )
        self.assertFalse(SESSION_KEY in self.client.session)

        self.client.login(
            username='test',
            password='testpassword'
        )
        self.assertTrue(SESSION_KEY in self.client.session)
