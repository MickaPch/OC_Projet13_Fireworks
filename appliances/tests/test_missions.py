# from django.urls import reverse
# from appliances.models import Appliance
# from contacts.models.models import Company
# from contacts.tests.test_contacts_views import ContactsTest
# from accounts.models import User


# class AddMissionTest(ContactsTest):
#     """Test add mission"""

#     def test_mission_related_to_appliances(self):

#         missions_appliance1 = Mission.objects.filter(
#             appliance=self.appliance1
#         )
#         missions_appliance2 = Mission.objects.filter(
#             appliance=self.appliance2
#         )
#         missions_company3 = Mission.objects.filter(
#             company=self.company1,
#             user=self.user2
#         )
#         missions_company4 = Mission.objects.filter(
#             company=self.company2,
#             user=self.user2
#         )

#         self.assertIn(self.mission1, missions_company1)
#         self.assertNotIn(self.mission1, missions_company2)
#         self.assertNotIn(self.mission1, missions_company3)
#         self.assertNotIn(self.mission1, missions_company4)

#         self.assertNotIn(self.mission2, missions_company1)
#         self.assertNotIn(self.mission2, missions_company2)
#         self.assertNotIn(self.mission2, missions_company3)
#         self.assertIn(self.mission2, missions_company4)

#     def test_user_can_add_mission_to_companies(self):
#         self.client.login(
#             username='User1',
#             password='pwd$User1'
#         )

#         company = Company.objects.get(name="Company2")
#         company_pk = str(company.pk)

#         response = self.client.post(
#             reverse('add_mission'),
#             data={
#                 "title": "TestMission3",
#                 "description": "description_test",
#                 "company": company_pk
#             }
#         )

#         user1 = User.objects.get(username='User1')
#         user2 = User.objects.get(username='User2')

#         new_mission = Mission.objects.get(
#             title='TestMission3'
#         )

#         missions_company1 = Mission.objects.filter(
#             company=self.company1,
#             user=user1
#         )
#         missions_company2 = Mission.objects.filter(
#             company=self.company2,
#             user=user1
#         )
#         missions_company3 = Mission.objects.filter(
#             company=self.company1,
#             user=user2
#         )
#         missions_company4 = Mission.objects.filter(
#             company=self.company2,
#             user=user2
#         )

#         self.assertNotIn(new_mission, missions_company1)
#         self.assertIn(new_mission, missions_company2)
#         self.assertNotIn(new_mission, missions_company3)
#         self.assertNotIn(new_mission, missions_company4)

#     def test_contacts_homeview_show_companies_and_missions_for_user(self):
#         self.client.login(
#             username='User2',
#             password='pwd$User2'
#         )

#         company_pk = str(Company.objects.get(name="Company2").pk)

#         self.client.post(
#             reverse('add_mission'),
#             data={
#                 "title": "TestMission3",
#                 "description": "description_test",
#                 "company": company_pk
#             }
#         )

#         response = self.client.get(reverse('contacts_home'))

#         self.assertIn(b'company-item">Company2', response.content)
#         self.assertIn(b'mission-item">TestMission3', response.content)

#     def test_contacts_homeview_show_contact_add_form_mission(self):
#         self.client.login(
#             username='User1',
#             password='pwd$User1'
#         )
#         response = self.client.get(reverse('contacts_home'))

#         self.assertIn(b'id_form_add_mission', response.content)
#         self.assertIn(b'id_title', response.content)


# class DeleteMissionTest(ContactsTest):
#     """Test delete missions"""

#     def test_user_can_delete_mission(self):
#         self.client.login(
#             username='User1',
#             password='pwd$User1'
#         )

#         company = Company.objects.get(name="Company1")
#         user1 = User.objects.get(username='User1')
#         mission_to_delete = Mission.objects.get(
#             title="Mission test 1",
#             company=company,
#             user=user1
#         )

#         company_pk = str(company.pk)

#         response = self.client.post(
#             reverse('delete_mission'),
#             data={
#                 "title": "Mission test 1",
#                 "company": company_pk
#             }
#         )

#         user2 = User.objects.get(username='User2')

#         missions_company1 = Mission.objects.filter(
#             company=self.company1,
#             user=user1
#         )
#         missions_company2 = Mission.objects.filter(
#             company=self.company2,
#             user=user1
#         )
#         missions_company3 = Mission.objects.filter(
#             company=self.company1,
#             user=user2
#         )
#         missions_company4 = Mission.objects.filter(
#             company=self.company2,
#             user=user2
#         )

#         self.assertNotIn(mission_to_delete, missions_company1)
#         self.assertNotIn(mission_to_delete, missions_company2)
#         self.assertNotIn(mission_to_delete, missions_company3)
#         self.assertNotIn(mission_to_delete, missions_company4)

#     def test_contacts_homeview_show_contact_delete_form_mission(self):
#         self.client.login(
#             username='User1',
#             password='pwd$User1'
#         )
#         response = self.client.get(reverse('contacts_home'))

#         self.assertIn(b'class_form_delete_mission', response.content)

#     def test_contacts_homeview_show_prepopulate_delete_mission_form(self):
#         self.client.login(
#             username='User1',
#             password='pwd$User1'
#         )
#         response = self.client.get(reverse('contacts_home'))

#         self.assertIn(b'class_form_delete_mission', response.content)
#         self.assertIn(b'id_title', response.content)
