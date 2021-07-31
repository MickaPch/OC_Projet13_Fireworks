"""Contacts forms"""
from django import forms

from contacts.models.models import Company, ContactEmail, ContactMember, Mission, PhoneNumber


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


class CompanyDeleteForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = [
            'name'
        ]

        widgets = {
            'name': forms.HiddenInput()
        }

    def delete_company(self, user):
        company_to_delete = Company.objects.get(
            name=self.cleaned_data['name']
        )
        company_to_delete.user.remove(user)


class PhoneNumberAddForm(forms.ModelForm):

    class Meta:
        model = PhoneNumber
        fields = [
            'phone_number'
        ]

    def add_phone_number(self, contact):
        new_phone_number, created = PhoneNumber.objects.get_or_create(
            phone_number=self.cleaned_data['phone_number'],
            contact=contact
        )

class EmailAddForm(forms.ModelForm):

    class Meta:
        model = ContactEmail
        fields = [
            'email'
        ]

    def add_email(self, contact):
        new_email, created = ContactEmail.objects.get_or_create(
            email=self.cleaned_data['email'],
            contact=contact
        )

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

        return new_contact_member

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
