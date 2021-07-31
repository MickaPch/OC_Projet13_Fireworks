from django.urls import reverse

from contacts.models.models import Company, ContactMember, PhoneNumber, ContactEmail
from contacts.tests.test_contacts_views import ContactsTest


class AddContactMemberTest(ContactsTest):
    """Test add contact member"""

    def test_contact_member_related_to_companies(self):

        contacts_company1 = ContactMember.objects.filter(company=self.company1)
        contacts_company2 = ContactMember.objects.filter(company=self.company2)

        self.assertIn(self.contact1, contacts_company1)
        self.assertIn(self.contact2, contacts_company2)
        self.assertNotIn(self.contact1, contacts_company2)
        self.assertNotIn(self.contact2, contacts_company1)

    def test_user_can_add_contact_member_to_companies(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        response = self.client.post(
            reverse('add_contact_member'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk
            }
        )

        new_contact = ContactMember.objects.get(
            first_name='TestFirstName3'
        )

        contacts_company1 = ContactMember.objects.filter(company=self.company1)
        contacts_company2 = ContactMember.objects.filter(company=self.company2)

        self.assertIn(new_contact, contacts_company2)
        self.assertNotIn(new_contact, contacts_company1)

    def test_contacts_homeview_show_companies_and_contacts(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'company-item">Company1', response.content)
        self.assertIn(b'contact-item">Alain Thomas', response.content)
        self.assertNotIn(b'company-item">Company2', response.content)

    def test_contacts_homeview_show_contact_add_form(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'id_form_add_contact_member', response.content)
        self.assertIn(b'id_last_name', response.content)

    def test_user_can_add_phone_number_when_contact_creation(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        phone_number = "0123456789"

        phone_numbers = PhoneNumber.objects.filter(
            phone_number=phone_number
        )

        self.assertEqual(phone_numbers.count(), 0)

        self.client.post(
            reverse('add_contact_member'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk,
                "phone_number": phone_number
            }
        )

        phone_numbers = PhoneNumber.objects.filter(
            phone_number=phone_number
        )
        new_contact = ContactMember.objects.get(
            first_name='TestFirstName3'
        )

        self.assertEqual(phone_numbers.count(), 1)
        self.assertEqual(new_contact, phone_numbers[0].contact)

    def test_user_cannot_add_wrong_phone_number_letter_when_contact_creation(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        phone_number = "ABCDE"

        phone_numbers = PhoneNumber.objects.filter(
            phone_number=phone_number
        )

        self.assertEqual(phone_numbers.count(), 0)

        self.client.post(
            reverse('add_contact_member'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk,
                "phone_number": phone_number
            }
        )

        phone_numbers = PhoneNumber.objects.filter(
            phone_number=phone_number
        )

        self.assertEqual(phone_numbers.count(), 0)

    def test_user_cannot_add_wrong_phone_number_length_when_contact_creation(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        phone_number = "0123456"

        phone_numbers = PhoneNumber.objects.filter(
            phone_number=phone_number
        )

        self.assertEqual(phone_numbers.count(), 0)

        self.client.post(
            reverse('add_contact_member'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk,
                "phone_number": phone_number
            }
        )

        phone_numbers = PhoneNumber.objects.filter(
            phone_number=phone_number
        )

        self.assertEqual(phone_numbers.count(), 0)

    def test_user_can_add_email_when_contact_creation(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        email = "foo@example.com"

        emails = ContactEmail.objects.filter(
            email=email
        )

        self.assertEqual(emails.count(), 0)

        self.client.post(
            reverse('add_contact_member'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk,
                "email": email
            }
        )

        emails = ContactEmail.objects.filter(
            email=email
        )
        new_contact = ContactMember.objects.get(
            first_name='TestFirstName3'
        )

        self.assertEqual(emails.count(), 1)
        self.assertEqual(new_contact, emails[0].contact)

    def test_user_cannot_add_wrong_email_when_contact_creation(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        email = "@example.com"

        emails = ContactEmail.objects.filter(
            email=email
        )

        self.assertEqual(emails.count(), 0)

        self.client.post(
            reverse('add_contact_member'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk,
                "email": email
            }
        )

        emails = ContactEmail.objects.filter(
            email=email
        )

        self.assertEqual(emails.count(), 0)
