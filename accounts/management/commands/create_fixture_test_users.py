import os
import json

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    """Command to create user fixture for tests"""

    def handle(self, *args, **kwargs):
        """Create user fixture"""

        users = [
            {
                "model": "auth.User",
                "pk": 1,
                "fields": {
                    "username": "User1",
                    "password": make_password('pwd$User1'),
                    "is_superuser": False,
                    "is_staff": False,
                    "is_active": True,
                    "email": "user1@foo.com"
                }
            }, {
                "model": "auth.User",
                "pk": 2,
                "fields": {
                    "username": "User2",
                    "password": make_password('pwd$User2'),
                    "is_superuser": False,
                    "is_staff": False,
                    "is_active": True,
                    "email": "user2@foo.com"
                }
            }, {
                "model": "auth.User",
                "pk": 3,
                "fields": {
                    "username": "User3",
                    "password": make_password('pwd$User3'),
                    "is_superuser": False,
                    "is_staff": False,
                    "is_active": True,
                    "email": "user3@foo.com"
                }
            },
        ]

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)
                )
            ),
            'fixtures',
            'users.json'
        )

        with open(path_file, 'w') as file_user:
            file_user.write(json.dumps(users))
