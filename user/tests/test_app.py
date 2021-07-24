"""Test user app"""
from django.apps import apps
from django.test import TestCase

from user.apps import UserConfig


class UserConfigTest(TestCase):
    """Testing User app"""

    def test_app_user(self):
        """"Test user app name"""

        self.assertEqual(
            UserConfig.name,
            "user"
        )
        self.assertEqual(
            apps.get_app_config('user').name,
            "user"
        )