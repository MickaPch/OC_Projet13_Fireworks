from django.db import models

from contacts.validators import validator_company


class ZipcodeField(models.CharField):
    default_validators = [validator_company.validate_zipcode]