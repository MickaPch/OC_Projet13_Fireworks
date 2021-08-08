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
        start_date = datetime.date(2021, 6, 1)
        end_date = datetime.date.today()

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days

        for i in range(random.randint(0, 5)):
            type = random.choice(list(event_types.keys()))
            title = random.choice(event_types[type])
            descrition = random.choice(['', lorem.paragraph()])
            random_number_of_days = random.randrange(days_between_dates)
            date = start_date + datetime.timedelta(days=random_number_of_days)
            appliance_pk = 1

            events.append(
                {
                    "model": model,
                    "pk": i,
                    "fields": {
                        "appliance": appliance_pk,
                        "title": title,
                        "descrition": descrition,
                        "date": date,
                        "type": type
                    }
                }
            )


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
