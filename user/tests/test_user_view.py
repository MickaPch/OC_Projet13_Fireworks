"""Test user views"""
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
    
    def test_user_page_shows_LogIn(self):

        response = self.client.get('/user/home/')

        self.assertIn(
            b'Log In',
            response.content
        )

    def test_user_form_is_present(self):

        response = self.client.get('/user/login/')

        self.assertIn(
            b'<input',
            response.content
        )

