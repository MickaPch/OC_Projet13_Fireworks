import os
import json

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to create contact fixture for tests"""

    def handle(self, *args, **kwargs):
        """Create contact fixture"""

        contacts = [
            {
                "model": "contacts.Company",
                "pk": 1,
                "fields": {
                    "name": "Company1",
                    "address1": "address1",
                    "address2": "content1",
                    "zipcode": "01234",
                    "city": "CITY1",
                    "user": [1],
                }
            }, {
                "model": "contacts.Company",
                "pk": 2,
                "fields": {
                    "name": "Company2",
                    "address1": "address2",
                    "address2": "content2",
                    "zipcode": "21025",
                    "city": "CITY2",
                    "user": [2],
                }
            }, {
                "model": "contacts.Company",
                "pk": 3,
                "fields": {
                    "name": "Company3",
                    "address1": "address3",
                    "address2": "content3",
                    "zipcode": "14485",
                    "city": "CITY3",
                    "user": [3],
                }
            }, {
                "model": "contacts.Company",
                "pk": 4,
                "fields": {
                    "name": "Company4",
                    "address1": "address4",
                    "address2": "content4",
                    "zipcode": "45525",
                    "city": "CITY4",
                    "user": [1, 2],
                }
            }, {
                "model": "contacts.Company",
                "pk": 5,
                "fields": {
                    "name": "Company5",
                    "address1": "address5",
                    "address2": "content5",
                    "zipcode": "01234",
                    "city": "CITY1",
                    "user": [1, 2, 3],
                }
            }, {
                "model": "contacts.Contact",
                "pk": 1,
                "fields": {
                    "first_name": "Alain",
                    "last_name": "THOMAS",
                    "company": 1,
                    "user": [1]
                }
            }, {
                "model": "contacts.Contact",
                "pk": 2,
                "fields": {
                    "first_name": "Thibault",
                    "last_name": "ASTIER",
                    "company": 2,
                    "phone_number": "0612345679",
                    "user": [2]
                }
            }, {
                "model": "contacts.Contact",
                "pk": 3,
                "fields": {
                    "first_name": "Giselle",
                    "last_name": "COHEN",
                    "company": 3,
                    "email": "giselle@example.com",
                    "user": [3]
                }
            }, {
                "model": "contacts.Contact",
                "pk": 4,
                "fields": {
                    "first_name": "Edouard",
                    "last_name": "MARTY",
                    "company": 5,
                    "phone_number": "0612345678",
                    "email": "edouard@example.com",
                    "user": [1, 3]
                }
            }, {
                "model": "contacts.Contact",
                "pk": 5,
                "fields": {
                    "first_name": "Sébastien",
                    "last_name": "BRIS",
                    "company": 4,
                    "user": [1, 2]
                }
            }, {
                "model": "contacts.Contact",
                "pk": 6,
                "fields": {
                    "first_name": "Laura",
                    "last_name": "GRASSINEAU",
                    "company": 5,
                    "user": [1, 2, 3]
                }
            }, {
                "model": "contacts.Mission",
                "pk": 1,
                "fields": {
                    "title": "Mission test 1",
                    "description": "Description 1",
                    "company": 1,
                    "user": 1,
                }
            }, {
                "model": "contacts.Mission",
                "pk": 2,
                "fields": {
                    "title": "Mission test 2",
                    "description": "Description 2",
                    "company": 2,
                    "user": 1,
                }
            }, {
                "model": "contacts.Mission",
                "pk": 3,
                "fields": {
                    "title": "Mission test 3",
                    "description": "Description 3",
                    "company": 1,
                    "user": 2,
                }
            }, {
                "model": "contacts.Mission",
                "pk": 4,
                "fields": {
                    "title": "Mission test 4",
                    "description": "Description 4",
                    "company": 3,
                    "user": 1,
                }
            }, {
                "model": "contacts.Mission",
                "pk": 5,
                "fields": {
                    "title": "Mission test 5",
                    "description": "Description 5",
                    "company": 3,
                    "user": 3,
                }
            }, {
                "model": "contacts.Mission",
                "pk": 6,
                "fields": {
                    "title": "Mission test 6",
                    "description": "Description 6",
                    "company": 2,
                    "user": 2,
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
            'contacts.json'
        )

        with open(path_file, 'w') as file_contact:
            file_contact.write(json.dumps(contacts))
