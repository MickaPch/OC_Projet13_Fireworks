"""Test user views"""
from django.test import TestCase


class UserViewTest(TestCase):
    """Testing user view"""

    def test_user_view(self):
        """Test user view"""

        self.client.get('/user/')
        self.assertTemplateUsed('user.html')
    
