"""Test accounts views"""
from django.contrib.auth import SESSION_KEY
from django.http import response
from django.test import TestCase
from django.urls import reverse

from accounts.models import User

class AccountsViewTest(TestCase):
    """Testing accounts view"""

    fixtures = ['users.json']

    def test_user_template_used(self):
        """Test accounts view"""

        self.client.get(reverse("accounts_home_page"))

        self.assertTemplateUsed('accounts/accounts.html')

    def test_user_html_status(self):
        """Test accounts view"""

        response = self.client.get(reverse("accounts_home_page"))

        self.assertEqual(response.status_code, 200)

    def test_user_page_shows_User_home(self):

        response = self.client.get(reverse("accounts_home_page"))

        self.assertIn(
            b'>Log',
            response.content
        )

    def test_user_form_exists(self):

        response = self.client.get(reverse('login'))

        self.assertIn(
            b'<input',
            response.content
        )

    def test_user_can_login(self):

        response = self.client.get(reverse("accounts_home_page"))
        self.assertFalse(SESSION_KEY in self.client.session)
        self.assertIn(b'>Log In</a>', response.content)

    def test_user_can_logout(self):

        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse("accounts_home_page"))

        self.assertTrue(SESSION_KEY in self.client.session)
        self.assertIn(b'>Log Out</a>', response.content)

    def test_login_user(self):

        self.client.get(reverse('login'))
        self.assertFalse(SESSION_KEY in self.client.session)

        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        self.assertTrue(SESSION_KEY in self.client.session)

    def test_user_loginpage_from_base(self):

        response = self.client.get(reverse('login'))

        self.assertIn(
            b'<title>MyJOB - Log In',
            response.content
        )

    def test_form_login_redirects_user(self):

        response = self.client.post(
            reverse('login'),
            data={
                "username": "User1",
                "password": "pwd$User1"
            }
        )
        self.assertRedirects(response, reverse("accounts_profile_page"))
        self.assertTrue(SESSION_KEY in self.client.session)
