from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

from contacts.models import validator_fields


ESN = 'ESN'
SOFTWARE = 'SOFT'
ENGINEERING = 'ENG'
INDUSTRY = 'IND'
WEB = 'WEB'
COMPANY_TYPE = [
    (ESN, 'Entreprise de services numériques'),
    (SOFTWARE, 'Editeur de logiciels'),
    (ENGINEERING, 'Ingénierie'),
    (INDUSTRY, 'Industrie'),
    (WEB, 'Création de sites internet')
]

class Business(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)

class Company(models.Model):
    name = models.CharField(max_length=250, default="", null=False)
    type = models.CharField(choices=COMPANY_TYPE, max_length=4, blank=False, null=False)
    description = models.TextField(blank=True, null=False, default="")
    address1 = models.TextField(max_length=1024, null=False, blank=True, default="")
    address2 = models.TextField(max_length=1024, null=False, blank=True, default="")
    zipcode = validator_fields.ZipcodeField(max_length=5, null=False, blank=True, default="")
    city = models.CharField(max_length=250, null=False)
    user = models.ManyToManyField(User)
    business = models.ManyToManyField('contacts.Business')

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

    def format_phonenumber(self):

        preformatted_phone = [self.phone_number[i:i+2] for i in range(0, len(self.phone_number), 2)]

        formatted_phone = '<div class="col-10 contact-phonenumber">'
        for phone_element in preformatted_phone:
            formatted_phone += f'<span class="mr-1">{phone_element}</span>'
        formatted_phone += '</div>'


        return formatted_phone        
