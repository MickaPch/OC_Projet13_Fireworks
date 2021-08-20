from calendar import month_name
from django.db import models
from django.db.models.deletion import CASCADE


class Event(models.Model):
    
    PHONE_CALL = 'PHC'
    MEETING = 'MEE'
    OFFER = 'OFR'
    APPLY = 'APY'
    TEST = 'TES'


    EVENT_TYPES = [
        (PHONE_CALL, 'Phone call'),
        (MEETING, 'Meeting'),
        (OFFER, 'Offer'),
        (APPLY, 'Apply'),
        (TEST, 'Test'),
    ]

    appliance = models.ForeignKey('appliances.Appliance', on_delete=CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=False, default="")
    start_time = models.DateTimeField(auto_now=True, null=False)
    end_time = models.DateTimeField(auto_now=True, null=False)
    type = models.CharField(max_length=3, choices=EVENT_TYPES)

    def get_badge(self):
        
        if self.type == "MEE":
            event_badge = 'badge badge-event-xl badge-primary fas fa-calendar-alt'
        elif self.type == "PHC":
            event_badge = 'badge badge-event-xl badge-secondary fas fa-phone'
        elif self.type == "APY":
            event_badge = 'badge badge-event-xl badge-primary fas fa-calendar-plus'
        elif self.type == "OFR":
            event_badge = 'badge badge-event-xl badge-success fa fa-check'
        elif self.type == "TES":
            event_badge = 'badge badge-event-xl badge-info fas fa-pencil-alt'
        else:
            event_badge = 'badge badge-event-xl badge-primary'

        return event_badge

    def get_badge_bg(self):
        
        if self.type == "MEE":
            event_badge = 'badge badge-primary'
        elif self.type == "PHC":
            event_badge = 'badge badge-secondary'
        elif self.type == "APY":
            event_badge = 'badge badge-primary'
        elif self.type == "OFR":
            event_badge = 'badge badge-success'
        elif self.type == "TES":
            event_badge = 'badge badge-info'
        else:
            event_badge = 'badge badge-primary'

        return event_badge

    def get_time_formatted(self):

        hours = str(self.start_time.hour)
        if len(hours) == 1:
            hours = '0' + hours
        
        minutes = str(self.start_time.minute)
        if len(minutes) == 1:
            minutes = '0' + minutes

        return f'{hours}:{minutes}'

    def get_formatted_date(self):

        month = month_name[self.start_time.month]
        day = str(self.start_time.day)
        year = str(self.start_time.year)

        date = f'{month} {day}, {year}'

        return date
