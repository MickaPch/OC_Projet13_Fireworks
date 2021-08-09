"""Test accounts views"""
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.core.exceptions import ValidationError
from django.http import response
from django.test import TestCase
from django.urls import reverse

from contacts.models.models import Company, Contact


class ContactsTest(TestCase):
    """Settings for contacts tests"""

    fixtures = [
        'users.json',
        'contacts.json'
    ]

    def setUp(self):

        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.company1 = Company.objects.get(pk=1)
        self.company2 = Company.objects.get(pk=2)

        self.contact1 = Contact.objects.get(pk=1)
        self.contact2 = Contact.objects.get(pk=2)

class ContactsViewTest(ContactsTest):
    """Testing contacts view"""

    def test_contacts_only_for_connected(self):
        response = self.client.get(reverse('contacts_home'))
        self.assertFalse(SESSION_KEY in self.client.session)

        redirect_url = f"{reverse('login')}?next={reverse('contacts_home')}"

        self.assertRedirects(response, redirect_url)

    def test_contacts_homeview(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_homeview_show(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'MyJOB - Contacts', response.content)

    def test_contacts_homeview_show_user_contacts(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'My contacts', response.content)

    def test_contacts_homeview_show_contacts(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'contact-item', response.content)

    def test_contacts_homeview_show_only_user_contacts(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('contacts_home'))

        non_user_companies = Company.objects.exclude(user=self.user1)

        company_string = f'company-item">{non_user_companies[0].name}'

        self.assertIn(b'company-item">Company1', response.content)
        self.assertNotIn(bytes(company_string, 'utf-8'), response.content)

    def test_contacts_homeview_show_user_contacts_manyfield(self):
        self.client.login(
            username='User2',
            password='pwd$User2'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'company-item">Company4', response.content)
        self.assertIn(b'company-item">Company2', response.content)


