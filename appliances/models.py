from myjob_calendar.models import Event
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import User


NOTATIONS_LIST = [
    'environment_notation',
    'values_notation',
    'evolution_notation',
    'knowledge_notation',
    'management_notation',
    'advantages_notation',
    'notoriety_notation',
    'office_notation'
]
NOTATIONS_LABELS = [
    'Environment',
    'Values',
    'Evolution',
    'Knowledge',
    'Management',
    'Advantages',
    'Notoriety',
    'Office'
]

REGISTERED = 0 # dark
TO_DO = 10 # warning
IN_PROGRESS = 20 # primary
OFFER_RECEIVED = 30 # success
ABORTED = 40 # secondary
REFUSED = 50 # danger

STATUS_CHOICES = [
    (REGISTERED, 'Company registered'),
    (TO_DO, 'Action to do'),
    (IN_PROGRESS, 'In progress'),
    (OFFER_RECEIVED, 'Offer received'),
    (ABORTED, 'Aborted'),
    (REFUSED, 'Refused by company'),
]

LANGUAGE = 0
FRAMEWORK = 1
TOOL = 2
LIBRARY = 3
OS = 4
METHOD = 5

SKILL_TYPES = [
    (LANGUAGE, 'Language'),
    (FRAMEWORK, 'Framework'),
    (TOOL, 'Tool'),
    (LIBRARY, 'Library'),
    (OS, 'OS'),
    (METHOD, 'Method'),
]


class Appliance(models.Model):


    company = models.ForeignKey('contacts.Company', on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=REGISTERED)
    estimated_salary = models.FloatField(null=True)
    proposed_salary = models.FloatField(null=True)
    environment_notation = models.IntegerField(
        default=0,
        null=False,
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
        default=0,
        null=False,
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
        default=0,
        null=False,
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
        default=0,
        null=False,
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
        default=0,
        null=False,
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
        default=0,
        null=False,
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
        default=0,
        null=False,
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
        default=0,
        null=False,
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

    def get_notation(self):
        notations = [
            self.environment_notation,
            self.values_notation,
            self.evolution_notation,
            self.knowledge_notation,
            self.management_notation,
            self.advantages_notation,
            self.notoriety_notation,
            self.office_notation
        ]

        notations = [notation for notation in notations if notation > 0]

        if len(notations) >= 3:
            mean = round(sum(notations) / len(notations), 2)
        else:
            mean = 0

        return mean

    def get_notations_list(self):
        appliance_notations = [
            self.environment_notation,
            self.values_notation,
            self.evolution_notation,
            self.knowledge_notation,
            self.management_notation,
            self.advantages_notation,
            self.notoriety_notation,
            self.office_notation
        ]

        return appliance_notations

    def get_events(self):

        events = Event.objects.filter(
            appliance=self.pk
        ).order_by('-start_time')

        return reversed(events[:3])

    def get_tasks(self):

        tasks = Task.objects.filter(
            appliance=self.pk,
            user=self.user
        ).order_by('id')

        return tasks

    def get_tasks_count(self):

        total_tasks = self.get_tasks().count()

        tasks_done = Task.objects.filter(
            appliance=self.pk,
            user=self.user,
            done=True
        ).count()

        return f"{tasks_done} / {total_tasks}"

    def get_all_choice(self):

        choices = []
        for appliance in self.objects.all():
            choices.append(
                (appliance.pk, appliance.company.name)
            )
        
        return choices


class Skill(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    type = models.IntegerField(choices=SKILL_TYPES, blank=True, null=True)
    related = models.ForeignKey(to='appliances.Skill', on_delete=CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='skills', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Mission(models.Model):
    appliance = models.ForeignKey('appliances.Appliance', on_delete=CASCADE)
    title = models.CharField(max_length=250, null=False)
    description = models.TextField(null=False)
    skills = models.ManyToManyField('appliances.Skill')

    class Meta:
        ordering = ['appliance', 'title']

    def __str__(self):
        return self.title


class Task(models.Model):

    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    appliance = models.ForeignKey('appliances.Appliance', on_delete=CASCADE, blank=True, null=True)
    description = models.CharField(max_length=255, null=False, blank=False)
    done = models.BooleanField(default=False, null=False)
