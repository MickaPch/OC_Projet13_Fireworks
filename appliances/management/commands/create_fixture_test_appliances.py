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
        appliances = self.generate_appliances(companies)
        skills, skills_per_type = self.get_skills()
        missions = self.generate_missions(skills_per_type, appliances)
        tasks = self.generate_tasks(appliances)

        appliance_datas = appliances + skills + missions + tasks

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
            file_contact.write(json.dumps(appliance_datas))

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

    def generate_appliances(self, companies):

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
                        "status": status,
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
        
        return appliances

    def get_skills(self):

        skills_fixture = 'appliances/fixtures/skills.json'

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(__file__)
                    )
                )
            ),
            skills_fixture
        )

        with open(path_file, 'rb') as skills_file:
            skills = json.load(skills_file)

        skills_per_type = {}
        for skill in skills:
            type = skill['fields']['type']
            skill_pk = skill['pk']
            if type not in skills_per_type:
                skills_per_type[type] = [skill_pk]
            else:
                skills_per_type[type].append(skill_pk)

        return skills, skills_per_type


    def generate_missions(self, skills_per_type, appliances):
        
        missions = []
        model = "appliances.Mission"
        mission_pk = 0
        for appliance in appliances:
            for i in range(random.randint(0, 4)):
                mission_pk += 1
                mission_title = "Mission" + str(mission_pk)
                mission_description = random.choice(['', lorem.paragraph()])
                mission_types = list(range(6))
                mission_skills = []
                for type in mission_types:
                    list_skills_type = skills_per_type[str(type)]
                    if random.choice([True, False]):
                        mission_skills += random.sample(
                            list_skills_type,
                            random.randint(1, max([3, len(list_skills_type)]))
                        )

                mission = {
                    "model": model,
                    "pk": mission_pk,
                    "fields": {
                        "appliance": appliance['pk'],
                        "title": mission_title,
                        "description": mission_description,
                        "skills": mission_skills
                    }
                }

                missions.append(mission)
        
        return missions

    def generate_tasks(self, appliances):
        
        tasks = []
        model = "appliances.Task"
        task_pk = 0
        for appliance in appliances:
            for i in range(random.randint(0, 10)):
                task_pk += 1
                mission_description = lorem.sentence()[:255]
                random_done = random.choice([True, False])

                task = {
                    "model": model,
                    "pk": task_pk,
                    "fields": {
                        "user": appliance['fields']['user'],
                        "appliance": appliance['pk'],
                        "description": mission_description,
                        "done": random_done
                    }
                }

                tasks.append(task)
        
        return tasks
