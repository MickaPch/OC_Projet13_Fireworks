from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse

from contacts.models.models import Company
from contacts.tests.test_contacts_views import ContactsTest
from contacts.validators.validator_contacts import validate_zipcode


class AddCompanyTest(ContactsTest):
    """Test add companies"""

    def test_user_can_add_new_company(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'id_form_add_company', response.content)
        self.assertIn(b'id_city', response.content)

    def test_user_add_new_company(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        response = self.client.post(
            reverse('add_company'),
            data={
                "name": "COMPANY TEST",
                "address1": "1, Rue TEST",
                "address2": "Bâtiment TEST",
                "zipcode": "31000",
                "city": "TOULOUSE"
            }
        )

        self.assertRedirects(response, reverse('contacts_home'))

        response = self.client.get(reverse('contacts_home'))
        self.assertIn(b'COMPANY TEST', response.content)

    def test_user_add_new_company_invalid_form(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_name = "COMPANY TEST"
        zipcode = "012"

        self.client.post(
            reverse('add_company'),
            data={
                "name": company_name,
                "address1": "COMPANY address",
                "zipcode": zipcode,
                "city": "COMPANY CITY"
            }
        )

        self.assertRaises(ValidationError, validate_zipcode, zipcode)

        company_queryset = Company.objects.filter(
            name=company_name
        )
        self.assertEqual(company_queryset.count(), 0)

        response = self.client.get(reverse('contacts_home'))
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertIn('An error occured', str(messages[0]))

    def test_user_add_new_company_invalid_form_not_digits(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_name = "COMPANY TEST"
        zipcode = "ABCDE"

        self.client.post(
            reverse('add_company'),
            data={
                "name": company_name,
                "address1": "COMPANY address",
                "zipcode": zipcode,
                "city": "COMPANY CITY"
            }
        )

        self.assertRaises(ValidationError, validate_zipcode, zipcode)

        company_queryset = Company.objects.filter(
            name=company_name
        )
        self.assertEqual(company_queryset.count(), 0)

        response = self.client.get(reverse('contacts_home'))
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertIn('An error occured', str(messages[0]))

class EditCompanyTest(ContactsTest):
    """Test edit company"""

    def test_user_can_edit_company(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        company = Company.objects.get(
            pk=1
        )

        new_company_name = 'Edit test'
        new_company_address1 = 'EDIT TEST'
        new_company_address2 = '0123456789'
        new_company_zipcode = '012345'
        new_company_city = 'EDIT TEST CITY'

        self.assertNotEqual(company.name, new_company_name)
        self.assertNotEqual(company.address1, new_company_address1)
        self.assertNotEqual(company.address2, new_company_address2)
        self.assertNotEqual(company.zipcode, new_company_zipcode)
        self.assertNotEqual(company.city, new_company_city)

        self.assertEqual(contact.phone_number, "")

        contact_emails = Contact.objects.filter(
            email=new_email
        )
        self.assertEqual(contact_emails.count(), 0)

        self.client.post(
            reverse('edit_contact'),
            data={
                "contact_pk": contact.pk,
                "first_name": new_first_name,
                "last_name": new_last_name,
                "company": contact.company.pk,
                "phone_number": new_phone_number,
                "email": new_email
            }
        )

        contact = Contact.objects.get(
            pk=1
        )

        self.assertEqual(contact.first_name, new_first_name)
        self.assertEqual(contact.last_name, new_last_name)

        contact_phones = Contact.objects.filter(
            phone_number=new_phone_number
        )
        self.assertEqual(contact_phones.count(), 1)
        self.assertEqual(contact, contact_phones[0])

        contact_emails = Contact.objects.filter(
            email=new_email
        )
        self.assertEqual(contact_emails.count(), 1)
        self.assertEqual(contact, contact_emails[0])

class DeleteCompanyTest(ContactsTest):
    """Test delete companies for user"""

    def setUp(self):

        self.company_name = "Company5"
        self.company_to_delete = Company.objects.get(name=self.company_name)

        self.user1 = User.objects.get(username='User1')
        self.user2 = User.objects.get(username='User2')

        return super().setUp()

    def test_user_can_delete_company(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        list_company_before_delete = Company.objects.filter(
            user=self.user1
        )
        all_companies = Company.objects.all()
        self.assertIn(self.company_to_delete, list_company_before_delete)
        self.assertIn(self.company_to_delete, all_companies)

        company_pk = str(self.company_to_delete.pk)

        self.client.post(
            reverse('delete_company'),
            data={
                "name": self.company_to_delete
            }
        )

        list_company_for_user1 = Company.objects.filter(
            name=self.company_name,
            user=self.user1
        )
        list_company_for_user2 = Company.objects.filter(
            name=self.company_name,
            user=self.user2
        )

        self.assertNotIn(self.company_to_delete, list_company_for_user1)
        self.assertIn(self.company_to_delete, list_company_for_user2)


    # def test_contacts_homeview_show_contact_delete_form_mission(self):
    #     self.client.login(
    #         username='User1',
    #         password='pwd$User1'
    #     )
    #     response = self.client.get(reverse('contacts_home'))

    #     self.assertIn(b'class_form_delete_mission', response.content)

    # def test_contacts_homeview_show_prepopulate_delete_mission_form(self):
    #     self.client.login(
    #         username='User1',
    #         password='pwd$User1'
    #     )
    #     response = self.client.get(reverse('contacts_home'))

    #     self.assertIn(b'class_form_delete_mission', response.content)
    #     self.assertIn(b'id_title', response.content)
