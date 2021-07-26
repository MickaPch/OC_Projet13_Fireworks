"""Contacts forms"""
from django.forms import ModelForm

from contacts.models import Company, ContactMember, Mission


class CompanyAddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyAddForm, self).__init__(*args, **kwargs)
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

class ContactMemberAddForm(ModelForm):

    class Meta:
        model = ContactMember
        fields = [
            'first_name',
            'last_name',
            'company',
        ]

    def add_contact_member(self):
        company = Company.objects.get(
            name=self.cleaned_data['company']
        )
        new_contact_member, created = ContactMember.objects.get_or_create(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            company=company
        )

class MissionAddForm(ModelForm):

    class Meta:
        model = Mission
        fields = [
            'title',
            'description',
            'company',
            'user',
        ]

    def add_mission(self, user):
        company = Company.objects.get(
            name=self.cleaned_data['company']
        )
        new_mission, created = Mission.objects.get_or_create(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            company=company,
            user=user
        )
