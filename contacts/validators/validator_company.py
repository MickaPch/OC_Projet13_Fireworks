from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_zipcode(value):

    if len(value) != 5:
        raise ValidationError(
            _('%(value)s must have 5 characters'),
            params={'value': value},
        )