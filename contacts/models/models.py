from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

from contacts.models import validator_fields

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=250, default="", null=False)
    address1 = models.TextField(max_length=1024, null=False, blank=True, default="")
    address2 = models.TextField(max_length=1024, null=False, blank=True, default="")
    zipcode = validator_fields.ZipcodeField(max_length=5, null=False, blank=True, default="")
    city = models.CharField(max_length=250, null=False)
    user = models.ManyToManyField(User)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=250, null=False)
    last_name = models.CharField(max_length=250, null=False)
    company = models.ForeignKey('contacts.Company', on_delete=CASCADE)
    phone_number = validator_fields.PhoneNumberField(max_length=10, null=False, blank=True, default="")
    email = models.EmailField(max_length=254, null=False, blank=True)
    user = models.ManyToManyField(User)

    class Meta:
        ordering = ['company', 'last_name']

    def __str__(self):
        return self.last_name

