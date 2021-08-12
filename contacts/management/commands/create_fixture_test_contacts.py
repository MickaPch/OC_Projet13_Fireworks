import os
import json
import random
import lorem
import numpy.random as np_random

from django.core.management.base import BaseCommand

from contacts.models.models import COMPANY_TYPE

class Command(BaseCommand):
    """Command to create contact fixture for tests"""

    def handle(self, *args, **kwargs):
        """Create contact fixture"""

        print('Contacts fixture creation ...')

        users = self.get_users_from_fixture()

        model_company = "contacts.Company"
        companies = []
        cities = self.get_cities()
        first_names = self.get_first_names()
        last_names = self.get_last_names()
        business_datas, business_pk_list = self.get_business_lists()
        self.create_business_fixture(business_datas)
        types = [type_tuple[0] for type_tuple in COMPANY_TYPE]

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
            business = random.sample(business_pk_list, random.randint(1, 4))
            type = random.choice(types)
            description = random.choice(['', lorem.paragraph()])

            company = {
                "model": model_company,
                "pk": i,
                "fields": {
                    "name": company_name,
                    "type": type,
                    "description": description,
                    "address1": address1,
                    "address2": address2,
                    "zipcode": zipcode,
                    "city": city,
                    "user": random_users,
                    "business": business
                }
            }

            companies.append(company)

        contacts = []
        contact_pk = 0
        model_contact = "contacts.Contact"

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

    def get_cities(self):
        
        cities_fixture = 'contacts/fixtures/cities.json'

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(__file__)
                    )
                )
            ),
            cities_fixture
        )

        with open(path_file, 'rb') as cities_file:
            cities = json.load(cities_file)

        return cities

    def get_first_names(self):
        
        first_names_fixture = 'contacts/fixtures/first_names.json'

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(__file__)
                    )
                )
            ),
            first_names_fixture
        )

        with open(path_file, 'rb') as first_names_file:
            first_names = json.load(first_names_file)

        return first_names

    def get_last_names(self):
        
        last_names_fixture = 'contacts/fixtures/last_names.json'

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(__file__)
                    )
                )
            ),
            last_names_fixture
        )

        with open(path_file, 'rb') as last_names_file:
            last_names = json.load(last_names_file)

        return last_names

    def get_business_lists(self):
        
        business_fixture = 'contacts/fixtures/business_list.json'

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(__file__)
                    )
                )
            ),
            business_fixture
        )

        with open(path_file, 'rb') as business_file:
            business_datas = json.load(business_file)

        business_pk_list = list(range(1, len(business_datas) + 1))

        return business_datas, business_pk_list

    def create_business_fixture(self, business_datas):

        business_json = []
        model_business = 'contacts.Business'
        business_pk = 0
        for business_item in business_datas:
            business_pk += 1
            business = {
                "model": model_business,
                "pk": business_pk,
                "fields": {
                    "name": business_item['name'],
                    "fa_icon": business_item['fa_icon'],
                }
            }
            business_json.append(business)

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)
                )
            ),
            'fixtures',
            'business.json'
        )

        with open(path_file, 'w') as file_business:
            file_business.write(json.dumps(business_json))


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
