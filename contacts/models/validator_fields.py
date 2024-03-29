from django.db import models

from contacts.validators import validator_contacts


class ZipcodeField(models.CharField):
    default_validators = [validator_contacts.validate_zipcode]

class PhoneNumberField(models.CharField):
    default_validators = [validator_contacts.validate_phonenumber]
