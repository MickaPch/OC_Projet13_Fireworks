import os
import json
import random
import lorem
import numpy.random as np_random

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to create contact fixture for tests"""

    def handle(self, *args, **kwargs):
        """Create contact fixture"""

        print('Contacts fixture creation ...')

        users = self.get_users_from_fixture()

        model_company = "contacts.Company"
        companies = []
        cities = {
            'TOULOUSE': "31000",
            'CARCASSONNE': "11000",
            'PARIS': "75000",
            'MARSEILLE': "13000",
            'LYON': "69000",
            'DIJON': "21000",
            'BORDEAUX': "33000",
            'LILLE': "59000",
            'GAILLAC': "81600",
            'ALBI': "81000",
            'CASTRES': "81100"
        }
        first_names = [
            'Alain',
            'Thomas',
            'Olivier',
            'Serge',
            'Matthieu',
            'Stéphanie',
            'Sophie',
            'Renaud',
            'Kevin',
            'Mourad',
            'Nora',
            'Carine'
        ]
        last_names = [
            'Wilkinson',
            'Montoya',
            'Marchand',
            'Mazet',
            'Levasseur',
            'Dupuy',
            'Aliker',
            'Cazenave',
            'Allard',
            'Poirier',
            'Faucher',
            'Duval',
            'Blandin'
        ]

        for i in range(1, random.randint(3, 10)):
            if i == 1:
                random_users = users
            else:
                random_users = random.sample(users, random.randint(1, len(users)))
            company_name = "Company" + str(i)
            address1 = np_random.choice(["", lorem.sentence()], p=[0.2, 0.8])
            if address1 != '':
                address2 = np_random.choice(["", lorem.sentence()], p=[0.8, 0.2])
            else:
                address2 = ""

            city = random.choice(list(cities.keys()))
            zipcode = random.choice(['', cities[city]])

            company = {
                "model": model_company,
                "pk": i,
                "fields": {
                    "name": company_name,
                    "address1": address1,
                    "address2": address2,
                    "zipcode": zipcode,
                    "city": city,
                    "user": random_users
                }
            }

            companies.append(company)

        contacts = []
        contact_pk = 0
        model_contact = "contacts.Contact"

        missions = []
        mission_pk = 0
        model_mission = "contacts.Mission"
        for company in  companies:

            company_pk = company["pk"]
            # CONTACTS
            for i in range(random.randint(0, 4)):
                contact_pk += 1
                first_name = random.choice(first_names).capitalize()
                last_name = random.choice(last_names).upper()
                contact_users = random.sample(company['fields']['user'], random.randint(1, len(company['fields']['user'])))

                phone_number = "0" + "".join(str(random.randint(0,9)) for i in range(9))

                email_name = random.choice([
                    first_name.lower(), first_name[0].lower()
                ]) + random.choice(["", ".", '-']) + last_name.lower()
                email = email_name + "@example.com"

                contact = {
                    "model": model_contact,
                    "pk": contact_pk,
                    "fields": {
                        "first_name": first_name,
                        "last_name": last_name,
                        "company": company_pk,
                        "user": contact_users,
                        "phone_number": phone_number,
                        "email": email
                    }
                }
                contacts.append(contact)


        contact_objects = companies + contacts

        print('File creation ...')

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
            file_contact.write(json.dumps(contact_objects))

        print('Contacts fixture created !')

    def get_users_from_fixture(self):

        print('Retrieving users ...')
        user_fixture = 'accounts/fixtures/users.json'

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(__file__)
                    )
                )
            ),
            user_fixture
        )

        with open(path_file, 'rb') as users_file:
            users = json.load(users_file)
            users = list(range(1, len(users) + 1))

        print('List of users OK')

        return users
