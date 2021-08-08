import os
import json
import random
import lorem
import datetime

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to create event fixture for tests"""

    def handle(self, *args, **kwargs):
        """Create event fixture"""

        commands = [
            "create_fixture_test_users",
            "create_fixture_test_contacts",
            "create_fixture_test_appliances",
            "create_fixture_test_events"
        ]

        for command in commands:
            call_command(command)
