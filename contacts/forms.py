"""Contacts forms"""
from django.forms import ModelForm

from contacts.models import Company


class CompanyAddForm(ModelForm):

    class Meta:
        model = Company
        fields = [
            'name',
            'address1',
            'address2',
            'zipcode',
            'city'
        ]