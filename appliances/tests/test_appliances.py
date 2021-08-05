from django.contrib.auth.models import User
from contacts.models.models import Company
from django.urls.base import reverse

from appliances.tests.test_home_view import AppliancesTest
from appliances.models import Appliance

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
