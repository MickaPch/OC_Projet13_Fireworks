"""Test accounts views"""
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.http import response
from django.test import TestCase
from django.urls import reverse

from contacts.models import Company, ContactMember, Mission


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
        self.company1 = Company.objects.create(
            name="Company1"
        )
        self.company2 = Company.objects.create(
            name="Company2"
        )
        self.company1.user.add(self.user1, self.user2)
        self.company2.user.add(self.user2)

        self.contact1 = ContactMember.objects.create(
            first_name='TestFirstName1',
            last_name='TestLastName1',
            company=self.company1
        )
        self.contact2 = ContactMember.objects.create(
            first_name='TestFirstName2',
            last_name='TestLastName2',
            company=self.company2
        )

        self.mission1 = Mission.objects.create(
            title='TestMission1',
            description='description1',
            company=self.company1,
            user=self.user1
        )
        self.mission2 = Mission.objects.create(
            title='TestMission2',
            description='description2',
            company=self.company2,
            user=self.user2
        )
        

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

        self.assertIn(b'company-item">Company1', response.content)
        self.assertNotIn(b'company-item">Company2', response.content)

    def test_contacts_homeview_show_user_contacts_manyfield(self):
        self.client.login(
            username= 'test2',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'company-item">Company1', response.content)
        self.assertIn(b'company-item">Company2', response.content)

    def test_user_can_add_new_company(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'id_form_add_company', response.content)
        self.assertIn(b'id_city', response.content)

    def test_user_add_new_company(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
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
            username= 'test1',
            password= 'testpassword'
        )

        response = self.client.post(
            reverse('add_company'),
            data={
                "name": "COMPANY TEST"
            }
        )

        self.assertNotIn(b'COMPANY TEST', response.content)

    def test_contact_member_related_to_companies(self):

        contacts_company1 = ContactMember.objects.filter(company=self.company1)
        contacts_company2 = ContactMember.objects.filter(company=self.company2)
        
        self.assertIn(self.contact1, contacts_company1)
        self.assertIn(self.contact2, contacts_company2)
        self.assertNotIn(self.contact1, contacts_company2)
        self.assertNotIn(self.contact2, contacts_company1)

    def test_user_can_add_contact_member_to_companies(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
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
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'company-item">Company1', response.content)
        self.assertIn(b'contact-item">TestLastName1', response.content)
        self.assertNotIn(b'company-item">Company2', response.content)

    def test_contacts_homeview_show_contact_add_form(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'id_form_add_contact_member', response.content)
        self.assertIn(b'id_last_name', response.content)


    def test_mission_related_to_companies(self):

        missions_company1 = Mission.objects.filter(
            company=self.company1,
            user=self.user1
        )
        missions_company2 = Mission.objects.filter(
            company=self.company2,
            user=self.user1
        )
        missions_company3 = Mission.objects.filter(
            company=self.company1,
            user=self.user2
        )
        missions_company4 = Mission.objects.filter(
            company=self.company2,
            user=self.user2
        )
        
        self.assertIn(self.mission1, missions_company1)
        self.assertNotIn(self.mission1, missions_company2)
        self.assertNotIn(self.mission1, missions_company3)
        self.assertNotIn(self.mission1, missions_company4)

        self.assertNotIn(self.mission2, missions_company1)
        self.assertNotIn(self.mission2, missions_company2)
        self.assertNotIn(self.mission2, missions_company3)
        self.assertIn(self.mission2, missions_company4)


    def test_user_can_add_mission_to_companies(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )

        company = Company.objects.get(name="Company2")
        company_pk = str(company.pk)

        response = self.client.post(
            reverse('add_mission'),
            data={
                "title": "TestMission3",
                "description": "description_test",
                "company": company_pk
            }
        )

        user1 = User.objects.get(username='test1')
        user2 = User.objects.get(username='test2')

        new_mission = Mission.objects.get(
            company=company,
            user=user1
        )

        missions_company1 = Mission.objects.filter(
            company=self.company1,
            user=user1
        )
        missions_company2 = Mission.objects.filter(
            company=self.company2,
            user=user1
        )
        missions_company3 = Mission.objects.filter(
            company=self.company1,
            user=user2
        )
        missions_company4 = Mission.objects.filter(
            company=self.company2,
            user=user2
        )

        self.assertNotIn(new_mission, missions_company1)
        self.assertIn(new_mission, missions_company2)
        self.assertNotIn(new_mission, missions_company3)
        self.assertNotIn(new_mission, missions_company4)

    def test_contacts_homeview_show_companies_and_missions_for_user(self):
        self.client.login(
            username= 'test2',
            password= 'testpassword'
        )

        company_pk = str(Company.objects.get(name="Company2").pk)

        self.client.post(
            reverse('add_mission'),
            data={
                "title": "TestMission3",
                "description": "description_test",
                "company": company_pk
            }
        )

        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'company-item">Company2', response.content)
        self.assertIn(b'mission-item">TestMission3', response.content)

    def test_contacts_homeview_show_contact_add_form_mission(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'id_form_add_mission', response.content)
        self.assertIn(b'id_title', response.content)


    def test_user_can_delete_mission(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )

        company = Company.objects.get(name="Company1")
        user1 = User.objects.get(username='test1')
        mission_to_delete = Mission.objects.get(
            title="TestMission1",
            company=company,
            user=user1
        )
        
        company_pk = str(company.pk)

        response = self.client.post(
            reverse('delete_mission'),
            data={
                "title": "TestMission1",
                "company": company_pk
            }
        )

        user2 = User.objects.get(username='test2')

        missions_company1 = Mission.objects.filter(
            company=self.company1,
            user=user1
        )
        missions_company2 = Mission.objects.filter(
            company=self.company2,
            user=user1
        )
        missions_company3 = Mission.objects.filter(
            company=self.company1,
            user=user2
        )
        missions_company4 = Mission.objects.filter(
            company=self.company2,
            user=user2
        )

        self.assertNotIn(mission_to_delete, missions_company1)
        self.assertNotIn(mission_to_delete, missions_company2)
        self.assertNotIn(mission_to_delete, missions_company3)
        self.assertNotIn(mission_to_delete, missions_company4)

    def test_contacts_homeview_show_contact_delete_form_mission(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'class_form_delete_mission', response.content)

    def test_contacts_homeview_show_prepopulate_delete_mission_form(self):
        self.client.login(
            username= 'test1',
            password= 'testpassword'
        )
        response = self.client.get(reverse('contacts_home'))

        self.assertIn(b'class_form_delete_mission', response.content)
        self.assertIn(b'id_title', response.content)
