"""Test accounts app"""
from django.apps import apps
from django.test import TestCase

from contacts.apps import ContactsConfig


class ContactsConfigTest(TestCase):
    """Testing Contacts app"""

    def test_app_accounts(self):
        """"Test contacts app name"""

        self.assertEqual(
            ContactsConfig.name,
            "contacts"
        )
        self.assertEqual(
            apps.get_app_config('contacts').name,
            "contacts"
        )