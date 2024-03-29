"""Test accounts views"""
from django.contrib.auth import SESSION_KEY
from django.http import response
from django.test import TestCase
from django.urls import reverse

from accounts.models import User

class DashboardViewTest(TestCase):
    """Testing dashboard view"""

    def setUp(self):

        self.user = User.objects.create_user(
            'test',
            'test@mailtest.com',
            'testpassword'
        )

    def test_home_template_used(self):
        """Test accounts view"""

        self.client.get(reverse('home'))

        self.assertTemplateUsed('home.html')

    def test_home_html_status(self):
        """Test accounts view"""

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)

    def test_home_user_can_login(self):
        """Test accounts view"""

        response = self.client.get(reverse('home'))

        self.assertFalse(SESSION_KEY in self.client.session)
        self.assertIn(b'>Log In', response.content)



    # def test_user_html_status(self):
    #     """Test accounts view"""

    #     response = self.client.get('/accounts/home/')

    #     self.assertEqual(response.status_code, 200)

    # def test_user_page_shows_User_home(self):

    #     response = self.client.get('/accounts/home/')

    #     self.assertIn(
    #         b'<title>MyJOB - Home',
    #         response.content
    #     )

    # def test_user_form_exists(self):

    #     response = self.client.get('/accounts/login/')

    #     self.assertIn(
    #         b'<input',
    #         response.content
    #     )

    # def test_user_can_login(self):

    #     response = self.client.get('/accounts/home/')
    #     self.assertFalse(SESSION_KEY in self.client.session)
    #     self.assertIn(b'>Log In</a>', response.content)

    # def test_user_can_logout(self):

    #     self.client.login(
    #         username='test',
    #         password='testpassword'
    #     )
    #     response = self.client.get('/accounts/home/')

    #     self.assertTrue(SESSION_KEY in self.client.session)
    #     self.assertIn(b'>Log Out</a>', response.content)

    # def test_login_user(self):

    #     self.client.get('/accounts/login/')
    #     self.assertFalse(SESSION_KEY in self.client.session)

    #     self.client.login(
    #         username='test',
    #         password='testpassword'
    #     )
    #     self.assertTrue(SESSION_KEY in self.client.session)

    # def test_user_loginpage_from_base(self):

    #     response = self.client.get('/accounts/login/')

    #     self.assertIn(
    #         b'<title>MyJOB - Log In',
    #         response.content
    #     )

    # def test_form_login_redirects_user(self):

    #     response = self.client.post(
    #         "/accounts/login/",
    #         data={
    #             "username": "test",
    #             "password": "testpassword"
    #         }
    #     )
    #     self.assertRedirects(response, "/accounts/profile/")
