"""Test accounts views"""
from django.contrib.auth import SESSION_KEY
from django.core.exceptions import ValidationError
from django.http import response
from django.test import TestCase
from django.urls import reverse

from contacts.models.models import Company, Contact
from appliances.models import Appliance, Mission
from accounts.models import User


class AppliancesTest(TestCase):
    """Settings for appliances tests"""

    fixtures = [
        'users.json',
        'contacts.json',
        'appliances.json'
    ]

    def setUp(self):

        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.company1 = Company.objects.get(pk=1)
        self.company2 = Company.objects.get(pk=2)

        self.contact1 = Contact.objects.get(pk=1)
        self.contact2 = Contact.objects.get(pk=2)

        self.appliance1 = Appliance.objects.get(pk=1)
        self.appliance2 = Appliance.objects.get(pk=2)

        # self.mission1 = Mission.objects.get(pk=1)
        # self.mission2 = Mission.objects.get(pk=2)

class AppliancesViewTest(AppliancesTest):
    """Testing appliances view"""

    def test_appliances_only_for_connected(self):
        response = self.client.get(reverse('appliances_home'))
        self.assertFalse(SESSION_KEY in self.client.session)

        redirect_url = f"{reverse('login')}?next={reverse('appliances_home')}"

        self.assertRedirects(response, redirect_url)

    def test_appliances_homeview(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('appliances_home'))
        self.assertEqual(response.status_code, 200)

    def test_appliances_homeview_show(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('appliances_home'))

        self.assertIn(b'MyJOB - Appliances', response.content)

    def test_appliances_homeview_show_user_appliances(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('appliances_home'))

        self.assertIn(b'My appliances', response.content)

    def test_appliances_homeview_show_appliances_items(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('appliances_home'))

        self.assertIn(b'appliance-item', response.content)

    def test_contacts_homeview_show_only_user_appliances(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        response = self.client.get(reverse('appliances_home'))

        not_user_appliances = Appliance.objects.exclude(user=self.user1)
        appliance_string = f'appliance-item">{not_user_appliances[0].company.name}'

        self.assertIn(b'appliance-item">Company1', response.content)
        self.assertNotIn(bytes(appliance_string, 'utf-8'), response.content)
