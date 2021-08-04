import os
import json

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to create appliance fixture for tests"""

    def handle(self, *args, **kwargs):
        """Create appliance fixture"""

        appliances = [
            {
                "model": "appliances.Appliance",
                "pk": 1,
                "fields": {
                    "company": 1,
                    "user": 1,
                    "estimated_salary": 35.0,
                    "proposed_salary": 33.5,
                    "environment_notation": 4,
                    "environment_details": "Lorem ipsum dolor sit amet",
                    "values_notation": 3,
                    "values_details": "",
                    "evolution_notation": 3,
                    "evolution_details": "Lorem ipsum",
                    "knowledge_notation": 4,
                    "knowledge_details": "Lorem ipsum dolor sit amet",
                    "management_notation": 3,
                    "management_details": "Lorem ipsum dolor sit amet",
                    "advantages_notation": 4,
                    "advantages_details": "Lorem",
                    "notoriety_notation": 1,
                    "notoriety_details": "Lorem ipsum dolor",
                    "office_notation": None,
                    "office_details": "",
                }
            }
        ]

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)
                )
            ),
            'fixtures',
            'appliances.json'
        )

        with open(path_file, 'w') as file_contact:
            file_contact.write(json.dumps(appliances))
