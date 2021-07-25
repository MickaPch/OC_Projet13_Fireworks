"""Test dashboard app"""
from django.apps import apps
from django.test import TestCase

from dashboard.apps import DashboardConfig


class DashboardConfigTest(TestCase):
    """Testing Dashboard app"""

    def test_app_dashboard(self):
        """"Test dashboard app name"""

        self.assertEqual(
            DashboardConfig.name,
            "dashboard"
        )
        self.assertEqual(
            apps.get_app_config('dashboard').name,
            "dashboard"
        )