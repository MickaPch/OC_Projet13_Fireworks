import os
import json
import random

from django.core.management.base import BaseCommand
import lorem
from numpy.random.mtrand import rand

class Command(BaseCommand):
    """Command to create appliance fixture for tests"""

    def handle(self, *args, **kwargs):
        """Create appliance fixture"""

        print('Appliance fixture creation ...')

        companies = self.get_companies()

        model = 'appliances.Appliance'
        status_choices = [0, 10, 20, 30, 40, 50, 60, 70, 80]

        appliance_pk = 0
        appliances = []
        for company in companies:
            company_pk = company['pk']
            users = company['fields']['user']

            for user in users:
                appliance_pk += 1
                estimated_salary = random.randint(25, 45) + round(random.random(), 1)
                proposed_salary = random.randint(25, 45) + round(random.random(), 1)
                status = random.choice(status_choices)
                environment_notation = random.randint(0, 5)
                values_notation = random.randint(0, 5)
                evolution_notation = random.randint(0, 5)
                knowledge_notation = random.randint(0, 5)
                management_notation = random.randint(0, 5)
                advantages_notation = random.randint(0, 5)
                notoriety_notation = random.randint(0, 5)
                office_notation = random.randint(0, 5)
                environment_details = random.choice(['', lorem.sentence()])
                values_details = random.choice(['', lorem.sentence()])
                evolution_details = random.choice(['', lorem.sentence()])
                knowledge_details = random.choice(['', lorem.sentence()])
                management_details = random.choice(['', lorem.sentence()])
                advantages_details = random.choice(['', lorem.sentence()])
                notoriety_details = random.choice(['', lorem.sentence()])
                office_details = random.choice(['', lorem.sentence()])

                appliance = {
                    "model": model,
                    "pk": appliance_pk,
                    "fields": {
                        "company": company_pk,
                        "user": user,
                        "estimated_salary": estimated_salary,
                        "proposed_salary": proposed_salary,
                        "environment_notation": environment_notation,
                        "environment_details": environment_details,
                        "values_notation": values_notation,
                        "values_details": values_details,
                        "evolution_notation": evolution_notation,
                        "evolution_details": evolution_details,
                        "knowledge_notation": knowledge_notation,
                        "knowledge_details": knowledge_details,
                        "management_notation": management_notation,
                        "management_details": management_details,
                        "advantages_notation": advantages_notation,
                        "advantages_details": advantages_details,
                        "notoriety_notation": notoriety_notation,
                        "notoriety_details": notoriety_details,
                        "office_notation": office_notation,
                        "office_details": office_details,
                    }
                }

                appliances.append(appliance)

        print('File creation ...')

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

        print('Appliances fixture created !')

    def get_companies(self):

        print('Retrieving companies ...')

        contact_fixture = 'contacts/fixtures/contacts.json'

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(__file__)
                    )
                )
            ),
            contact_fixture
        )

        companies = []
        with open(path_file, 'rb') as contacts_file:
            contacts = json.load(contacts_file)

            for contact in contacts:
                if contact['model'] == "contacts.Company":
                    companies.append(contact)

        print('List of companies OK')

        return companies
