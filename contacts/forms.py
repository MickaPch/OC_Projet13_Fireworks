"""Contacts forms"""
from django import forms

from contacts.models.models import Company, Contact, Mission


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

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'company',
            'phone_number',
            'email'
        ]

    def add_contact(self):
        company = Company.objects.get(
            name=self.cleaned_data['company']
        )
        new_contact, created = Contact.objects.get_or_create(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            company=company,
            phone_number=self.cleaned_data['phone_number'],
            email=self.cleaned_data['email']
        )

        return new_contact

    def clean(self):

        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')        

        if (
            email != ""
            and Contact.objects.filter(email=email).exists()
        ):
            raise forms.ValidationError(u'Email addresses must be unique.')
        if (
            phone_number != ""
            and Contact.objects.filter(phone_number=phone_number).exists()
        ):
            raise forms.ValidationError(u'Phone number must be unique.')

        return super().clean()

class EditContactForm(forms.ModelForm):

    contact_pk = forms.IntegerField()

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'company',
            'phone_number',
            'email'
        ]

        widgets = {
            'contact_pk': forms.HiddenInput()
        }

    def edit_contact(self):

        contact = Contact.objects.get(
            pk=self.cleaned_data['contact_pk']
        )

        contact.first_name = self.cleaned_data['first_name']
        contact.last_name = self.cleaned_data['last_name']
        contact.phone_number = self.cleaned_data['phone_number']
        contact.email = self.cleaned_data['email']

        contact.save()

    def clean(self):

        contact_pk = self.cleaned_data.get('contact_pk')
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')        

        if (
            email != ""
            and Contact.objects.filter(email=email).exclude(pk=contact_pk).exists()
        ):
            raise forms.ValidationError(u'Email addresses must be unique.')
        if (
            phone_number != ""
            and Contact.objects.filter(phone_number=phone_number).exclude(pk=contact_pk).exists()
        ):
            raise forms.ValidationError(u'Phone number must be unique.')

        return super().clean()

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
