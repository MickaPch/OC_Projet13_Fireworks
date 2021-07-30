from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import string


def validate_zipcode(value):

    error = ValidationError(
        _('"%(value)s" is invalid. Zipcode must have 5 digits'),
        params={'value': value},
    )

    if (
        len(value) != 5
        or not any(i.isdigit() for i in value)
    ):
        raise error


def validate_phonenumber(value):

    error = ValidationError(
        _('"%(value)s" is invalid. Zipcode must have 10 digits'),
        params={'value': value},
    )

    if (
        len(value) != 10
        or not any(i.isdigit() for i in value)
    ):
        raise error
