from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Appliance(models.Model):

    REGISTERED = 0 # Nothing
    TO_APPLY = 10 # light
    CONTACTED_BY = 20 # info
    FIRST_MEET_INCOMING = 30 # dark
    TECHNICAL_TEST = 40 # warning
    IN_PROGRESS = 50 # primary
    OFFER_RECEIVED = 60 # success
    ABORTED = 70 # secondary
    REFUSED = 80 # danger
    STATUS_CHOICES = [
        (REGISTERED, 'Company registered'),
        (TO_APPLY, 'To apply'),
        (CONTACTED_BY, 'Contacted by company'),
        (FIRST_MEET_INCOMING, 'First meet incoming'),
        (TECHNICAL_TEST, 'Technical test'),
        (IN_PROGRESS, 'In progress'),
        (OFFER_RECEIVED, 'Offer received'),
        (ABORTED, 'Aborted'),
        (REFUSED, 'Refused by company'),
    ]


    company = models.ForeignKey('contacts.Company', on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=REGISTERED)
    estimated_salary = models.FloatField(null=True)
    proposed_salary = models.FloatField(null=True)
    environment_notation = models.IntegerField(
        default=None,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    environment_details = models.TextField(
        default="",
        null=False,
        blank=True
    )
    values_notation = models.IntegerField(
        default=None,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    values_details = models.TextField(
        default="",
        null=False,
        blank=True
    )
    evolution_notation = models.IntegerField(
        default=None,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    evolution_details = models.TextField(
        default="",
        null=False,
        blank=True
    )
    knowledge_notation = models.IntegerField(
        default=None,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    knowledge_details = models.TextField(
        default="",
        null=False,
        blank=True
    )
    management_notation = models.IntegerField(
        default=None,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    management_details = models.TextField(
        default="",
        null=False,
        blank=True
    )
    advantages_notation = models.IntegerField(
        default=None,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    advantages_details = models.TextField(
        default="",
        null=False,
        blank=True
    )
    notoriety_notation = models.IntegerField(
        default=None,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    notoriety_details = models.TextField(
        default="",
        null=False,
        blank=True
    )
    office_notation = models.IntegerField(
        default=None,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    office_details = models.TextField(
        default="",
        null=False,
        blank=True
    )

    class Meta:
        ordering = ['proposed_salary', 'estimated_salary', 'company']

    def __str__(self):
        return self.company.name

class ApplianceStatus(models.Model):
    status = models.CharField(max_length=255, null=False, blank=False)
