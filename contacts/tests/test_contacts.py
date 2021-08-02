from django.contrib.auth.models import User
from django.urls import reverse

from contacts.models.models import Company, Contact
from contacts.tests.test_contacts_views import ContactsTest


class AddContactTest(ContactsTest):
    """Test add contact"""

    def test_contact_related_to_companies(self):

        contacts_company1 = Contact.objects.filter(company=self.company1)
        contacts_company2 = Contact.objects.filter(company=self.company2)

        self.assertIn(self.contact1, contacts_company1)
        self.assertIn(self.contact2, contacts_company2)
        self.assertNotIn(self.contact1, contacts_company2)
        self.assertNotIn(self.contact2, contacts_company1)

    def test_user_can_add_contact_to_companies(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        response = self.client.post(
            reverse('add_contact'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk
            }
        )

        new_contact = Contact.objects.get(
            first_name='TestFirstName3'
        )

        contacts_company1 = Contact.objects.filter(company=self.company1)
        contacts_company2 = Contact.objects.filter(company=self.company2)

        self.assertIn(new_contact, contacts_company2)
        self.assertNotIn(new_contact, contacts_company1)

    def test_contacts_homeview_show_companies_and_contacts(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'company-item">Company1', response.content)
        self.assertIn(b'contact-item">Alain THOMAS', response.content)
        self.assertNotIn(b'company-item">Company2', response.content)

    def test_contacts_homeview_show_contact_add_form(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'id_form_contact', response.content)
        self.assertIn(b'id_last_name', response.content)

    def test_user_can_add_phone_number_when_contact_creation(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        phone_number = "0123456789"

        contacts_phone = Contact.objects.filter(
            phone_number=phone_number
        )

        self.assertEqual(contacts_phone.count(), 0)

        self.client.post(
            reverse('add_contact'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk,
                "phone_number": phone_number
            }
        )

        contacts_phone = Contact.objects.filter(
            phone_number=phone_number
        )
        new_contact = Contact.objects.get(
            first_name='TestFirstName3'
        )

        self.assertEqual(contacts_phone.count(), 1)
        self.assertEqual(new_contact, contacts_phone[0])

    def test_user_cannot_add_wrong_phone_number_letter_when_contact_creation(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        phone_number = "ABCDE"

        contacts_phone_number = Contact.objects.filter(
            phone_number=phone_number
        )

        self.assertEqual(contacts_phone_number.count(), 0)

        self.client.post(
            reverse('add_contact'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk,
                "phone_number": phone_number
            }
        )

        contacts_phone_number = Contact.objects.filter(
            phone_number=phone_number
        )

        self.assertEqual(contacts_phone_number.count(), 0)

    def test_user_cannot_add_wrong_phone_number_length_when_contact_creation(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        phone_number = "0123456"

        contacts_phone_number = Contact.objects.filter(
            phone_number=phone_number
        )

        self.assertEqual(contacts_phone_number.count(), 0)

        self.client.post(
            reverse('add_contact'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk,
                "phone_number": phone_number
            }
        )

        contacts_phone_number = Contact.objects.filter(
            phone_number=phone_number
        )

        self.assertEqual(contacts_phone_number.count(), 0)

    def test_user_can_add_email_when_contact_creation(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        email = "foo@example.com"

        contact_emails = Contact.objects.filter(
            email=email
        )

        self.assertEqual(contact_emails.count(), 0)

        self.client.post(
            reverse('add_contact'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk,
                "email": email
            }
        )

        contact_emails = Contact.objects.filter(
            email=email
        )
        new_contact = Contact.objects.get(
            first_name='TestFirstName3'
        )

        self.assertEqual(contact_emails.count(), 1)
        self.assertEqual(new_contact, contact_emails[0])

    def test_user_cannot_add_wrong_email_when_contact_creation(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        email = "@example.com"

        contact_emails = Contact.objects.filter(
            email=email
        )

        self.assertEqual(contact_emails.count(), 0)

        self.client.post(
            reverse('add_contact'),
            data={
                "first_name": "TestFirstName3",
                "last_name": "TestLastName3",
                "company": company_pk,
                "email": email
            }
        )

        contact_emails = Contact.objects.filter(
            email=email
        )

        self.assertEqual(contact_emails.count(), 0)


class EditContactTest(ContactsTest):
    """Test edit contact"""

    def test_user_can_edit_contact(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        contact = Contact.objects.get(
            pk=1
        )

        new_first_name = 'Edit test'
        new_last_name = 'EDIT TEST'
        new_phone_number = '0123456789'
        new_email = 'edit_test@example.com'

        self.assertNotEqual(contact.first_name, new_first_name)
        self.assertNotEqual(contact.last_name, new_last_name)

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

class DeleteContactTest(ContactsTest):
    """Test delete contacts"""

    def test_user_can_delete_contact(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        user1 = User.objects.get(username='User1')
        contact_to_delete = Contact.objects.get(pk=1)

        self.client.post(
            reverse('delete_contact'),
            data={
                "contact_pk": contact_to_delete.pk
            }
        )

        user_contacts = Contact.objects.filter(
            user=user1
        )

        self.assertNotIn(contact_to_delete, user_contacts)

    def test_contacts_homeview_show_contact_delete_form_contact(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'class_form_delete_contact', response.content)
