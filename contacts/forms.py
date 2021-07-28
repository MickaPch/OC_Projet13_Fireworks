"""Contacts forms"""
from django import forms

from contacts.models.models import Company, ContactMember, Mission


class CompanyAddForm(forms.ModelForm):
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

class ContactMemberAddForm(forms.ModelForm):

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

class MissionAddForm(forms.ModelForm):

    class Meta:
        model = Mission
        fields = [
            'title',
            'description',
            'company',
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

class MissionDeleteForm(forms.ModelForm):

    class Meta:
        model = Mission
        fields = [
            'title',
            'company',
        ]

        widgets = {
            'title': forms.HiddenInput(),
            'company': forms.HiddenInput()
        }

    def delete_mission(self, user):
        company = Company.objects.get(
            name=self.cleaned_data['company']
        )
        mission_to_delete = Mission.objects.get(
            title=self.cleaned_data['title'],
            company=company,
            user=user
        )
        mission_to_delete.delete()
