from django.contrib.auth.models import User
from contacts.models.models import Company
from django.test import TestCase
from django.urls.base import reverse

from myjob_calendar.models import Event

class AppliancesTest(TestCase):
    """Settings for appliances tests"""

    fixtures = [
        'users.json',
        'contacts.json',
        'appliances.json',
        'events.json'
    ]

    def setUp(self):

        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.company1 = Company.objects.get(pk=1)
        self.company2 = Company.objects.get(pk=2)

        self.contact1 = Contact.objects.get(pk=1)
        self.contact2 = Contact.objects.get(pk=2)

        self.mission1 = Mission.objects.get(pk=1)
        self.mission2 = Mission.objects.get(pk=6)

class AppliancesCompanyRelationTest(AppliancesTest):

    def test_appliance_is_added_when_user_add_company(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        user = User.objects.get(username='User1')
        company_name = 'test'

        appliances = Appliance.objects.filter(
            company__name=company_name,
            user=user
        )

        self.assertEqual(appliances.count(), 0)

        self.client.post(
            reverse('add_company'),
            {
                'name': company_name,
                'city': 'city_test'
            }
        )

        appliances = Appliance.objects.filter(
            company__name=company_name,
            user=user
        )

        self.assertNotEqual(appliances.count(), 0)

    def test_appliance_is_deleted_when_user_delete_company(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )
        user = User.objects.get(username='User1')
        company = Company.objects.get(pk=1)

        appliances_for_company = Appliance.objects.filter(
            company=company,
            user=user
        )
        self.assertEqual(appliances_for_company.count(), 1)

        self.client.post(
            reverse('delete_company'),
            {
                'company_pk': company.pk
            }
        )

        appliances_for_company = Appliance.objects.filter(
            company=company,
            user=user
        )

        self.assertEqual(appliances_for_company.count(), 0)

    def test_user_can_update_appliances(self):
        self.client.login(
            username='User1',
            password='pwd$User1'
        )

        response = self.client.get(reverse('appliances_home'))

        self.assertIn(b'edit-appliance', response.content)


class TestApplianceNotations(AppliancesTest):

    def test_get_appliance_notations(self):

        appliances = Appliance.objects.all()
        for appliance in appliances:
            self.assertNotEqual(appliance.get_notation(), None)
