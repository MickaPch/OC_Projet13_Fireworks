from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Appliance(models.Model):
    company = models.ForeignKey('contacts.Company', on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
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
