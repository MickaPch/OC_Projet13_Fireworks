"""Contacts forms"""
from django.forms import ModelForm

from contacts.models import Company


class CompanyAddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyAddForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['address2'].required = False

    class Meta:
        model = Company
        fields = [
            'name',
            'address1',
            'address2',
            'zipcode',
            'city'
        ]

    def add_company(self, user):
        new_company, created = Company.objects.get_or_create(
            name=self.cleaned_data['name'],
            address1=self.cleaned_data['address1'],
            address2=self.cleaned_data['address2'],
            zipcode=self.cleaned_data['zipcode'],
            city=self.cleaned_data['city']
        )
        new_company.user.add(user)
