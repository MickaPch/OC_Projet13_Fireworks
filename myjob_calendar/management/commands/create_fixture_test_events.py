import os
import json
import random
import lorem
import datetime

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to create event fixture for tests"""

    def handle(self, *args, **kwargs):
        """Create event fixture"""

        print('Event fixture creation ...')

        appliances = self.get_appliances()

        events = []
        model = "myjob_calendar.Event"
        event_types = {
            'PHC': [
                'Phone call with manager',
                'Phone call with CEO',
                'Phone call with engineer',
                'Phone call with developer',
                'Meeting planned',
                'Introduction',
                'Company informations',
            ],
            'MEE': [
                'Meeting with manager',
                'Meeting with CEO',
                'Meeting with engineer',
                'Meeting with developer',
                'Proposal',
                'Technical meeting',
            ],
            'OFR': [
                'Phone call offer received',
                'Phone call offer received',
                'Offer talk',
                'Negociation',
            ],
            'APY' : [
                'To apply',
                'Email to send',
                'To call',
                'To throw back',
            ],
            'TES': [
                'Technical test to do',
                'Personal test',
                'Technical test to send',
            ]
        }
        start_date = datetime.datetime(2021, 6, 1)
        end_date = datetime.datetime.today()

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days

        event_pk = 0
        for appliance in appliances:
            appliance_pk = appliance['pk']
            for i in range(random.randint(0, 5)):
                event_pk += 1

                type = random.choice(list(event_types.keys()))
                title = random.choice(event_types[type])
                descrition = random.choice(['', lorem.paragraph()])
                start_date_event = start_date + datetime.timedelta(
                    days=random.randrange(days_between_dates),
                    hours=random.randrange(23),
                    minutes=random.randrange(59)
                )
                days_between_event = datetime.datetime(2021, 12, 31) - start_date_event
                end_date_event = start_date_event + datetime.timedelta(
                    days=random.randrange(days_between_event.days),
                    hours=random.randrange(23),
                    minutes=random.randrange(59)
                )


                event = {
                    "model": model,
                    "pk": event_pk,
                    "fields": {
                        "appliance": appliance_pk,
                        "title": title,
                        "description": descrition,
                        "start_time": str(start_date_event),
                        "end_time": str(end_date_event),
                        "type": type
                    }
                }

                events.append(event)

        print('File creation ...')

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)
                )
            ),
            'fixtures',
            'events.json'
        )

        with open(path_file, 'w') as file_events:
            file_events.write(json.dumps(events))

        print('Events fixture created !')

    def get_appliances(self):

        print('Retrieving appliances ...')
        appliance_fixture = 'appliances/fixtures/appliances.json'

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(__file__)
                    )
                )
            ),
            appliance_fixture
        )

        appliances = []
        with open(path_file, 'rb') as appliances_file:
            json_appliances = json.load(appliances_file)

            for appliance in json_appliances:
                if appliance['model'] == "appliances.Appliance":
                    appliances.append(appliance)

        print('List of appliances OK')

        return appliances
