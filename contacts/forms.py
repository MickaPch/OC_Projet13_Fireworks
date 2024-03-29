"""Contacts forms"""
from appliances.models import Appliance
from django import forms

from contacts.models.models import Business, Company, Contact


class CompanyAddForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompanyAddForm, self).__init__(*args, **kwargs)
        self.fields['address1'].required = False
        self.fields['address2'].required = False
        self.fields['zipcode'].required = False

    class Meta:
        model = Company
        fields = [
            'name',
            'description',
            'address1',
            'address2',
            'zipcode',
            'type',
            'city'
        ]

    def add_company(self, user):
        company_name = self.cleaned_data['name'].capitalize()
        company_city = self.cleaned_data['city'].upper()
        self.new_company, self.created = Company.objects.get_or_create(
            name=company_name,
            city=company_city
        )
        self.new_company.user.add(user)
        self.add_company_infos()
        self.add_appliance(user)

    def add_company_infos(self):
        if self.created:
            self.new_company.address1 = self.cleaned_data['address1']
            self.new_company.address2 = self.cleaned_data['address2']
            self.new_company.zipcode = self.cleaned_data['zipcode']
            self.new_company.description = self.cleaned_data['description']
            self.new_company.type = self.cleaned_data['type']
        
        if (
            self.new_company.address1 == ""
            and self.cleaned_data['address1'] != ""
        ):
            self.new_company.address1 = self.cleaned_data['address1']
        if (
            self.new_company.address2 == ""
            and self.cleaned_data['address2'] != ""
        ):
            self.new_company.address2 = self.cleaned_data['address2']
        if (
            self.new_company.zipcode == ""
            and self.cleaned_data['zipcode'] != ""
        ):
            self.new_company.zipcode = self.cleaned_data['zipcode']
        if (
            self.new_company.description == ""
            and self.cleaned_data['description'] != ""
        ):
            self.new_company.description = self.cleaned_data['description']
        if (
            self.new_company.type == ""
            and self.cleaned_data['type'] != ""
        ):
            self.new_company.type = self.cleaned_data['type']

    def add_appliance(self, user):
        new_appliance, created = Appliance.objects.get_or_create(
            company=self.new_company,
            user=user,
            environment_notation=0,
            values_notation=0,
            evolution_notation=0,
            knowledge_notation=0,
            management_notation=0,
            advantages_notation=0,
            notoriety_notation=0,
            office_notation=0
        )


class EditCompanyForm(forms.ModelForm):

    company_pk = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(EditCompanyForm, self).__init__(*args, **kwargs)
        self.fields['address1'].required = False
        self.fields['address2'].required = False
        self.fields['zipcode'].required = False
        self.fields['business'].required = False

    class Meta:
        model = Company
        fields = [
            'name',
            'description',
            'address1',
            'address2',
            'zipcode',
            'city',
            'type',
            'business'
        ]

        widgets = {
            'company_pk': forms.HiddenInput(),
            'type': forms.Select(
                attrs={
                    'class': 'form-control select-company-type',
                    'disabled': True
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
            'address1': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2
                }
            ),
            'address2': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2
                }
            ),
            'business': forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'form-group company-select-business'
                }
            )
        }

    def edit_company(self):

        company = Company.objects.get(
            pk=self.cleaned_data['company_pk']
        )

        company_name = self.cleaned_data['name'].capitalize()
        company_city = self.cleaned_data['city'].upper()

        company.name = company_name
        company.city = company_city
        company.address1 = self.cleaned_data['address1']
        company.address2 = self.cleaned_data['address2']
        company.zipcode = self.cleaned_data['zipcode']
        company.description = self.cleaned_data['description']
        company.type = self.cleaned_data['type']

        for business in self.cleaned_data['business']:
            company.business.add(business)

        company.save()


class CompanyDeleteForm(forms.ModelForm):

    company_pk = forms.IntegerField()

    class Meta:
        model = Company
        fields = [
            'company_pk'
        ]

        widgets = {
            'company_pk': forms.HiddenInput()
        }

    def delete_company(self, user):
        self.company_to_delete = Company.objects.get(
            pk=self.cleaned_data['company_pk']
        )
        self.company_to_delete.user.remove(user)
        self.delete_appliance(user)

    def delete_appliance(self, user):
        appliance_to_delete = Appliance.objects.filter(
            company=self.company_to_delete,
            user=user
        )
        appliance_to_delete.update(
            user=None
        )

class AddContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'company',
            'phone_number',
            'email'
        ]

    def add_contact(self, user):
        company = Company.objects.get(
            name=self.cleaned_data['company']
        )
        first_name = self.cleaned_data['first_name'].capitalize()
        last_name = self.cleaned_data['last_name'].upper()
        new_contact, created = Contact.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            company=company
        )
        if created:
            new_contact.phone_number = self.cleaned_data['phone_number']
            new_contact.email = self.cleaned_data['email']
        new_contact.user.add(user)

        new_contact.save()

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
            'contact_pk': forms.HiddenInput(),
            'company': forms.Select(
                attrs={
                    'class': 'form-control contact-company',
                    'disabled': True
                }
            )
        }

    def edit_contact(self):

        contact = Contact.objects.get(
            pk=self.cleaned_data['contact_pk']
        )

        first_name = self.cleaned_data['first_name'].capitalize()
        last_name = self.cleaned_data['last_name'].upper()

        contact.first_name = first_name
        contact.last_name = last_name
        contact.phone_number = self.cleaned_data['phone_number']
        contact.email = self.cleaned_data['email']
        contact.company = self.cleaned_data['company']

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


class DeleteContactForm(forms.ModelForm):

    contact_pk = forms.IntegerField()

    class Meta:
        model = Contact

        fields = ['contact_pk']

        widgets = {
            'contact_pk': forms.HiddenInput()
        }

    def delete_contact(self, user):
        contact_to_delete = Contact.objects.get(
            pk=self.cleaned_data['contact_pk']
        )
        contact_to_delete.user.remove(user)

# class MissionAddForm(forms.ModelForm):

#     class Meta:
#         model = Mission
#         fields = [
#             'title',
#             'description',
#             'company',
#         ]

#     def add_mission(self, user):
#         company = Company.objects.get(
#             name=self.cleaned_data['company']
#         )
#         new_mission, created = Mission.objects.get_or_create(
#             title=self.cleaned_data['title'],
#             description=self.cleaned_data['description'],
#             company=company,
#             user=user
#         )

# class MissionDeleteForm(forms.ModelForm):

#     class Meta:
#         model = Mission
#         fields = [
#             'title',
#             'company',
#         ]

#         widgets = {
#             'title': forms.HiddenInput(),
#             'company': forms.HiddenInput()
#         }

#     def delete_mission(self, user):
#         company = Company.objects.get(
#             name=self.cleaned_data['company']
#         )
#         mission_to_delete = Mission.objects.get(
#             title=self.cleaned_data['title'],
#             company=company,
#             user=user
#         )
#         mission_to_delete.delete()
