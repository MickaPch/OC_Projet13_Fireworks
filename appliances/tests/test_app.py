"""Test appliances app"""
from django.apps import apps
from django.test import TestCase

from appliances.apps import AppliancesConfig


class AppliancesConfigTest(TestCase):
    """Testing Appliances app"""

    def test_app_appliances(self):
        """"Test appliances app name"""

        self.assertEqual(
            AppliancesConfig.name,
            "appliances"
        )
        self.assertEqual(
            apps.get_app_config('appliances').name,
            "appliances"
        )