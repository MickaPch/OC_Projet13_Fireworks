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
    date = models.DateField(auto_now=True, null=False)
    type = models.CharField(max_length=3, choices=EVENT_TYPES)
