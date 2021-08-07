"""Test myjob_calendar app"""
from django.apps import apps
from django.test import TestCase

from myjob_calendar.apps import MyjobCalendarConfig


class MyjobCalendarConfigTest(TestCase):
    """Testing myjob_calendar app"""

    def test_app_myjob_calendar(self):
        """"Test myjob_calendar app name"""

        self.assertEqual(
            MyjobCalendarConfig.name,
            "myjob_calendar"
        )
        self.assertEqual(
            apps.get_app_config('myjob_calendar').name,
            "myjob_calendar"
        )