import os
import json
import random

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    """Command to create user fixture for tests"""

    def handle(self, *args, **kwargs):
        """Create user fixture"""

        print('User fixture creation ...')

        users = []
        model = "auth.User"
        is_superuser = True
        is_staff = True
        for i in range(1, random.randint(4, 11)):
            if i > 1:
                is_superuser = False
            if i > 2:
                is_staff = False
            username = "User" + str(i)
            password = "pwd$" + username
            email = username.lower() + '@example.com'

            user = {
                "model": model,
                "pk": i,
                "fields": {
                    "username": username,
                    "password": make_password(password),
                    "is_superuser": is_superuser,
                    "is_staff": is_staff,
                    "is_active": True,
                    "email": email
                }
            }

            users.append(user)

        print('File creation ...')

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)
                )
            ),
            'fixtures',
            'users.json'
        )

        print('Users fixture created !')

        with open(path_file, 'w') as file_user:
            file_user.write(json.dumps(users))
