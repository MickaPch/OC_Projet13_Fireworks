"""Test accounts app"""
from django.apps import apps
from django.test import TestCase

from accounts.apps import AccountsConfig


class AccountsConfigTest(TestCase):
    """Testing Accounts app"""

    def test_app_accounts(self):
        """"Test accounts app name"""

        self.assertEqual(
            AccountsConfig.name,
            "accounts"
        )
        self.assertEqual(
            apps.get_app_config('accounts').name,
            "accounts"
        )