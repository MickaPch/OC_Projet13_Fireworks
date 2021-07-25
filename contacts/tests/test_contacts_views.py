"""Test accounts views"""
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.http import response
from django.test import TestCase
from django.urls import reverse

from contacts.models import Company


class ContactsViewTest(TestCase):
    """Testing contacts view"""

    def setUp(self):

        self.user1 = User.objects.create_user(
            'test1',
            'test1@mailtest.com',
            'testpassword'
        )
        self.user2 = User.objects.create_user(
            'test2',
            'test2@mailtest.com',
            'testpassword'
        )
        self.contact1 = Company.objects.create(
            name="Contact1"
        )
        self.contact2 = Company.objects.create(
            name="Contact2"
        )
        self.contact1.user.add(self.user1, self.user2)
        self.contact2.user.add(self.user2)

    def test_contacts_only_for_connected(self):
        response = self.client.get(reverse('contacts_home'))
        self.assertFalse(SESSION_KEY in self.client.session)

        redirect_url = f"{reverse('login')}?next={reverse('contacts_home')}"

        self.assertRedirects(response, redirect_url)

    def test_contacts_homeview(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_homeview_show(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'MyJOB - Contacts', response.content)

    def test_contacts_homeview_show_user_contacts(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'My contacts', response.content)

    def test_contacts_homeview_show_contacts(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'contact-item', response.content)

    def test_contacts_homeview_show_only_user_contacts(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'Contact1', response.content)
        self.assertNotIn(b'Contact2', response.content)

    def test_contacts_homeview_show_user_contacts_manyfield(self):
        self.client.login(
            username= 'test2',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'Contact1', response.content)
        self.assertIn(b'Contact2', response.content)

    def test_user_can_add_new_company(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'<form', response.content)
        self.assertIn(b'id_city', response.content)

    def test_user_add_new_company(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )

        self.client.post(
            reverse('add_company'),
            data={
                "name": "COMPANY TEST",
                "address1": "1, Rue TEST",
                "address2": "Bâtiment TEST",
                "zipcode": "31000",
                "city": "TOULOUSE"
            }
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'COMPANY TEST', response.content)
